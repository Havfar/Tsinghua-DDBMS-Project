
class Read:

    def __init__(self, rid = None, aid = None,  uid = None, timestamp=None, read_or_not = 0,
                 read_time_length = 0, read_sequence=0, agree_or_not=0,
                 comment_or_not=None, share_or_not=None, comment_detail=None, input_string = None):
        if input_string == None:
            self.rid = rid
            self.aid = aid
            self.uid = uid
            self.timestamp = timestamp
            self.read_or_not = read_or_not
            self.read_time_length = read_time_length
            self.read_sequence = read_sequence
            self.agree_or_not = agree_or_not
            self.comment_or_not = comment_or_not
            self.share_or_not = share_or_not
            self.comment_detail = comment_detail
        else:
            input_string = input_string.replace("(", "")
            input_string = input_string.replace(")", "")
            input_string = input_string.split(', ')
            self.rid = input_string[0].replace("'", "")
            self.uid = input_string[1].replace("'", "")
            self.aid = input_string[2].replace("'", "")
            self.timestamp = input_string[3].replace("'", "")
            self.read_or_not = input_string[4].replace("'", "")
            self.read_time_length = input_string[5].replace("'", "")
            self.read_sequence = input_string[6].replace("'", "")
            self.agree_or_not = input_string[7].replace("'", "")
            self.comment_or_not = input_string[8].replace("'", "")
            self.share_or_not = input_string[9].replace("'", "")
            self.comment_detail = input_string[10].replace("'", "")

    def __str__(self):
        return  "(" + \
            "\"" + self.rid + "\", " + \
            "\"" + self.aid + "\", " + \
            "\"" + self.timestamp + "\", " + \
            "\"" + str(self.read_or_not) + "\", " + \
            "\"" + str(self.read_time_length) + "\", " + \
            "\"" + str(self.read_sequence )+ "\", " + \
            "\"" + str(self.agree_or_not) + "\", " + \
            "\"" + str(self.comment_or_not) + "\", " + \
            "\"" + str(self.share_or_not) + "\", " + \
            "\"" + str(self.comment_detail) + "\")"
