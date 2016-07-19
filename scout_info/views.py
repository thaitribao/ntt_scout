from django.shortcuts import render, redirect, get_object_or_404
from .models import Scout_Profile, Camp, Document, Category, Item
from team_management.models import Member, Team
from django.utils import timezone
import team_management
from .forms import CampForm, Scout_ProfileForm, CategoryForm, DocumentForm, ItemForm
from django.contrib.auth.decorators import login_required
from team_management.views import check_admin_right
# Create your views here.

#View information related to Scouting of a member given their ID
@login_required
def scout_profile(request, member_id):
	is_admin = check_admin_right(request.user)
	member = Member.objects.get(pk=member_id)
	profile = Scout_Profile.objects.get(member=member)
	team = member.team
	camps = member.camp_set.all()
	context_dict={'member':member,'profile':profile,'team':team,'camps':camps,'is_admin':is_admin,}
	return render(request, 'scout_info/scout_profile.html',context_dict)

#Add a new set of information for a scout given their ID
@login_required
def add_profile(request, member_id):
	is_admin = check_admin_right(request.user)
	if is_admin:
		member = Member.objects.get(pk=member_id)
		if request.method == 'POST':
			form = Scout_ProfileForm(request.POST)
			if form.is_valid():
				profile = form.save(commit=False)
				if not profile.khan_quang:
					profile.khan_quang_date = None
				if not profile.tan_sinh:
					profile.tan_sinh_date = None
				if not profile.hang_nhi:
					profile.hang_nhi = None
				profile.member = member
				profile.save()
				return redirect(team_management.views.member, member_id=member_id)
			else: 
				print(form.errors)
		else:
			form = Scout_ProfileForm()
		return render(request, 'scout_info/add_profile.html', {'form':form,'member':member})
	else: 
		return render(request, 'scout_info/access_denied.html', {})

#View information of all camps in the DB
@login_required
def camp_index(request):
	is_admin = check_admin_right(request.user)
	camps = Camp.objects.all()
	return render(request, 'scout_info/camp_index.html',{'camps':camps,'is_admin':is_admin,})

