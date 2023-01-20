from mongoengine import *
from mongoengine.fields import *


class Author(Document):
    fullname = StringField(max_length=50, required=True)
    born_date = StringField()
    born_location = StringField(max_length=120)        
    description = StringField()

class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author, reverse_delete_rule=DENY)
    quote = StringField(required=True)     
    meta = {'allow_inheritance': True}