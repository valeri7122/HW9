from models import Quote, Author
import connect
import json


with open('data/authors.json', "rb") as fh:
    authors = json.load(fh)
    for a in authors:
        author = Author(fullname=a['fullname'], born_date=a['born_date'],
         born_location=a['born_location'], description=a['description'])
        author.save()

with open('data/quotes.json', "rb") as fh:
    quotes = json.load(fh)
    for q in quotes:
        for ao in Author.objects():
            if ao.fullname == q['author']:
               author = ao
               break 
        quote = Quote(tags=q['tags'], author=author, quote=q['quote'])
        quote.save()
