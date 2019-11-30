
class Article:

    def __init__(self, id=None, aid = None, timestamp = None, title = None,
                 category = None, abstract = None, article_tags = None,
                 authors = None, language = None, text = None, image = None,
                 video = None, input_string = None):
        if input_string == None:
            self.id = id
            self.aid = aid
            self.timestamp = timestamp
            self.title = title
            self.category = category
            self.abstract = abstract
            self.article_tags = article_tags
            self.authors = authors
            self.language = language
            self.text = text
            self.image = image
            self.video = video
        else:
            input_string = input_string.replace("(","")
            input_string = input_string.replace(")","")
            input_string = input_string.split(', ')
            self.id = input_string[1].replace("'","")
            self.aid = input_string[0].replace("'","")
            self.timestamp = input_string[2].replace("'","")
            self.title = input_string[3].replace("'","")
            self.category = input_string[4].replace("'","")
            self.abstract = input_string[5].replace("'","")
            self.article_tags = input_string[6].replace("'","")
            self.authors = input_string[7].replace("'","")
            self.language = input_string[8].replace("'","")
            self.text = input_string[9].replace("'","")
            self.image = input_string[10].replace("'","")
            self.video = input_string[11].replace("'","")


    def __str__(self):
        return  "(" + \
           "\"" + self.id + "\", " + \
           "\"" + self.aid + "\", " + \
           "\"" + self.timestamp + "\", " + \
           "\"" + self.title + "\", " + \
           "\"" + self.category + "\", " + \
           "\"" + self.abstract + "\", " + \
           "\"" + self.article_tags + "\", " + \
           "\"" + self.authors + "\", " + \
           "\"" + self.language + "\", " + \
           "\"" + self.text+ "\", " + \
           "\"" + self.image+ "\", " + \
           "\"" + self.video + "\")"

# a = Article("id", "aid", "timestamp", "title",
#                  "category", "abstract", "article_tags",
#                  "authors", "language", "text", "image", "video")
