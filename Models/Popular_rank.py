class Popular_rank:

    # temporalGranularity= “daily”, “weekly”, or “monthly”
    def __init__(self, pid = None, timestamp = None, temporal_granularity = None, article_aid_list = None, input_string = None, category = None):
        if input_string == None:
            self.pid = id
            self.timestamp = timestamp
            self.temporal_granularity = temporal_granularity
            self.article_aid_list = article_aid_list
            self.category = category
        else:
            input_string = input_string.replace("(", "")
            input_string = input_string.replace(")", "")
            input_string = input_string.split(', ')
            self.id = input_string[0].replace("'", "")
            self.timestamp = input_string[1].replace("'", "")
            self.temporal_granularity = input_string[2].replace("'", "")
            self.article_aid_list = input_string[3].replace("'", "")
            self.category = input_string[4].replace("'", "")

    def __str__(self):
        return "(" + \
               "\"" + self.pid + "\", " + \
               "\"" + self.timestamp + "\", " + \
               "\"" + self.temporal_granularity + "\", " + \
               "\"" + self.article_aid_list + "\")"
