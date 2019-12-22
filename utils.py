import datetime
import json
import uuid
from random import random
import numpy as np
from PIL import Image
from shutil import copyfile
import os
import loremipsum

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


def convert_img_to_string():
    pass

def convert_string_to_img():
    pass

# science:45%   technology:55%
# en:50%    zh:50%
# 50 tags
# 2000 authors
def gen_an_article (i):
    article = {}
    timestamp = get_current_timestamp()
    aid = create_id('a')
    title = "title%d" % i
    category = "science" if random() > 0.55 else "technology"
    abstract = "abstract of article %d" % i
    article_tags = "tags%d" % int(random() * 50)
    author  = "author%d" % int(random() * 2000)
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
    image_num = 1#int(random()*5)+1
    image_str = ""
    for j in range(image_num):
        image_str+= 'image_a'+str(i)+'_'+str(j)+'.jpg,'
    article["image"] = image_str
    num_image = int(random()*5)+1
    for j in range(num_image):
        img = create_img_bin_string()


    # create video
    if random() < 0.05:
        #has one video
        video = "video_a"+str(i)+'_video.flv'
        if random()<0.5:
            copyfile('./video/video1.flv',path+"/video_a"+str(i)+'_video.flv')
        else:
            copyfile('./video/video2.flv',path+"/video_a"+str(i)+'_video.flv')
    else:
        video = ""

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


# Used to create unique ids to Articles/ Users / Reads/ be_reads / pop_rank
def create_id(prefix):
    return prefix + str(uuid.uuid4())


def get_current_timestamp():
    return str(datetime.datetime.now())[:-3]


def get_last_day_timestamp():
    today = datetime.datetime.now()
    last_day = today - datetime.timedelta(days=1)
    return str(last_day)[:-3]


def get_last_week_timestamp():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    return str(last_week)[:-3]


def get_last_month_timestamp():
    today = datetime.datetime.now()
    last_month = today - datetime.timedelta(days=30)
    return str(last_month)[:-3]


def gen_an_user (i):
    user = {}
    timestamp = get_current_timestamp()
    uid = create_id("u")
    name = "user%d" % i
    gender = "male" if random() > 0.33 else "female"
    email = "email%d" % i
    phone = "phone%d" % i
    dept  = "dept%d" % int(random() * 20)
    grade = "grade%d" % int(random() * 4 + 1)
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


def gen_an_read(i):

    timeBegin = get_current_timestamp()
    read = {}
    timestamp = get_current_timestamp()
    rid = create_id("r")
    uid = str(int(random() * USERS_NUM))
    aid= str(int(random() * ARTICLES_NUM))
    region = uid_region[uid]
    lang = aid_lang[aid]
    ps = p[region + lang]

    if (random() > ps[0]):
        # read["readOrNot"] = "0";
        return gen_an_read(i)
    else:
        read_or_not = True
        read_time_length = str(int(random() * 100))
        read_sequence = str(int(random() * 4))
        agree_or_not = True if random() < ps[1] else False
        comment_or_not = True if random() < ps[2] else False
        share_or_not = True if random() < ps[3] else False
        comment_detail = "comments to this article: (" + uid + "," + aid + ")"
    return Read(rid, timestamp=timestamp, uid=uid, aid= aid, read_or_not=read_or_not, read_time_length=read_time_length, read_sequence=read_sequence, agree_or_not=agree_or_not,
                comment_or_not= comment_or_not, share_or_not=share_or_not, comment_detail=comment_detail)


def create_img_bin_string():
    buffered = BytesIO()
    a = np.random.randint(0, 255, (360, 480, 3))
    img = Image.fromarray(a.astype('uint8')).convert('RGB')
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

def bin_to_img(bin_str):
    img = Image.frombytes(data=bin_str)
    return img

get_last_weeks_timestamp()

