class Popular_rank:

    # temporalGranularity= “daily”, “weekly”, or “monthly”
    def __init__(self, id, timestamp, temporal_granularity, article_aid_list):
        self.id = id
        self.timestamp = timestamp
        self.temporal_granularity = temporal_granularity
        self.article_aid_list = article_aid_list

    def __str__(self):
        return "(" + \
               "\"" + self.id + "\", " + \
               "\"" + self.timestamp + "\", " + \
               "\"" + self.temporal_granularity + "\", " + \
               "\"" + self.article_aid_list + "\")"
