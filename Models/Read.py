
class Read:

    def __init__(self, id, aid,  uid, timestamp, read_or_not = 0,
                 read_time_length = 0, read_sequence=0, agree_or_not=0,
                 commentOrNot=None, share_or_not=None, comment_detail=None):
        self.id = id
        self.aid = aid
        self.uid = uid
        self.timestamp = timestamp
        self.read_or_not = read_or_not
        self.read_time_length = read_time_length
        self.read_sequence = read_sequence
        self.agree_or_not = agree_or_not
        self.commentOrNot = commentOrNot
        self.share_or_not = share_or_not
        self.comment_detail = comment_detail

    def __str__(self):
        return  "(" + \
           "\"" + self.id + "\", " + \
           "\"" + self.aid + "\", " + \
           "\"" + self.uid + "\", " + \
           "\"" + self.timestamp + "\", " + \
           "\"" + str(self.read_or_not) + "\", " + \
           "\"" + str(self.read_time_length) + "\", " + \
           "\"" + str(self.read_sequence )+ "\", " + \
           "\"" + str(self.agree_or_not) + "\", " + \
           "\"" + str(self.commentOrNot) + "\", " + \
           "\"" + str(self.share_or_not) + "\", " + \
           "\"" + str(self.comment_detail) + "\")"
