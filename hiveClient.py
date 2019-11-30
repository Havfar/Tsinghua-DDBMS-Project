import datetime

from pyhive import hive

from Models.Article import Article
from Models.Read import Read
from Models.User import User
from utils import gen_an_read
import numpy
import config


class HiveClient:
    def __init__(self, host_name, portNumber, user, password ):
        self.conn = hive.Connection(host=host_name, port=portNumber, username=user, password=password,
                                    auth='CUSTOM')

    def get_table_by_name(self, table_name, columns='*', order_by='asc'):
        cur = self.conn.cursor()
        try:
            cur.execute('select ' + columns + ' from ' + table_name)
            result = cur.fetchall()
        except:
            result = "None"
        return result

    def get_user_read(self):
        cur = self.conn.cursor()
        cur.execute('select * from user_read')
        result = cur.fetchall()
        return result

    def get_all_tables(self):
        cur = self.conn.cursor()
        cur.execute('show tables')
        result = cur.fetchall()
        return result

    def get_all_databases(self):
        cur = self.conn.cursor()
        cur.execute('show databases')
        result = cur.fetchall()
        return result

    def describe_table(self, table_name):
        cur = self.conn.cursor()
        try:
            print('describe ' + table_name)
            cur.execute('describe ' + table_name )
            result = cur.fetchall()
        except:
            result = "None"
        return result

    def create_user(self, user):
        cur = self.conn.cursor()
        cur.execute('insert into table user_table values' + user.__str__())

    def create_article(self, article):
        cur = self.conn.cursor()
        cur.execute('insert into table article_table values' + article.__str__())

    def read_article(self, read):
        cur = self.conn.cursor()
        cur.execute('insert into table user_read values' + read.__str__())
        cur.execute('select * from user_read')
        print(cur.fetchall())

    def get_user_read_table_by_user(self, user):
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

    def get_user_read_table_by_read(self, read):
        cur = self.conn.cursor()
        cur.execute('select  * '
                    'from (select aid, uid from user_read where id="' + read.id +'") r '
                    'left outer join (select uid, name from user_table) usr '
                    'on ( r.uid = usr.uid) '
                    'left outer join (select aid, title from article_table) artcl '
                    'on (r.aid = artcl.aid) '

                    )
        result = cur.fetchall()
        return result

    def get_article_by_id(self, aid):
        cur = self.conn.cursor()
        cur.execute('select * from article_table where aid=' + aid)
        return cur.fetchall()

    def get_user_by_uid(self, uid, region = None):
        cur = self.conn.cursor()
        cur.execute('select * from user_table where user_table.uid="'+uid + '"')
        return cur.fetchall()


    def get_read_count_by_aid(self, aid):
        pass

    def get_read_count_by_aid_and_uid(self, aid, uid):
        pass

    def update_read(self, aid, uid):
        pass

    def get_popularity_rank(self):
        cur = self.conn.cursor()
        cur.execute()

    def misc(self):
        cur = self.conn.cursor()
        cur.execute('alter table user_table change newid uid string ')
        cur.execute('describe user_table')
        return cur.fetchall()


def prettyPrint(input):
    for element in input:
        print(element)

