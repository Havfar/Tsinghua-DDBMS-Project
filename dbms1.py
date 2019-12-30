from flask import Flask
from flask import request
import utils
import config
import json
from hiveClient import HiveClient
from Models.User import User
from Models.Article import Article
from Models.Read import Read
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return 'Hello World from dbms1'
 

# just for testing json
@app.route('/postjson', methods = ['POST'])
def postjson():
    # mimetype must be json
    content = request.json
    return content

# create a read for when a user reads an article
@app.route('/create_read/', methods=['GET'])
def create_read():
    # get uid and aid
    uid = request.args.get('uid')
    aid = request.args.get('aid')

    # create read id
    rid = utils.create_id('r')

    # create timestamp
    timestamp = utils.get_current_timestamp()

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)
    
    # Create readobject
    new_read = Read(rid=rid, aid=aid, uid=uid, timestamp=timestamp, read_time_length=0, read_sequence=0, read_or_not=True, agree_or_not=True, comment_or_not=False, share_or_not=False, comment_detail="", input_string=None)
    
    # Send read to hive
    client.create_read(new_read)

    return rid


# Creates a user
@app.route('/create_user', methods = ['POST'])
def create_user():
    # Get json
    content = request.json

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    uid = utils.create_id("u")

    # Create User object
    new_user = User(uid=uid, timestamp=utils.get_current_timestamp(), name=content["name"], gender=content["gender"], email=content["email"], age=content["age"], phone=content["phone"], dept=content["department"], region=content["region"], language=content["language"], role=content["role"], prefer_tags=content["prefer_tags"], obtained_credits=content["obtained_credits"], input_string=None)

    print("User created:", new_user)

    # Create user in hive
    client.create_user(new_user)

    return "User created with id: " + uid

# Creates an article
@app.route('/create_article', methods = ['POST'])
def create_article():
    # Get json
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    aid = utils.create_id("a")

    # Create Article object
    new_article = Article(aid=aid, timestamp=utils.get_current_timestamp(), title=content["title"], category=content["category"], abstract=content["abstract"], article_tags=content["article_tags"], author=content["author"], language=content["language"], text=content["text"], image=content["image"], video=content["video"], input_string=None)

    print("Article created:", new_article)
    
    # Create article in hive
    client.create_article(new_article)

    return "Article created with aid: " + aid

# Loads article without uid - does not create new read entry
@app.route('/load_article_from_popular/', methods = ['GET'])
def load_pop_article():
    aid = request.args.get('aid')

     # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get article from hive
    requested_article = client.get_article_by_aid(aid = aid, category=None)

    return requested_article.__dict__

# returns article by aid on json format {}, also updates be_read table and requesting user read_table
@app.route('/load_article/', methods = ['GET'])
def load_article():
    uid = request.args.get('uid')
    aid = request.args.get('aid')

    current_time = utils.get_current_timestamp()

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get article from hive
    requested_article = client.get_article_by_aid(aid = aid, category=None)


    # Create Read object of the loaded article aid and uid
    new_read = Read(rid=utils.create_id('r'), aid=aid, uid=uid, timestamp=current_time, read_or_not=True, read_time_length=0, read_sequence=1, agree_or_not=True, comment_or_not=False, share_or_not=False, comment_detail="")

    # insert new_read into hive
    client.create_read(new_read)

    # load be_read object from client for the aid
    be_read = client.get_be_read_by_aid(aid=aid, page_size=None, page_number=None)

    # uid_list should be a commaseparated string
    # add new uid to the end after a comma, no spaces
    be_read.read_uid_list = be_read.read_uid_list + "," + uid

    # update the be_read object in hive
    client.update_be_read(be_read)
    
    # Sending a dict is the same as sending a json
    return requested_article.__dict__


# returns list of all users [{}]
@app.route('/load_all_users', methods = ['GET'])
def load_all_users():
    # region is hardcoded for this server as it is dbms1
    region = 'Beijing'

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get users from hive []
    all_users = client.get_users_by_region(region=region)
    list_all_users = []

    # Convert users to dicts and append to list
    for user in all_users:
        list_all_users.append(user.__dict__)
    return json.dumps(list_all_users)

# returns list of all users [{}]
@app.route('/load_all_articles', methods = ['GET'])
def load_all_articles():
    # category is hardcoded for this server as it is dbms1
    # only 1 category
    # dbms2 should have both science and technology
    category_science = 'Science'

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get articles from hive []

    all_articles = client.get_articles_by_category(category_science, page_number=0, page_size=15)
    print("received articles")

    list_all_articles = []

    # Convert users to dicts and append to list
    for article in all_articles:
        list_all_articles.append(article.__dict__)
    return json.dumps(list_all_articles)


# returns user object for given uid, returns json {}
@app.route('/load_user/', methods = ['GET'])
def load_user():
    uid = request.args.get('uid')
    print("uid:", uid)

    # Hardcoded region for dbms1
    region = "Beijing"

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get user from hive
    requested_user = client.get_user_by_uid(uid = uid, region=region)
    return requested_user.__dict__

# returns be_read object holding all uid's that has read the article with given aid - json format {}
@app.route('/be_read_by_aid/', methods = ['GET'])
def be_read():
    aid = request.args.get('aid')

    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)
    
    # be_read_table holds a "read_uid_list" string. Needs to be split somehow to get all unique user ids
    be_read_table = client.get_be_read_by_aid(aid = aid, page_size=None, page_number=None)


    return be_read_table.__dict__

# creates a be_read for an article

# Returns all articles read by the uid, returned as json [{}]
@app.route('/user_read_table/', methods = ['GET'])
def user_read_table():
    
    # get uid
    uid = request.args.get('uid')
    
    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get list of read objects
    read_objects_list = client.get_read_by_uid(uid, page_size=None, page_number=None)

    # Convert list of Read objects to list of dicts
    list_of_dicts = []
    for readobj in read_objects_list:
        list_of_dicts.append(readobj.__dict__)
    
    # Returns a json to the app, but it is enclosed in '[]' square brackets.
    # Keep this in mind on the app end of things.
    return json.dumps(list_of_dicts)

# Returns most popular articles by day/week/month
@app.route('/popular_rank/', methods = ['GET'])
def popular_rank():

    # This does not support categories as of time being, but can
    # be implemented. Needs changes to the hiveclient calls.
    
    # filter is the same as granulairty (eg. daily/weekly/monthly)
    # Should be either "weekly", "monthly" or anything.
    filter = request.args.get("filter")

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # List of article objects
    article_list = client.get_pop_rank(filter)


    article_dicts = []
    for article in article_list:
        article_dicts.append(article.__dict__)


    # return dump of the list (json) [{}]
    return json.dumps(article_dicts)



if __name__ == '__main__':
    app.run(port=5000)