
class Article:

    def __init__(self, aid = None, timestamp = None, title = None,
                 category = None, abstract = None, article_tags = None,
                 author = None, language = None, text = None, image = None,
                 video = None, input_string = None):
        if input_string == None:
            self.aid = aid
            self.timestamp = timestamp
            self.title = title
            self.category = category
            self.abstract = abstract
            self.article_tags = article_tags
            self.author = author
            self.language = language
            self.text = text
            self.image = image
            self.video = video
        else:
            input_string = input_string.replace("[", "")
            input_string = input_string.replace("]", "")
            input_string = input_string.replace("(","")
            input_string = input_string.replace(")","")
            input_string = input_string.split(', ')

            self.aid = input_string[0].replace("'","")
            self.timestamp = input_string[1].replace("'","")
            self.title = input_string[2].replace("'","")
            self.abstract = input_string[3].replace("'","")
            self.article_tags = input_string[4].replace("'","")
            self.author = input_string[5].replace("'","")
            self.language = input_string[6].replace("'","")
            self.text = input_string[7].replace("'","")
            self.image = input_string[8].replace("'","")
            self.video = input_string[9].replace("'","")
            self.category = input_string[10].replace("'","")


    def __str__(self):
        return  "(" + \
           "\"" + self.aid + "\", " + \
           "\"" + str(self.timestamp) + "\", " + \
           "\"" + self.title + "\", " + \
           "\"" + self.abstract + "\", " + \
           "\"" + self.article_tags + "\", " + \
           "\"" + self.author + "\", " + \
           "\"" + self.language + "\", " + \
           "\"" + self.text+ "\", " + \
           "\"" + self.image+ "\", " + \
           "\"" + str(self.video) + "\")"

# a = Article("id", "aid", "timestamp", "title",
#                  "category", "abstract", "article_tags",
#                  "authors", "language", "text", "image", "video")
