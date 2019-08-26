import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from catalog.models import Article
import csv


with open('1997_2008.csv', newline='') as csvfile:
	article_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in article_reader:
		date = row[0]
		title = row[1]
		text = row[2]
		author = row[3]
		title = title.replace('  ', ' ')
		text= text.replace('  ', ' ') 

		b = Article(title=title, summary=text, date_publication=date, author=author)
		b.save()
