from flask import Flask
from flask import request
from flask import send_from_directory
from flask import render_template
import utils
import config
import json
from hiveClient import HiveClient
from Models.User import User
from Models.Article import Article
from Models.Be_Read import Be_read
from Models.Read import Read
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World from dbms1'
   
"""
@app.route('/article/<number>')
def article_number(number):
   return 'GET article number: %s' % number

@app.route('/beijing')
def beijing():
    return render_template('beijing.html')

@app.route('/hongkong')
def hongkong():
    return render_template('hongkong.html')

@app.route('/userinput/')
def userinput():
    if((request.args.get('name') == None) or (request.args.get('lname') == None)):
        return("Please submit a name lastname like '/userinput/?name=\"name\"&lname=\"lname\"', but don't use \'\"\'")
    else:
        name = request.args.get('name')
        secondName = request.args.get('lname')
        returnGibberish = name + secondName
        returnGibberish = ''.join(random.sample(returnGibberish,len(returnGibberish)))
        # random.shuffle((returnGibberish))
        return returnGibberish
"""

# @app.route('/formpost', methods = ['POST'])
# def formpost():
#     if request.method == 'POST':
        
#         newFormListener = formListener()
#         readFormResponse = newFormListener.readForm(request.form)
#         return readFormResponse

"""
@app.route('/testpost',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
       #user = request.form['nm']
       # #return redirect(url_for('success',name = user))
        if(request.args.get('lname') != None):
            return "Received post from " + request.args.get('lname')
        else:
            return "Received your post."
   else:
        #user = request.args.get('nm')
        #return redirect(url_for('success',name = user))
        if(request.args.get('name') != None):
            return "Sending " + request.args.get('name') + "'s post"
        else:
            return "Sending your post."
"""

# just for testing json
@app.route('/postjson', methods = ['POST'])
def postjson():
    # mimetype must be json
    content = request.json
    print("content:", content)
    print("content.name:", content["name"])
    return content

# Creates a user
@app.route('/create_user', methods = ['POST'])
def create_user():
    # Get json
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Create User object
    new_user = User(uid=utils.create_id("u"), timestamp=utils.get_current_timestamp(), name=content["name"], gender=content["gender"], email=content["email"], age=content["age"], phone=content["phone"], dept=content["department"], region=content["region"], language=content["language"], role=content["role"], prefer_tags=content["prefer_tags"], obtained_credits=content["obtained_credits"], input_string=None)

    print("User created:", new_user)

    # Create user in hive
    client.create_user(new_user)

    return "User created"

# Creates an article
@app.route('/create_article', methods = ['POST'])
def create_article():
    # Get json
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Create Article object
    new_article = Article(aid=utils.create_id("a"), timestamp=utils.get_current_timestamp(), title=content["title"], category=content["category"], abstract=content["abstract"], article_tags=content["article_tags"], author=content["author"], language=content["language"], text=content["text"], image=content["image"], video=content["video"], input_string=None)

    print("Article created:", new_article)
    
    # Create article in hive
    client.create_article(new_article)

    return "Article created"


# returns article by aid on json format {}, also updates be_read table and requesting user read_table
@app.route('/load_article', methods = ['GET'])
def load_article():

    content = request.json
    print("Content:", content)
    uid = content["uid"]
    aid = content["aid"]
    current_time = utils.get_current_timestamp()

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get article from hive
    requested_article = client.get_article_by_aid(aid = content["aid"], category=None)


    # Create Read object of the loaded article aid and uid
    new_read = Read(id=None, aid=aid, uid=uid, timestamp=current_time, read_or_not=True, read_time_length=0, read_sequence=1, agree_or_not=True, comment_or_not=None, share_or_not=None, comment_detail=None, input_string=None)

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


# returns user object for given uid, returns json {}
@app.route('/load_user', methods = ['GET'])
def load_user():
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get user from hive
    requested_user = client.get_user_by_uid(uid = content["uid"], region=None)

    return requested_user.__dict__

# returns be_read object holding all uid's that has read the article with given aid - json format {}
@app.route('/be_read_by_aid', methods = ['GET'])
def be_read():
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get Be_Read from hive
    requested_Be_Read = client.get_be_read_by_aid(aid = content["aid"], page_size=None, page_number=None)

    return requested_Be_Read.__dict__

# Returns all articles read by the uid, returned as json [{}]
@app.route('/user_read_table', methods = ['GET'])
def user_read_table():
    content = request.json
    print("Content:", content)

    # Create hiveclient
    client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)

    # Get read articles from hive - returned as list
    requested_read_articles = client.get_user_read_table_by_uid(uid=content["uid"], page_size=None, page_number=None)

    # Convert list of Read objects to list of dicts
    list_of_dicts = []
    for readobj in requested_read_articles:
        list_of_dicts.append(readobj.__dict__)
    
    # Returns a json to the app, but it is enclosed in '[]' square brackets.
    # Keep this in mind on the app end of things.
    return json.dumps(list_of_dicts)





if __name__ == '__main__':
    #querybuilder = queryBuilder("ok", "tableNameTest", "articleTableTest", "userTableTest", "readTableTest", "beReadTableTest", "popularRankTableTest")
    #print(querybuilder.selectUserFromTable(2, None, "region", None, None, "region", 5))
    #print(querybuilder.selectUserFromTable(None, "userID", ">", 23, None, None, None))
    # if no port is provided it defaults to 5000

    app.run(port=5000)