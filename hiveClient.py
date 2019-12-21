import datetime
from typing import List

from PIL import Image
from pyhive import hive

from Models.Article import Article
from Models.Be_Read import Be_read
from Models.Popular_rank import Popular_rank
from Models.Read import Read
from Models.User import User
import uuid
from utils import gen_an_read, gen_an_user, gen_an_article
import numpy as np
import config

class HiveClient:
    def __init__(self, host_name, portNumber, user, password ):
        self.conn = hive.Connection(host=host_name, port=portNumber, username=user, password=password,
                                    auth='CUSTOM')

    # Used to create unique ids to Articles/ Users / Reads/ be_reads / pop_rank
    def create_id(self, prefix):
        return prefix + str(uuid.uuid4())

    # Returns table by name. Possiblity to change selected columns
    def get_table_by_name(self, table_name, columns='*', order_by='asc', page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select ' + columns + ' from ' + table_name
        if page_size != None and page_number != None:
            query += ' limit ' + str(page_size) + ' offset ' + str(page_number*page_size)
        try:
            cur.execute(query)
            result = cur.fetchall()
        except:
            result = "None"
        return result

    # Returns a list of all users whom have read the article
    # May need to change if it is not possible to update table row (e.g check for latest row)
    def get_user_read_by_aid(self, aid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        cur.execute('select * from user_read where aid="' + aid + '"')
        users:List[User] = []
        for user in cur.fetchall():
            user = User(input_string=user)
            users.append(user)
        result = cur.fetchall()
        return result
    
    def get_all_users(self, region, page_size=None, page_number=None):
        cur = self.conn.cursor()
        query = 'select * from users where region ="' + region + '"' 
        if page_size != None and page_number != None:
            query += ' limit ' + str(page_size) + ' offset ' + str(page_number*page_size)
        cur.execute(query)
        result = cur.fetchall()
        user_list = []
        for item in result:
            user_list.append(User(
                uid=item[0], 
                timestamp = item[1], 
                name = item[2], 
                gender=item[3], 
                email = item[4],
                phone = item[5], 
                dept = item[6], 
                language = item[7], 
                role = item[8], 
                prefer_tags = item[9], 
                obtained_credits = item[10], 
                age = item[11], 
                region = item[12])
            )
        return user_list
    
    def get_all_articles(self, category, page_size=None, page_number=None):
        cur = self.conn.cursor()
        query = 'select * from articles where category ="' + category + '"' 
        if page_size != None and page_number != None:
            query += ' limit ' + str(page_size) + ' offset ' + str(page_number*page_size)
        cur.execute(query)
        result = cur.fetchall()
        article_list = []
        for article in result:
            article_list.append(Article(
                aid=article[0], 
                timestamp = article[1], 
                title = article[2], 
                abstract=article[3], 
                article_tags = article[4],
                author = article[5], 
                language = article[6], 
                text = article[7], 
                image = article[8], 
                video = article[9], 
                category = article[10])
            )
        return article_list

    # Used for local testing
    def get_all_tables(self):
        cur = self.conn.cursor()
        cur.execute('show tables')
        result = cur.fetchall()
        return result

    # Used for local testing
    def get_all_databases(self):
        cur = self.conn.cursor()
        cur.execute('show databases')
        result = cur.fetchall()
        return result

    # Used for local testing
    def describe_table(self, table_name):
        cur = self.conn.cursor()
        try:
            cur.execute('describe ' + table_name )
            result = cur.fetchall()
        except:
            result = "None"
        return result

    # Input: User object
    def create_user(self, user):
        cur = self.conn.cursor()
        #cur.execute('insert into table user_table values' + user.__str__())
        cur.execute('insert into table users partition(region ="' + user.region + '") values' + user.__str__())

    # Input: Article object
    def create_article(self, article):
        cur = self.conn.cursor()
        cur.execute('insert into table articles partition(category ="' + article.category + '") values' + article.__str__())

    # Input: Read object
    def create_read(self, read):
        cur = self.conn.cursor()
        cur.execute('insert into table user_read values' + read.__str__())

    # Input: Be_read object
    def create_be_read(self, be_read):
        cur = self.conn.cursor()
        cur.execute('insert into table be_read values' + be_read.__str__())

    # Input: Popular_rank object
    def create_popular_rank(self, pop_rank):
        cur = self.conn.cursor()
        cur.execute('insert into table popular_rank partition(category = "'+ pop_rank.category +'") values' + pop_rank.__str__())

    # Experimenting with joins
    # NOT FOR PRODUCTION
    def get_user_read_table_by_user(self, user, page_size=None, page_number = None):
        cur = self.conn.cursor()
        cur.execute('select  * '
                    'from (select aid, uid from user_read where uid="' + user.uid +'") r '
                    'left outer join (select uid, name from user_table) usr '
                    'on ( r.uid = usr.uid) '
                    'left outer join (select aid, title from article_table) artcl '
                    'on (r.aid = artcl.aid) '
                    )
        result = cur.fetchall()
        return result

    def get_user_read_table_by_uid(self, uid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select  * ' \
                'from user_read  ' \
                'where uid="' + uid + '"'

        if page_size != None and page_size != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string = element))
        return read_list

    def get_user_read_table_by_read(self, read, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select  * ' \
                'from (select aid, uid from user_read where id="' + read.id +'") r ' \
                'left outer join (select uid, name from user_table) usr ' \
                'on ( r.uid = usr.uid) ' \
                'left outer join (select aid, title from article_table) artcl ' \
                'on (r.aid = artcl.aid) '

        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number*page_size)
        cur.execute(query)
        result = cur.fetchall()
        return result

    def get_article_by_aid(self, aid, category = None):
        cur = self.conn.cursor()
        if category == None:
            query = 'select * from articles where aid="' + aid + '"'
        else:
            query ='select * from articles where articles.aid="' + aid + '" and articles.category = "' + category + '")'
        cur.execute(query)
        article = Article(input_string=str(cur.fetchall()))
        return article

    # Should provide region
    def get_user_by_uid(self, uid, region = None):
        if region == None:
            cur = self.conn.cursor()
            cur.execute('select * from users where users.uid="' + uid + '"')
        else:
            cur = self.conn.cursor()
            cur.execute('select * from users where (users.uid="' + uid + '" and users.region = "' + region + '")')
        user = User(input_string=str(cur.fetchall()))
        return user

    def get_users_by_region(self, region, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select * from users where region="' + region + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        output = cur.fetchall()
        print(output.__len__())
        users = []
        for item in output:
            users.append(User(str(item)))
        return users

    def get_articles_by_category(self, category, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select * from articles where category="' + category + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        output = cur.fetchall()
        print(output.__len__())
        articles = []
        for item in output:
            articles.append(User(str(item)))
        return articles

    # Returns a list of read objects whom have commented
    def get_article_reads_by_aid(self, aid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select * from user_read where (user_read.aid = "' + aid + '" and user_read.comment_or_not = 1) order by var_timestamp desc'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string=str(element)))
        return read_list

    #Retruns the read from an user and an article
    def get_read(self, aid, uid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        cur.execute('select * from user_read where (user_read.aid ="' + aid + '" and user_read.uid = "'+ uid +'")')
        read = Read(input_string=str(cur.fetchall()))
        return read

    def get_be_read_by_aid(self, aid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select * from be_read where be_read.aid = "' + aid + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        be_read = Be_read(input_string = str(cur.fetchall()))
        return be_read

    # Returns a list of read objects whom have read
    def get_read_count_by_aid(self, aid, page_size=None, page_number = None):
        cur = self.conn.cursor()
        query = 'select * from user_read where (user_read.aid = "' + aid + '" and user_read.read_or_not = 1) order by var_timestamp desc'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string=str(element)))
        return read_list

    def update_read(self, read):
        cur = self.conn.cursor()
        cur.execute('update user_read set'
                    + ' var_timestamp = ' + read.timestamp
                    + ', read_or_not = ' + read.read_or_not
                    + ', read_time_length = ' + read.read_time_length
                    + ', read_sequence = ' +read.read_sequence
                    + ', agree_or_not = ' + read.agree_or_not
                    + ', comment_or_not = ' + read.comment_or_not
                    + ', share_or_not = ' + read.share_or_not
                    + ', comment_detail = ' + read.comment_detail
                    + ' where user_read.rid = "' + read.rid
                    )


    def delete_read(self,read):
        cur = self.conn.cursor()
        cur.execute('delete from read where(read.uid = "'+ read.uid + '" and read.aid = "' + read.aid + '")')

    def update_be_read(self, be_read):
        cur = self.conn.cursor()
        cur.execute('update be_read set '
                    + ' timestamp = ' + be_read.timestamp
                    + ', read_uid_list = ' + be_read.read_uid_list
                    + ', comment_num = ' + be_read.comment_num
                    + ', comment_uid_list = ' +be_read.comment_uid_list
                    + ', agree_num = ' + be_read.agree_num
                    + ', agree_uid_list = ' + be_read.agree_uid_list
                    + ', share_num = ' + be_read.share_num
                    + ', share_uid_list = ' + be_read.share_uid_list
                    + ' where brid = "' + be_read.brid
                    )

    def update_pop_rank_aid_list(self, pop_rank, new_aid_list):
        cur = self.conn.cursor();
        query = 'update pop_rank set article_aid_list = "' + new_aid_list + '" where pid ="' + pop_rank.pid + '"'
        cur.execute(query)

    def delete_pop_rank_item(self, pop_rank):
        cur = self.conn.cursor();
        query = 'delete from pop_rank where pid="' + pop_rank.pid + '"'
        cur.execute(query)

    def get_popularity_rank(self, temporal_granularity, category):
        cur = self.conn.cursor()
        cur.execute('select * from popular_rank where (temporal_granularity="' + temporal_granularity+'" and category = "' + category + '")')
        rank = Popular_rank(cur.fetchall())
        return rank

    #ONLY USED FOR EXPERIMENTING
    def misc(self):
        cur = self.conn.cursor()
        a = np.random.randint(0, 255, (360, 480, 3))
        img = Image.fromarray(a.astype('uint8')).convert('RGB')
        img = img.tobytes("hex", "rgb")
        #img = str(img)
        #img = "BILDE"
        #query = 'insert into table articles_binary partition(category = "tech") values("id1", "2019-12-20 13:38:19.020", "text","' + str(img_str) + '", " video", " noe")'
        #cur.execute(query)
        #query = 'drop table articles_binary'
        #cur.execute(query)
        #query = 'Create table articles_binary(aid string, var_timestamp timestamp, title string, text string, image binary, video string) Partitioned by (category string)'
        query = 'select * from articles_binary'
        cur.execute(query)

        print(cur.fetchall())
        return


def pretty_print(input):
    for element in input:
        print(element)


#print("setting up connection " , config.host_name, config.port)
client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)
print(client.get_all_articles("technology"))