#Add a new camp to the DB
@login_required
def add_camp(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == 'POST':
			form = CampForm(request.POST)
			if form.is_valid():
				camp = form.save()
				return redirect('Scout_Info:camp_index')
			else:
				print(form.errors)
		else:
			form = CampForm()
		return render(request,'scout_info/add_camp.html',{'form':form,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

#View all information related to a specific camp given their slug
@login_required
def camp(request, camp_name_slug):
	is_admin = check_admin_right(request.user)
	camp = Camp.objects.get(slug=camp_name_slug)
	campers = camp.members.all()
	context_dict={'camp':camp,'campers':campers,'is_admin':is_admin,}
	return render(request, 'scout_info/camp.html',context_dict)


#Deleting an old document
#Delete a category

#View all documents (need url)
@login_required
def document_index(request):
	is_admin = check_admin_right(request.user)
	documents = Document.objects.all()
	context_dict={'documents':documents,'is_admin':is_admin}
	return render(request,'scout_info/document_index.html',context_dict)

#View all categories(need url)
@login_required
def category_index(request):
	is_admin = check_admin_right(request.user)
	categories = Category.objects.all()
	context_dict={'categories':categories,'is_admin':is_admin,}
	return render(request,'scout_info/category_index.html',context_dict)

#View documents belong to a category(need url)
@login_required
def category(request,category_slug):
	is_admin = check_admin_right(request.user)
	category = Category.objects.get(slug=category_slug)
	documents = Document.objects.filter(category=category)
	context_dict={'category':category,'documents':documents,'is_admin':is_admin,}
	return render(request,'scout_info/category.html',context_dict)

#Create a new category (need url)
@login_required
def add_category(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == 'POST':
			form = CategoryForm(request.POST)
			if form.is_valid():
				category = form.save()
				return redirect('Scout_Info:category_index')
			else: 
				print(form.errors)
		else:
			form = CategoryForm()
		return render(request,'scout_info/add_category.html',{'form':form,})
	else: 
		return render(request, 'scout_info/access_denied.html', {})

#Create a new document (need url)
@login_required
def add_document(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == 'POST':
			form = DocumentForm(request.POST)
			if form.is_valid():
				document = form.save()
				return redirect('Scout_Info:document_index')
			else:
				print(form.errors)
		else:
			form = DocumentForm()
		return render(request,'scout_info/add_document.html',{'form':form,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

#View all items in the inventory (need url, html)
@login_required
def item_index(request):
	is_admin = check_admin_right(request.user)
	items = Item.objects.all()
	return render(request,'scout_info/item_index.html',{'items':items,'is_admin':is_admin,})

#Create a new inventory item (need url, html)
@login_required
def add_item(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == 'POST':
			form = ItemForm(request.POST)
			if form.is_valid():
				item = form.save(commit=False)
				item.last_update = timezone.datetime.now()
				item.save()
				return redirect('Scout_Info:item_index')
			else:
				print(form.errors)
		else:
			form = ItemForm()
		return render(request,'scout_info/add_item.html',{'form':form,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def edit_item(request, item_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		item = get_object_or_404(Item, slug=item_slug)
		if request.method == "POST":
			form = ItemForm(request.POST, instance=item)
			if form.is_valid():
				item = form.save(commit=False)
				item.last_update = timezone.datetime.now()
				item.save()
				return redirect('Scout_Info:item_index')
			else:
				print(form.errors)
		else:	
			form = ItemForm(instance=item)
		return render(request, 'scout_info/edit_item.html',{'form':form,'item':item,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def edit_document(request, document_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		document = get_object_or_404(Document, slug=document_slug)
		if request.method == "POST":
			form = DocumentForm(request.POST, instance=document)
			if form.is_valid():
				document = form.save()
				return redirect('Scout_Info:document_index')
			else:
				print(form.errors)
		else:	
			form = DocumentForm(instance=document)
		return render(request, 'scout_info/edit_document.html',{'form':form,'document':document,})
	else: 
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def edit_camp(request, camp_name_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		camp = get_object_or_404(Camp, slug=camp_name_slug)
		if request.method == "POST":
			form = CampForm(request.POST, instance=camp)
			if form.is_valid():
				camp = form.save()
				return redirect('Scout_Info:camp', camp_name_slug=camp_name_slug)
			else:
				print(form.errors)
		else:	
			form = CampForm(instance=camp)
		return render(request, 'scout_info/edit_camp.html',{'form':form,'camp':camp,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def edit_category(request, category_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		category = get_object_or_404(Category, slug=category_slug)
		if request.method == "POST":
			form = CategoryForm(request.POST, instance=category)
			if form.is_valid():
				category = form.save()
				return redirect('Scout_Info:category', category_slug=category_slug)
			else:
				print(form.errors)
		else:	
			form = CategoryForm(instance=category)
		return render(request, 'scout_info/edit_category.html',{'form':form,'category':category,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def edit_profile(request, member_id):
	is_admin = check_admin_right(request.user)
	if is_admin:
		member = Member.objects.get(pk=member_id)
		profile = Scout_Profile.objects.get(member=member)
		if request.method == "POST":
			form = Scout_ProfileForm(request.POST, instance=profile)
			if form.is_valid():
				profile = form.save(commit=False)
				if not profile.khan_quang:
					profile.khan_quang_date = None
				if not profile.tan_sinh:
					profile.tan_sinh_date = None
				if not profile.hang_nhi:
					profile.hang_nhi = None
				profile.save()
				return redirect('Scout_Info:profile', member_id=member_id)
			else:
				print(form.errors)
		else:	
			form = Scout_ProfileForm(instance=profile)
		return render(request, 'scout_info/edit_profile.html',{'form':form,'profile':profile,'member':member,})
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def delete_category(request,category_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		category = get_object_or_404(Category, slug=category_slug)
		documents = Document.objects.filter(category=category)
		for document in documents:
			document.category = None
			document.save()
		category.delete()
		return redirect('Scout_Info:category_index')
	else:
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def category_delete_confirmation(request, category_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		category = get_object_or_404(Category, slug=category_slug)
		return render(request,'scout_info/category_delete_confirmation.html',{'category':category,})
	else: 
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def document_delete_confirmation(request, document_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		document = get_object_or_404(Document, slug=document_slug)
		return render(request,'scout_info/document_delete_confirmation.html',{'document':document,})
	else: 
		return render(request, 'scout_info/access_denied.html', {})

@login_required
def delete_document(request, document_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		document = get_object_or_404(Document, slug=document_slug)
		document.delete()
		return redirect('Scout_Info:document_index')
	else: 
		return render(request, 'scout_info/access_denied.html', {})