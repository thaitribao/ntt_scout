import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','scout_site.settings')
import django
django.setup()
from team_management.models import Team, Member, Comment

def add_team(team_name,slogan):
	team = Team.objects.get_or_create(team_name=team_name)[0]
	team.team_name = team_name
	team.slogan = slogan
	team.save()
	return team

def add_member(username,password, first_name, last_name, email, birthday, team, grade):
	user = User.objects.get_or_create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
	member = Member.objects.get_or_create(user = user, birthday = birthday, team = team, grade = grade)
	return member

def populate():

	DaiHung_team = add_team(team_name='Dai Hung', slogan = 'Cuong Trang')
	BachMa_team = add_team(team_name='Bach Ma', slogan = 'Khoe Manh')

	for team in Team.objects.all():
		print("- A team was created")

if __name__=='__main__':
	print("Starting Team Management population script..")
	populate()