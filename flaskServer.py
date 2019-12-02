from flask import Flask
from flask import request
from flask import send_from_directory
from flask import render_template

import random
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

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

@app.route('/formpost', methods = ['POST'])
def formpost():
    if request.method == 'POST':
        
        newFormListener = formListener()
        readFormResponse = newFormListener.readForm(request.form)
        return readFormResponse

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


class formListener():

    __get_table_by_tablename = ""
    __get_user_read = ""
    __get_all_tables = ""
    __get_all_databases = ""
    __describe_table = ""
    __create_user = ""
    __create_article = ""
    __read_article = ""
    __get_user_read_table_by_user = ""
    __get_user_read_table_by_read = ""
    __get_article_by_id = ""
    __get_user_by_id = ""
    __get_readcount_by_aid = ""
    __get_readcount_by_aid_and_uid = ""
    __update_read = ""
    __get_popularity_rank = ""

    def __init__(self):
        self.__get_table_by_tablename = "get_table_by_tablename"
        self.__get_user_read = "get_user_read"
        self.__get_all_tables = "get_all_tables"
        self.__get_all_databases = "get_all_databases"
        self.__describe_table = "describe_table"
        self.__create_user = "create_user"
        self.__create_article = "create_article"
        self.__read_article = "read_article"
        self.__get_user_read_table_by_user = "get_user_read_table_by_user"
        self.__get_user_read_table_by_read = "get_user_read_table_by_read"
        self.__get_article_by_id = "get_article_by_id"
        self.__get_user_by_id = "get_user_by_id"
        self.__get_readcount_by_aid = "get_readcount_by_aid"
        self.__get_readcount_by_aid_and_uid = "get_readcount_by_aid_and_uid"
        self.__update_read = "update_read"
        self.__get_popularity_rank = "get_popularity_rank"





    def readForm(self, formData):
        print("formListener received: ", formData)
        print("Console received post from form")
        try:
            keyValuePairsDict = formData.to_dict()
        except:
            return "Error, from readForm. Posted data was not a form."

        keylist = []
        for key in keyValuePairsDict:
            keylist.append(key)
            print("key: " + key + " value: " + keyValuePairsDict.get(str(key)))

        # Figure out which query is to be made
        queryType = str(keyValuePairsDict.get("query"))

        # call wanted query to pyhive here

        if(queryType == self.__get_table_by_tablename):
            #TODO
            tableName = keyValuePairsDict.get("tableName")
            return queryType

        elif(queryType == self.__get_user_read):
            #TODO
            user_id = keyValuePairsDict.get("uid")
            return queryType

        elif(queryType == self.__get_all_tables):
            #TODO
            return queryType

        elif(queryType == self.__get_all_databases):
            #TODO
            return queryType

        elif(queryType == self.__describe_table):
            #TODO
            tableName = keyValuePairsDict.get("tableName")
            return queryType

        elif(queryType == self.__create_user):
            #TODO
            newUserName = keyValuePairsDict.get("name")
            return queryType

        elif(queryType == self.__create_article):
            #TODO
            return queryType

        elif(queryType == self.__read_article):
            #TODO
            return queryType

        elif(queryType == self.__get_user_read_table_by_user):
            #TODO
            user_id = keyValuePairsDict.get("uid")
            return queryType

        elif(queryType == self.__get_user_read_table_by_read):
            #TODO
            return queryType

        elif(queryType == self.__get_article_by_id):
            #TODO
            article_id = keyValuePairsDict.get("aid")
            return queryType

        elif(queryType == self.__get_user_by_id):
            #TODO
            user_id = keyValuePairsDict.get("uid")
            return queryType

        elif(queryType == self.__get_readcount_by_aid):
            #TODO
            article_id = keyValuePairsDict.get("aid")
            return queryType

        elif(queryType == self.__get_readcount_by_aid_and_uid):
            #TODO
            article_id = keyValuePairsDict.get("aid")
            user_id = keyValuePairsDict.get("uid")
            return queryType

        elif(queryType == self.__update_read):
            #TODO
            article_id = keyValuePairsDict.get("aid")
            return queryType

        elif(queryType == self.__get_popularity_rank):
            #TODO
            article_id = keyValuePairsDict.get("aid")
            return queryType

class queryBuilder():

    dataBaseName = None
    tableName = None
    articleTable = None
    userTable = None
    readTable = None
    beReadTable = None
    popularRankTable = None

    def __init__(self, dataBaseName: None, tableName, articleTable, userTable, readTable, beReadTable, popularRankTable):
        self.dataBaseName = dataBaseName
        self.tableName = tableName
        self.articleTable = articleTable
        self.userTable = userTable
        self.readTable = readTable
        self.beReadTable = beReadTable
        self.popularRankTable = popularRankTable

    def selectArticleFromTable(self, articleId, tableName: None, orderBy: None, limit: None):

        query = "SELECT article "+ str(articleId) + " FROM " + self.articleTable

        if orderBy != None:
            query = query + " ORDER BY " + str(orderBy)
        
        if limit != None:
            query = query + " LIMIT " + str(limit)
        return query

    def selectUserFromTable(self, userId: None, whereParamater: None, whereClause: None, whereCondition: None, tableName: None, orderBy: None, limit: None):

        query = "SELECT user FROM " + self.userTable

        # Example usage:
        # SELECT user WHERE >whereParamater< >whereClause< >whereCondition<
        # Example values:
        # SELECT user WHERE userId == 23        here userID = whereParameter, whereClause is ==, whereCondition = 23

        if (whereParamater != None) and (whereCondition != None) and (whereClause != None) and (userId == None):
            query = query + " WHERE " + str(whereParamater) + " " + str(whereClause) + " " + str(whereCondition)

        if orderBy != None:
            query = query + " ORDER BY " + str(orderBy)
        
        if limit != None:
            query = query + " LIMIT " + str(limit)
        return query

if __name__ == '__main__':
    querybuilder = queryBuilder("ok", "tableNameTest", "articleTableTest", "userTableTest", "readTableTest", "beReadTableTest", "popularRankTableTest")
    print(querybuilder.selectUserFromTable(2, None, "region", None, None, "region", 5))
    print(querybuilder.selectUserFromTable(None, "userID", ">", 23, None, None, None))
    app.run()