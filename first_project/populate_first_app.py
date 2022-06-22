import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')

import django 
django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Topic, Webpage, User
from faker import Faker

fakegen = Faker()

topics = ["Search", 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
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

		# create a new webpage entry
		webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)
		# print(webpg)

		# create a fake accesrecord for that webpage
		acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)
	

# populate users
def populate_user_data(N=5):
	for entry in range(N):
		fake_name = fakegen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakegen.email()

		# NEW Entry
		user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
	print("Populationg script!")
	# populate(4)
	populate_user_data(10)
	print("populating complete!")
