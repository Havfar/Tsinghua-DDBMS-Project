import datetime
import uuid
from random import random
import numpy as np
from PIL import Image
import os
import loremipsum
import names
from coolname import generate_slug
from Models.Article import Article
from Models.Read import Read
from Models.User import User
import base64
from io import BytesIO

USERS_NUM = 10000
ARTICLES_NUM = 10000
READS_NUM = 1000000
uid_region = {}
aid_lang = {}

# Used to create unique ids to Articles/ Users / Reads/ be_reads / pop_rank
def create_id(prefix):
    """Creates a new unique id"""
    return prefix + str(uuid.uuid4())


def get_current_timestamp():
    """Gets the current timestamp on Hive timestamp format"""
    return str(datetime.datetime.now())[:-3]


def get_last_day_timestamp():
    """Gets yesterdays timestamp on Hive timestamp format"""
    today = datetime.datetime.now()
    last_day = today - datetime.timedelta(days=1)
    return str(last_day)[:-3]


def get_last_week_timestamp():
    """Gets last week timestamp on Hive timestamp format"""
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    return str(last_week)[:-3]


def get_last_month_timestamp():
    """Gets last month timestamp on Hive timestamp format"""
    today = datetime.datetime.now()
    last_month = today - datetime.timedelta(days=30)
    return str(last_month)[:-3]


def gen_an_article(i):
    """Generate a new article"""
    article = {}
    timestamp = get_current_timestamp()
    aid = create_id('a')
    title = generate_slug()
    category = "Science" if random() > 0.55 else "Technology"
    abstract = "abstract of article %d" % i
    article_tags = "tags%d" % int(random() * 50)
    author  = names.get_full_name()
    language = "en" if random() > 0.5 else "zh"
    # create text
    article["text"] = "text_a"+str(i)+'.txt'
    path = './articles/article'+str(i)
    if not os.path.exists(path):
        os.makedirs(path)
    num = int(random()*1000)
    text = loremipsum.generator.Generator().generate_paragraph(start_with_lorem=True)[2].replace("'",'').replace('b','')
    f = open(path+"/text_a"+str(i)+'.txt','w+',encoding="utf8")
    f.write("".join(text))
    f.close()

    # create images
    image_num = 1
    image_str = ""
    for j in range(image_num):
        image_str+= 'image_a'+str(i)+'_'+str(j)+'.jpg,'
    article["image"] = image_str
    num_image = int(random()*5)+1
    for j in range(num_image):
        img = create_img_bin_string()

    aid_lang[aid] = language
    return Article(
        timestamp=timestamp,
        aid = aid,
        title = title,
        category = category,
        abstract  =abstract,
        article_tags = article_tags,
        author = author,
        text = str(text),
        language = language,
        image = str(img),
        video = ""
    )

def gen_an_user (i):
    """Generate a new user"""
    user = {}
    timestamp = get_current_timestamp()
    uid = create_id("u")
    gender = "male" if random() > 0.33 else "female"
    name = names.get_full_name(gender=gender)
    email = "email%d" % i
    phone = "phone%d" % i
    dept  = "dept%d" % int(random() * 20)
    age = int(random()*100)
    language = "en" if random() > 0.8 else "zh"
    region = "Beijing" if random() > 0.4 else "HongKong"
    role = "role%d" % int(random() * 3)
    prefer_tags = "tags%d" % int(random() * 50)
    obtained_credits = str(int(random() * 100))

    uid_region[uid] = region
    return User(timestamp=timestamp,
                uid=uid, name=name,
                gender=gender, email=email,
                phone=phone, dept=dept,
                age=age, language=language,
                region=region, role=role,
                prefer_tags=prefer_tags,
                obtained_credits=obtained_credits)


p = {}
p["Beijing" + "en"] = [0.6, 0.2, 0.2, 0.1]
p["Beijing" + "zh"] = [1, 0.3, 0.3, 0.2]
p["Hong Kong" + "en"] = [1, 0.3, 0.3, 0.2]
p["Hong Kong" + "zh"] = [0.8, 0.2, 0.2, 0.1]


def gen_an_read(i, uid, aid):
    """Generate a new read based on user and article"""
    timestamp = get_current_timestamp()
    rid = create_id("r")
    uid = uid
    aid= aid
    region = uid_region[uid]
    lang = aid_lang[aid]
    ps = p[region + lang]

    if (random() > ps[0]):
        return gen_an_read(i)
    else:
        read_or_not = True
        read_time_length = str(int(random() * 100))
        read_sequence = str(int(random() * 4))
        agree_or_not = True if random() < ps[1] else False
        comment_or_not = True if random() < ps[2] else False
        share_or_not = True if random() < ps[3] else False
        comment_detail = "comments to this article: (" + uid + "," + aid + ")"
    return Read(rid=rid, timestamp=timestamp, uid=uid, aid= aid, read_or_not=read_or_not, read_time_length=read_time_length, read_sequence=read_sequence, agree_or_not=agree_or_not,
                comment_or_not= comment_or_not, share_or_not=share_or_not, comment_detail=comment_detail)


def create_img_bin_string():
    """creates a image and save it as a base64 binary"""
    buffered = BytesIO()
    a = np.random.randint(0, 255, (360, 480, 3))
    img = Image.fromarray(a.astype('uint8')).convert('RGB')
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return str(img_str)[2:-1]


def bin_to_img(bin_str):
    """converts a binary string to image"""
    img = Image.frombytes(data=bin_str)
    return img
