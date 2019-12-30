
from typing import List
from pyhive import hive
from Models.Article import Article
from Models.Be_Read import Be_read
from Models.Read import Read
from Models.User import User
import uuid
import config
import utils
class HiveClient:
    def __init__(self, host_name, portNumber, user, password ):
        self.conn = hive.Connection(host=host_name, port=portNumber, username=user, password=password,
                                    auth='CUSTOM')

    def get_table_by_name(self, table_name, columns='*', order_by='asc', page_size=None, page_number = None):
        """Get the content of table by the name of table, only used locally

            Parameters
            ----------
            table_name : str
                Name of table
            columns : str
                Select which columns to query
            order_by: str
                Order by asc or dsc
            page_size: int
                limit the query result
            page_number: int
                offsets the query result

            Returns
            -------
            result
                a list of table rows if the table exists, else None
        """
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

    def get_read_by_aid(self, aid, page_size=None, page_number = None):
        """Gets all reads by the article ID

            Parameters
            ----------
            aid : str
                A unique ID for an article
            page_size: int
                limit the query result
            page_number: int
                offsets the query result

            Returns
            -------
            reads
                a list of table Read items for the article
            """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('select * from read where aid="' + aid + '"')
        reads:List[Read] = []
        for read in cur.fetchall():
            read = Read(
                rid=read[0],
                aid=read[1],
                timestamp=read[2],
                read_or_not=read[3],
                read_time_length=read[4],
                read_sequence=read[5],
                agree_or_not=read[6],
                comment_or_not=read[7],
                share_or_not=read[8],
                comment_detail=read[9],
                uid=read[10],
            )
            reads.append(read)
        return reads

    def get_read_by_uid(self, uid, page_size=None, page_number = None):
        """Gets all reads by a specific user by its user ID

           Parameters
           ----------
           udi : str
               A unique ID for a user
           page_size: int
               limit the query result
           page_number: int
               offsets the query result

           Returns
           -------
           reads
               a list of table Read items for the user
           """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('select * from read where uid="' + uid + '"')
        reads:List[Read] = []
        for read in cur.fetchall():
            read = Read(
                rid=read[0],
                aid=read[1],
                timestamp=str(read[2]),
                read_or_not=read[3],
                read_time_length=read[4],
                read_sequence=read[5],
                agree_or_not=read[6],
                comment_or_not=read[7],
                share_or_not=read[8],
                comment_detail=read[9],
                uid=read[10],
            )
            reads.append(read)
        return reads
    
    def get_all_users(self, region, page_size=None, page_number=None):
        """Gets all users in the user table by region

           Parameters
           ----------
           region : str
               Either HongKong or Beijing
           page_size: int
               limit the query result
           page_number: int
               offsets the query result

           Returns
           -------
           user_list
               a list of table Users items for the region
           """
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
        """Gets all articles by region

           Parameters
           ----------
           category : str
                Either Science or Technology
           page_size: int
               limit the query result
           page_number: int
               offsets the query result

           Returns
           -------
           article_list
               a list of table Articles by a specific category
           """
        cur = self.conn.cursor()
        query = 'select * from articles where category ="' + category + '"' 
        if page_size != None and page_number != None:
            query += ' limit ' + str(page_size) + ' offset ' + str(page_number*page_size)
        cur.execute(query)
        result = cur.fetchall()
        print("got from hive:" ,result)
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

    def get_all_tables(self):
        """Gets all table names in database

           Returns
           -------
           result
               a list of tables
           """
        cur = self.conn.cursor()
        cur.execute('show tables')
        result = cur.fetchall()
        return result

    # Used for local testing
    def get_all_databases(self):
        """Gets all database names in hive

             Returns
             -------
             result
                 a list of databases
             """
        cur = self.conn.cursor()
        cur.execute('show databases')
        result = cur.fetchall()
        return result

    # Used for local testing
    def describe_table(self, table_name):
        """Used for local testing, describes a table by table name
            Parameters
            ----------
            table_name : str
                Name of a table in the database
            Returns
            -------
            result
                a list of attributes
             """
        cur = self.conn.cursor()
        try:
            cur.execute('describe ' + table_name )
            result = cur.fetchall()
        except:
            result = "None"
        return result

    def create_user(self, user):
        """Creates a user

            Parameters
            ----------
            user : User
                The user object to insert into user table
             """
        cur = self.conn.cursor()
        cur.execute('insert into table users partition(region ="' + user.region + '") values' + user.__str__())

    def create_users(self, users, region):
        """Bulk creates a users

            Parameters
            ----------
            users : User[]
                A list of Users to be inserted to table
            region: str
                the region to partition them in (Either HongKong or Beijing)
             """
        cur = self.conn.cursor()
        query = 'insert into table users partition(region ="' + region + '") values'
        i = 1
        for user in users:
            query += '  ("' + user.uid +  '", "' + str(user.timestamp) + '", "' + user.name + '", "' + user.gender + '", "' + user.email + '", "' + user.phone + '", "' + user.dept + '", "' + user.language + '", "' + user.role + '", " ' + user.prefer_tags + '", ' + str(user.obtained_credits) + ', ' + str(user.age) + ')'
            if(i != len(users)):
                query += ', '
            i+=1
        cur.execute(query)


    def create_article(self, article):
        """Creates an Article

            Parameters
            ----------
            article : Article
                The Article object to insert into articles table
             """
        cur = self.conn.cursor()
        cur.execute(
            'insert into table articles partition(category ="' + article.category + '") values' + article.__str__())

    def create_articles(self, articles, category):
        """Bulk creates a articles

            Parameters
            ----------
            articles : Article[]
                A list of Article to be inserted to table
            category: str
                the category to partition them in (Either Science or Technology)
             """
        cur = self.conn.cursor()
        query = 'insert into table articles partition(category ="' + category + '") values'
        i = 1
        for a in articles:
            query += ' ("' + a.aid + '","' + a.timestamp+ '","' + a.title+ '","' + a.abstract+ '","' + a.article_tags+ '","' + a.author+ '","' + a.language+ '", "' + a.text+ '", "' + a.image+ '", "' + str(a.video) +'")'
            if (i != len(articles)):
                query += ', '
            i += 1
        cur.execute(query)
        self.create_be_reads(articles, category)

    def create_read(self, read):
        """Creates an Read

            Parameters
            ----------
            read : Read
                The Read object to insert into read table
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('insert into table read partition(uid="' + read.uid +'") values' + read.__str__())

    # Input: Be_read object
    def create_be_read(self, be_read):
        """Creates a be_read

            Parameters
            ----------
            be_read : Be_read
                The Be_read object to insert into be_read table
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('insert into table be_read partition(aid="'+ be_read.aid +'") values' + be_read.__str__())

    # Input: Be_read object
    def create_be_reads(self, articles, category):
        """Bulk creates a be_reads, created after a creation of an article

            Parameters
            ----------
            articles : Article[]
                A list of Articles to be inserted to table
            category: str
                the category to partition them in (Either Science or Technology)
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'insert into table be_read partition(category="'+ category +'") values'
        i = 1
        for a in articles:
            query += ' ("' + utils.create_id("br") + '","' + a.aid + '","' + str(utils.get_current_timestamp()) + '",' + str(0) + ',"",' + str(0) + ',"",' + str(0) + ', "", ' + str(0) + ', "")'
            if (i != len(articles)):
                query += ', '
            i += 1
        cur.execute(query)

    def create_popular_rank(self, pop_rank):
        """Creates an popular Rank

            Parameters
            ----------
            pop_rank : Popular_Rank
                The Article object to insert into articles table
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('insert into table popular_rank partition(category = "'+ pop_rank.category +'") values' + pop_rank.__str__())

    def get_read_table_by_uid(self, uid, page_size=None, page_number = None):
        """Gets the reads by user
            Parameters
            ----------
            uid : str
                User ID
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            read_list
                a list of Reads
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'select  * from read  where uid="' + uid + '"'

        if page_size != None and page_size != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string = element))
        return read_list


    def get_article_by_aid(self, aid, category = None):
        """Gets the article by aid
            Parameters
            ----------
            aid : str
                Article ID
            category: str
               category of article
            Returns
            -------
            article
                an Article object with the specific aid
             """
        cur = self.conn.cursor()
        if category == None:
            query = 'select * from articles where aid="' + aid + '"'
        else:
            query ='select * from articles where articles.aid="' + aid + '" and articles.category = "' + category + '")'
        cur.execute(query)
        result = cur.fetchall()[0]
        article = Article(
            aid=result[0],
            timestamp= str(result[1]),
            title=result[2],
            abstract=result[3],
            article_tags=result[4],
            author=result[5],
            language=result[6],
            text=result[7],
            image=result[8],
            video=result[9],
        )
        return article

    # Should provide region
    def get_user_by_uid(self, uid, region = None):
        """Gets the user by uid
            Parameters
            ----------
            uid : str
                User ID
            region: str
               region of the user
            Returns
            -------
            user
                a User object
             """
        if region == None:
            cur = self.conn.cursor()
            cur.execute('select * from users where users.uid="' + uid + '"')
        else:
            cur = self.conn.cursor()
            cur.execute('select * from users where (users.uid="' + uid + '" and users.region = "' + region + '")')
        result = cur.fetchall()[0]
        user = User(
            uid = result[0],
            timestamp= str(result[1]),
            name = result[2],
            gender = result[3],
            email=result[4],
            phone = result[5],
            dept=result[6],
            language=result[7],
            role=result[8],
            prefer_tags=result[9],
            obtained_credits=result[10],
            age=result[11],
            region=result[12]
        )
        return user

    def get_users_by_region(self, region, page_size=None, page_number = None):
        """Gets the all users in a region
            Parameters
            ----------
            region : str
                region of users
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            users
                all users in a region
             """
        cur = self.conn.cursor()
        query = 'select * from users where region="' + region + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        output = cur.fetchall()
        print(output.__len__())
        users = []
        for item in output:
            user = User(
                uid=item[0],
                timestamp=str(item[1]),
                name=item[2],
                gender=item[3],
                email=item[4],
                phone=item[5],
                dept=item[6],
                language=item[7],
                role=item[8],
                prefer_tags=item[9],
                obtained_credits=item[10],
                age=item[11],
                region=item[12]
            )
            users.append(user)
        return users

    def get_articles_by_category(self, category, page_size=None, page_number = None):
        """Gets the all users in a region
            Parameters
            ----------
            category : str
                category of users
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            articles
                all articles in a category
             """
        cur = self.conn.cursor()
        query = 'select * from articles where category="' + category + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        output = cur.fetchall()
        print(output.__len__())
        articles = []
        for item in output:
            a = Article(
                aid=item[0],
                timestamp= str(item[1]),
                title=item[2],
                abstract=item[3],
                article_tags=item[4],
                author=item[5],
                language=item[6],
                text=item[7],
                image=item[8],
                video=item[9],
            )
            articles.append(a)
        return articles

    # Returns a list of read objects whom have commented
    def get_article_reads_by_aid(self, aid, page_size=None, page_number = None):
        """Gets the article reads by aid
            Parameters
            ----------
            aid : str
                Article ID
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            read_list
                a list of reads of the article
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'select * from read where (read.aid = "' + aid + '" and read.comment_or_not = 1) order by var_timestamp desc'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string=str(element)))
        return read_list

    #Retruns the read from an user and an article
    def get_read(self, aid, uid, page_size=None, page_number = None):
        """Gets the article reads by aid
            Parameters
            ----------
            aid : str
                Article ID
            uid : str
                User ID
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            read
                a Read object to the the spesific user and article
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('select * from read where (read.aid ="' + aid + '" and read.uid = "'+ uid +'")')
        read = Read(input_string=str(cur.fetchall()))
        return read

    def get_be_read_by_aid(self, aid, page_size=None, page_number = None):
        """Gets the be_read by a spefic article id
            Parameters
            ----------
            aid : str
                Article ID
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            be_read
                A Be_read item

             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'select * from be_read where be_read.aid = "' + aid + '"'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        be_read = Be_read(input_string = str(cur.fetchall()))
        return be_read


    def get_read_count_by_aid(self, aid, page_size=None, page_number = None):
        """Gets all reads from a aid
            Parameters
            ----------
            aid : str
                Article ID
            page_size: int
               limit the query result
            page_number: int
               offsets the query result
            Returns
            -------
            read_list
                a list of reads where all have read the article
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'select * from read where (read.aid = "' + aid + '" and read.read_or_not = 1) order by var_timestamp desc'
        if page_size != None and page_number != None:
            query += " limit " + str(page_size) + " offset " + str(page_number * page_size)
        cur.execute(query)
        read_list: List[Read] = []
        for element in cur.fetchall():
            read_list.append(Read(input_string=str(element)))
        return read_list

    def update_read(self, read):
        """Updates a read item
            Parameters
            ----------
            read : Read
                Read object that will be updated
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('update read set'
                    + ' var_timestamp = ' + read.timestamp
                    + ', read_or_not = ' + read.read_or_not
                    + ', read_time_length = ' + read.read_time_length
                    + ', read_sequence = ' +read.read_sequence
                    + ', agree_or_not = ' + read.agree_or_not
                    + ', comment_or_not = ' + read.comment_or_not
                    + ', share_or_not = ' + read.share_or_not
                    + ', comment_detail = ' + read.comment_detail
                    + ' where read.rid = "' + read.rid
                    )

    def delete_read(self,read):
        """Delete a read
            Parameters
            ----------
            read : Read
                Read object to be removed
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        cur.execute('delete from read where(read.uid = "'+ read.uid + '" and read.aid = "' + read.aid + '")')

    def update_be_read(self, be_read):
        """Updates a be_read item
            Parameters
            ----------
            be_read : Be_read
                Be_read object that will be updated
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
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

    def delete_pop_rank_item(self, pop_rank):
        """Delete a pop_rank item
            Parameters
            ----------
            pop_rank : Popular_rank
                pop_rank object to be removed
             """
        cur = self.conn.cursor();
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        query = 'delete from pop_rank where pid="' + pop_rank.pid + '"'
        cur.execute(query)


    def get_pop_rank(self, time):
        """Gets all reads from a aid
            Parameters
            ----------
            time : str
                temporalGranularity= “daily”, “weekly”, or “monthly”
            Returns
            -------
            article_list
                a list of the top 5 articles
             """
        cur = self.conn.cursor()
        cur.execute('set hive.support.concurrency=true')
        cur.execute('set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager')
        if(time == "weekly"):
            query = 'select  * from ( select aid, read_num from be_read) br left outer join (select * from articles where var_timestamp >"' + utils.get_last_week_timestamp() + '") artcl on ( br.aid = artcl.aid) order by read_num desc limit 5'
        elif(time =="monthly"):
            query = 'select  * from ( select aid, read_num from be_read) br left outer join (select * from articles where var_timestamp >"' + utils.get_last_month_timestamp() + '") artcl on ( br.aid = artcl.aid) order by read_num desc limit 5'
        else:
            query = 'select  * from ( select aid, read_num from be_read) br left outer join (select * from articles where var_timestamp >"' + utils.get_last_day_timestamp() + '") artcl on ( br.aid = artcl.aid) order by read_num desc limit 5'

        cur.execute(query)

        result = cur.fetchall()
        article_list = []
        print(len(result))
        print(len(result[0]))
        for item in result:
            a = Article(
                aid=item[2],
                timestamp=str(item[3]),
                title=item[4],
                abstract=item[5],
                article_tags=item[6],
                author=item[7],
                language=item[8],
                text=item[9],
                image=item[10],
                video=item[11],
            )
            article_list.append(a)
        return article_list



