from django.shortcuts import render, redirect, get_object_or_404
from .models import Song, Album
from django.utils import timezone
from .forms import SongForm, AlbumForm
from django.contrib.auth.decorators import login_required
from team_management.views import check_admin_right
# Create your views here.

def song_index(request):
	is_admin = False
	if request.user.is_authenticated():
		is_admin = check_admin_right(request.user)
	songs = Song.objects.all().order_by('name',)
	return render(request,'public_site/song_index.html',{'songs':songs,'is_admin':is_admin,})

def song(request,song_slug):
	is_admin = False
	if request.user.is_authenticated():
		is_admin = check_admin_right(request.user)
	song = get_object_or_404(Song, slug=song_slug)
	return render(request,'public_site/song.html',{'song':song,'is_admin':is_admin,})

@login_required
def add_song(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == "POST":
			form = SongForm(request.POST)
			if form.is_valid():
				song = form.save()
				return redirect('Public:song_index')
			else:
				print(form.errors)
		else: 
			form = SongForm()
		return render(request, 'public_site/add_song.html',{'form':form,})
	else:
		return render(request,'public_site/access_denied.html',{})

@login_required
def edit_song(request,song_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		song = get_object_or_404(Song, slug=song_slug)
		if request.method == "POST":
			form = SongForm(request.POST, instance=song)
			if form.is_valid():
				song = form.save()
				return redirect('Public:song', song_slug=song.slug)
			else:
				print(form.errors)
		else:	
			form = SongForm(instance=song)
		return render(request, 'public_site/edit_song.html',{'form':form,'song':song,})
	else: 
		return render(request, 'public_site/access_denied.html', {})

def album_index(request):
	is_admin = False
	if request.user.is_authenticated():
		is_admin = check_admin_right(request.user)
	albums = Album.objects.all().order_by('-date_taken','name')
	return render(request,'public_site/album_index.html',{'albums':albums,'is_admin':is_admin,})

@login_required
def add_album(request):
	is_admin = check_admin_right(request.user)
	if is_admin:
		if request.method == "POST":
			form = AlbumForm(request.POST)
			if form.is_valid():
				album = form.save()
				return redirect('Public:album_index')
			else:
				print(form.errors)
		else: 
			form = AlbumForm()
		return render(request, 'public_site/add_album.html',{'form':form,})
	else:
		return render(request,'public_site/access_denied.html',{})

@login_required
def edit_album(request,album_slug):
	is_admin = check_admin_right(request.user)
	if is_admin:
		album = get_object_or_404(Album, slug=album_slug)
		if request.method == "POST":
			form = AlbumForm(request.POST, instance=album)
			if form.is_valid():
				album = form.save()
				return redirect('Public:album_index', album_slug=album.slug)
			else:
				print(form.errors)
		else:	
			form = AlbumForm(instance=album)
		return render(request, 'public_site/edit_album.html',{'form':form,'album':album,})
	else: 
		return render(request, 'public_site/access_denied.html', {})