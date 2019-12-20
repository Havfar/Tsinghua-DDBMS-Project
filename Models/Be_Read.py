class Be_read:
    def __init__(self, brid= None, aid= None, timestamp= None,
                 read_uid_list= None, comment_num= None,
                 comment_uid_list= None, agree_num= None,
                 agree_uid_list= None, share_num= None,
                 share_uid_list= None, input_string = None):
        if input_string == None:
            self.brid = id
            self.aid = aid
            self.timestamp = timestamp
            self.read_uid_list = read_uid_list
            self.comment_num = comment_num
            self.comment_uid_list = comment_uid_list
            self.agree_num = agree_num
            self.agree_uid_list = agree_uid_list
            self.share_num = share_num
            self.share_uid_list = share_uid_list
        else:
            input_string = input_string.replace("(", "")
            input_string = input_string.replace(")", "")
            input_string = input_string.split(', ')
            self.brid = input_string[0].replace("'", "")
            self.aid = input_string[1].replace("'", "")
            self.timestamp = input_string[2].replace("'", "")
            self.read_uid_list = input_string[3].replace("'", "")
            self.comment_num = input_string[4].replace("'", "")
            self.comment_uid_list = input_string[5].replace("'", "")
            self.agree_num = input_string[6].replace("'", "")
            self.agree_uid_list = input_string[7].replace("'", "")
            self.share_num = input_string[8].replace("'", "")
            self.share_uid_list = input_string[9].replace("'", "")

    def __str__(self):
        return "(" + \
               "\"" + self.brid + "\", " + \
               "\"" + self.aid + "\", " + \
               "\"" + self.timestamp + "\", " + \
               "\"" + self.read_uid_list + "\", " + \
               "\"" + self.comment_num + "\", " + \
               "\"" + self.comment_uid_list + "\", " + \
               "\"" + self.agree_num + "\", " + \
               "\"" + self.agree_uid_list + "\", " + \
               "\"" + self.share_num + "\", " + \
               "\"" + self.share_uid_list + "\")"