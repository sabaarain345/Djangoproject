import os
from socket import if_nameindex
from unicodedata import name

from pip import main
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

## Here we have FAKE POP SCRIPT
import random
from second_app.models import Topic, Webpage, AccessRecord, User
from faker import Faker

fakegen = Faker()
topics = ['Social', 'Django', 'Python', 'Networking', 'Webpages']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):

    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

        # Create fake DATA for User models
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # # Create Fake Record
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]



if __name__ == '__main__':
    print("Population Scripts")
    populate(20)
    print("Populating Complete")