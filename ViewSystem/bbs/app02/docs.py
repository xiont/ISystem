#ecoding:utf-8
from mongoengine import *
from bbs.settings import DB_NAME
connect(DB_NAME)

class Profile(EmbeddedDocument):
    gender = StringField()
    location = StringField()

class User(Document):
    username = StringField(required=True)
    website = URLField()
    tags = ListField(StringField(max_length=16))
    profile = EmbeddedDocumentField(Profile)

class Event_Mongo(Document):
    title = StringField(required = True,max_length=128,unique=True)
    time = DateTimeField()
    url = URLField()
    platform = StringField(max_length=128)
    content = StringField()

