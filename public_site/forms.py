from django import forms
from .models import Song, Album
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

#Form for creating a new song
class SongForm(forms.ModelForm):
	name = forms.CharField(max_length=30, help_text="Tên bài hát: ")
	link = forms.URLField(max_length=300, help_text="Link tới clip nhạc: ", required=False)
	lyric = forms.CharField(widget=forms.Textarea, help_text="Lời bài hát: ")
	class Meta:
		model = Song
		fields = ('name','lyric','link',)


class AlbumForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Tên album: ")
	link = forms.URLField(max_length=300, help_text="Link tới album: ")
	date_taken = forms.DateField(widget=SelectDateWidget(years=range(timezone.now().year-10,timezone.now().year+1)), initial=timezone.now().date(), help_text="Ngày chụp: ")

	class Meta:
		model = Album
		fields = ('name','link','date_taken',)
