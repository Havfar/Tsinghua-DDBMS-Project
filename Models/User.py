class User:

    def __init__(self, id=None, uid=None, timestamp=None, name=None,
                 gender=None, email=None, phone=None, dept=None,
                 region=None, language=None, role=None, prefer_tags=None,
                 obtained_credits=None, input_string=None):
        if input_string == None:
            self.id = id
            self.uid = uid
            self.timestamp = timestamp
            self.name = name
            self.gender = gender
            self.email = email
            self.phone = phone
            self.dept = dept
            self.language = language
            self.region = region
            self.role = role
            self.prefer_tags = prefer_tags
            self.obtained_credits = obtained_credits
        else:

            input_string = input_string.replace("(", "")
            input_string = input_string.replace(")", "")
            input_string = input_string.split(', ')
            self.id = input_string[2].replace("'", "")
            self.timestamp = input_string[1].replace("'", "")
            self.uid = input_string[0].replace("'", "")
            self.name = input_string[3].replace("'", "")
            self.gender = input_string[4].replace("'", "")
            self.email = input_string[5].replace("'", "")
            self.phone = input_string[6].replace("'", "")
            self.dept = input_string[7].replace("'", "")
            self.language = input_string[8].replace("'", "")
            self.region = input_string[9].replace("'", "")
            self.role = input_string[10].replace("'", "")
            self.prefer_tags = input_string[11].replace("'", "")
            self.obtained_credits = input_string[12].replace("'", "")

    def __str__(self):
        return  "(" + \
           "\"" + self.id + "\", " + \
           "\"" + self.uid + "\", " + \
           "\"" + self.timestamp + "\", " + \
           "\"" + self.name + "\", " + \
           "\"" + self.gender + "\", " + \
           "\"" + self.email + "\", " + \
           "\"" + self.phone + "\", " + \
           "\"" + self.dept + "\", " + \
           "\"" + self.language + "\", " + \
           "\"" + self.region+ "\", " + \
           "\"" + self.role+ "\", " + \
           "\"" + self.prefer_tags+ "\", " + \
           "\"" + self.obtained_credits + "\")"
