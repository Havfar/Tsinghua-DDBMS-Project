class Be_read:
    def __init__(self, id, uid, aid, timestamp,
                 read_uid_list, comment_num,
                 comment_uid_list, agree_num,
                 agree_uid_list, share_num,
                 share_uid_list):
        self.id = id
        self.uid = uid
        self.aid = aid
        self.timestamp = timestamp
        self.read_uid_list = read_uid_list
        self.comment_num = comment_num
        self.comment_uid_list = comment_uid_list
        self.agree_num = agree_num
        self.agree_uid_list = agree_uid_list
        self.share_num = share_num
        self.share_uid_list = share_uid_list

    def __str__(self):
        return "(" + \
               "\"" + self.id + "\", " + \
               "\"" + self.uid + "\", " + \
               "\"" + self.aid + "\", " + \
               "\"" + self.timestamp + "\", " + \
               "\"" + self.read_uid_list + "\", " + \
               "\"" + self.comment_num + "\", " + \
               "\"" + self.comment_uid_list + "\", " + \
               "\"" + self.agree_num + "\", " + \
               "\"" + self.agree_uid_list + "\", " + \
               "\"" + self.share_num + "\", " + \
               "\"" + self.share_uid_list + "\")"