import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 20,
         'likes': 7,},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 15,
         'likes': 5,},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 13,
         'likes': 5,} ]
    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 17,
         'likes': 17,},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 42,
         'likes': 39,},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 31,
         'likes': 15,} ]
    
    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 13,
         'likes': 2,},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 9,
         'likes': 3,} ]
    
    cats = {'Python': {'pages': python_pages, 'views': 5, 'likes': 4},
            'Django': {'pages': django_pages, 'views': 9, 'likes': 5},
            'Other Frameworks': {'pages': other_pages, 'views': 15, 'likes': 11} }

 # If you want to add more categories or pages,
 # add them to the dictionaries above.

 # The code below goes through the cats dictionary, then adds each category,
 # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=0, likes=0)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'], p['likes'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views, likes):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.likes = likes
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
