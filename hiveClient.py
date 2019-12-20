import datetime
from typing import List

from pyhive import hive

from Models.Article import Article
from Models.Be_Read import Be_read
from Models.Popular_rank import Popular_rank
from Models.Read import Read
from Models.User import User
import uuid
from utils import gen_an_read, gen_an_user, gen_an_article
import numpy
import config

# TODO: Is it possible to bulk load in hive?( aka use LIMIT = X and Offset = X*Y)
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
        cur.execute('insert into table popular_rank values' + pop_rank.__str__())

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

    #NOT WORKING
    #TODO: Can you update in hive?
    def update_read(self, read):
        cur = self.conn.cursor()
        print(read.id, read.uid, read.aid)
        cur.execute('update user_read set'
                    + ' id = ' + read.aid
                    + ' uid = ' + read.uid
                    + ' uid = ' + read.uid
                    + ' aid = ' + read.aid
                    + ' var_timestamp = ' + read.timestamp
                    + ' read_or_not = ' + read.read_or_not
                    + ' read_time_length = ' + read.read_time_length
                    + ' read_sequence = ' +read.read_sequence
                    + ' agree_or_not = ' + read.agree_or_not
                    + ' comment_or_not = ' + read.comment_or_not
                    + ' share_or_not = ' + read.share_or_not
                    + ' comment_detail = ' + read.comment_detail
                    + ' where (user_read.uid = "' + read.uid
                    + '" and user_read.aid = "' + read.aid + '")'
                    )

    #NOT WORKING
    #TODO: Can you delete row in hive?
    def delete_read(self,read):
        cur = self.conn.cursor()
        cur.execute('delete from user_read where(user_read.uid = "'+ read.uid + '" and user_read.aid = "' + read.aid + '")')

    #NOT WORKING
    #TODO: Can you update in hive?
    def update_be_read(self, be_read):
        cur = self.conn.cursor()
        cur.execute('update be_read set '
                    + ' timestamp = ' + be_read.timestamp
                    + ' read_uid_list = ' + be_read.read_uid_list
                    + ' comment_num = ' + be_read.comment_num
                    + ' comment_uid_list = ' +be_read.comment_uid_list
                    + ' agree_num = ' + be_read.agree_num
                    + ' agree_uid_list = ' + be_read.agree_uid_list
                    + ' share_num = ' + be_read.share_num
                    + ' share_uid_list = ' + be_read.share_uid_list
                    + ' where (user_read.uid = "' + be_read.uid
                    + '" and user_read.aid = "' + be_read.aid + '")'
                    )

    #TODO: create function
    def update_pop_rank(self, pop_rank):
        pass;

    def get_popularity_rank(self, temporal_granularity, category):
        cur = self.conn.cursor()
        cur.execute('select * from popular_rank where tempporal_granularity="' + temporal_granularity+'"')
        rank = Popular_rank(cur.fetchall())
        return rank

    #ONLY USED FOR EXPERIMENTING
    def misc(self):
        cur = self.conn.cursor()
        cur.execute('update test_tab set name="bob" where name = "name"')
        cur.execute('select * from test_tab')
        print(cur.fetchall())
        return


def pretty_print(input):
    for element in input:
        print(element)


print("setting up connection " , config.host_name, config.port)
client = HiveClient(host_name=config.host_name, password=config.password, user=config.user, portNumber=config.port)
#print(client.get_users_by_region(region="Beijing")[0])
client.misc()
#client.create_article(gen_an_article(0))
#print(client.get_user_by_uid(uid="u636a1cda-01ac-467c-b8b9-1bb69f26838c", region="Hong Kong"))
#print(gen_an_user(1).__str__())
# Testing objects
#article1 = Article(input_string="('t0', 't0', '1506000000002', 'title2', 'science', 'abstract of article 2', 'tags30', 'author616', 'zh', 'text_a2.txt', 'image_a2_0.jpg,', '')")
#read = Read(input_string="('rt2', 'u69', 't0', '1506332297000', '1', '68', '0', '0', '0', '0', 'comments to this article: (u69,t0)'),")
#new_read = Read(input_string="('rt2', 'u69', 't0', '1506332297000', '1', '69', '0', '0', '0', '0', 'comments to this article: (u69,t0)'),")
#be_read1 = Be_read(id="0", aid='t0', timestamp=datetime.datetime.now().__str__(), read_uid_list="u69", comment_num="0", comment_uid_list="u69", agree_num="1", agree_uid_list="u69", share_num="1", share_uid_list="u69" )
#pop_rank = Popular_rank(id = '0', timestamp=datetime.datetime.now().__str__(), temporal_granularity="daily", article_aid_list='t0')

# client.misc()
#print(client.get_read('t0','u69'))
#client.create_read(read)
#print(client.get_read('t0','u69'))
#print(client.create_read(read))
#print(client.describe_table('be_read'))
#client.create_user(user)
#print(client.get_all_tables())
# print(client.describe_table(
#     "user_table"
# ))
#print(client.get_table_by_name('user_table'))