
from pyhive import hive
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

    def create_user(self,):
        pass

    def create_article(self):
        pass

    def read_article(self, uid, aid):
        pass

    def get_article_by_id(self, aid):
        pass

    def get_user_by_id(self, uid, region = None):
        pass

    def get_read_count_by_aid(self, aid):
        pass

    def get_read_count_by_aid_and_uid(self, aid, uid):
        pass

    def update_read(self, aid, uid):
        pass

    def get_popularity_rank(self):
        pass





client = HiveClient(host_name=config.host_name, password=config.password, portNumber=config.port, user=config.user)
print(client.get_table_by_name('user_table'))
print(client.get_all_tables())
print(client.describe_table('user_table'))


