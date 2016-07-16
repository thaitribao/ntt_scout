from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Member, Comment
from .forms import CommentForm, UserForm, MemberForm, TeamForm
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from scout_info.models import Scout_Profile

# Create your views here.

#Need a url, need to rewrite homepage/post-register/login logic...
def index(request):
	if request.user.is_authenticated(): 
		team_list = Team.objects.all()
		return render(request,'team_management/index.html',{'team_list':team_list})
	else: 
		return render(request,'team_management/homepage.html',{})

@login_required
def team(request,team_slug):
	context_dict = {}
	try:
		team = Team.objects.get(slug=team_slug)
		context_dict['team_name'] = team.team_name
		members = Member.objects.filter(team=team)
		context_dict['members'] = members
		context_dict['team']=team
		context_dict['team_slug']=team_slug
	except Team.DoesNotExist:
		pass
	return render(request,'team_management/team.html', context_dict)

@login_required
def member(request,member_id):
	context_dict = {}
	try: 
		member = Member.objects.get(pk=member_id)
		context_dict['member']=member
		context_dict['member_name'] = member.user.get_full_name
		comments = Comment.objects.filter(member=member)
		context_dict['comments'] = comments
		context_dict['member_id'] = member.id
		try:
			profile = Scout_Profile.objects.get(member=member)
			context_dict['profile']=profile
		except Scout_Profile.DoesNotExist:
			pass
	except Member.DoesNotExist:
		pass
	return render(request,'team_management/member.html', context_dict)

@login_required
def add_comment(request, member_id):
	context_dict = {}
	try: 
		member = Member.objects.get(pk=member_id)
	except Member.DoesNotExist:
		member = None
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.member = member
			comment.date = timezone.datetime.now()
			comment.author = request.user
			comment.save()
			return redirect('member', member_id=member_id)
		else:
			print(form.errors)
	else: 
		form = CommentForm()
	return render(request,'team_management/add_comment.html', {'form':form,'member':member,'member_id':member_id})

def register(request):
	registered = False
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		member_form = MemberForm(data=request.POST)

		if user_form.is_valid() and member_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			member = member_form.save(commit=False)
			member.user = user
			member.save()
			registered = True
		else: 
			print(user_form.errors, member_form.errors)
	else:
		user_form = UserForm()
		member_form = MemberForm()
	return render(request, 'team_management/register.html',{'user_form':user_form,'member_form':member_form,'registered':registered})

@login_required
def add_team(request):
	if request.method == "POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			team = form.save()
			return redirect(index)
		else:
			print(form.errors)
	else: 
		form = TeamForm()
	return render(request, 'team_management/add_team.html',{'form':form,})


def user_login(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/manage/')
			else: 
				return HttpResponse("Your account has been deactivated")
		else: 
			print("Invalid login details: {0},{1}".format(username,password))
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request,'team_management/login.html',{})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/manage/')

@login_required
def team_add_member_list(request, team_slug):
	context_dict = {}
	team = Team.objects.get(slug = team_slug)
	eligible_members = Member.objects.exclude(team = team)
	team_size = Member.objects.filter(team=team).count()
	context_dict['team'] = team
	context_dict['eligible_members'] = eligible_members
	context_dict['team_size'] = team_size
	return render(request,'team_management/team_add_member_list.html',context_dict) 

@login_required
def team_add_member(request, team_slug, member_id):
	team = Team.objects.get(slug = team_slug)
	member = Member.objects.get(pk=member_id)
	member.team = team 
	member.save()
	return render(request,'team_management/team_add_member.html',{'team':team,'member':member,'team_slug':team_slug})

@login_required
def remove_member(request, team_slug, member_id):
	team = Team.objects.get(slug = team_slug)
	member = Member.objects.get(pk=member_id)
	member.team = None
	member.save()
	return redirect('team', team_slug = team_slug)

@login_required
def member_index(request):
	members = Member.objects.all()
	return render(request,'team_management/member_index.html',{'members':members,})

@login_required
def edit_team(request,team_slug):
	team = get_object_or_404(Team,slug=team_slug)
	if request.method == "POST":
		form = TeamForm(request.POST, instance=team)
		if form.is_valid():
			team = form.save()
			return redirect('team', team_slug=team_slug)
		else:
			print(form.errors)
	else:	
		form = TeamForm(instance=team)
	return render(request, 'team_management/edit_team.html',{'form':form,'team':team,})

@login_required
def edit_member(request,member_id):
	member = get_object_or_404(Member,pk=member_id)
	if request.method == "POST":
		form = MemberForm(request.POST, instance=member)
		if form.is_valid():
			member = form.save(commit=False)
			if 'picture' in request.FILES:
				member.picture = request.FILES['picture']
			member.save()
			return redirect('member',member_id=member_id)
		else:
			print(form.errors)
	else:
		form = MemberForm(instance=member)
	return render(request, 'team_management/edit_member.html',{'form':form,'member':member,})

def delete_team(request,team_slug):
	team = get_object_or_404(Team, slug=team_slug)
	members = Member.objects.filter(team=team)
	for member in members:
		member.team = None
		member.save()
	team.delete()
	return redirect('index_page')

def team_delete_confirmation(request, team_slug):
	team = get_object_or_404(Team, slug=team_slug)
	return render(request,'team_management/team_delete_confirmation.html',{'team':team,})
