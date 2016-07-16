#This is form.py
from django import forms
from .models import Team, Member, Comment
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('comment',)


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Password: ")
	username = forms.CharField(max_length=30, help_text="Tên đăng nhập: ")
	first_name = forms.CharField(max_length=30, help_text="Tên: ")
	last_name = forms.CharField(max_length=30, help_text = "Họ: ")
	email = forms.EmailField(max_length=200, help_text="Địa chỉ email: ")

	class Meta:
		model = User
		fields = ('username','last_name','first_name','email','password')


class MemberForm(forms.ModelForm):
	birthday = forms.DateField(widget=SelectDateWidget(years=range(timezone.now().year-30,timezone.now().year)), initial=timezone.now().date(), help_text="DD/MM/YYYY.")
	join_date = forms.DateField(widget=SelectDateWidget(years=range(timezone.now().year-20, timezone.now().year)), initial=timezone.now().date(), help_text="Ngay nhap doan.")
	address = forms.CharField(max_length=500, help_text="Địa chỉ: ", required=False)
	facebook = forms.CharField(max_length=30, help_text="Facebook: ", required=False)
	dad_name = forms.CharField(max_length=40, help_text="Tên cha: ", required=False)
	dad_phone = forms.IntegerField(initial=0, help_text="Số điện thoại cha: ") 
	mom_name = forms.CharField(max_length=40, help_text="Tên mẹ: ", required=False)
	mom_phone = forms.IntegerField(initial=0, help_text="Số điện thoại mẹ: ")
	home_phone = forms.IntegerField(initial=0, help_text="Số điện thoại nhà: ")
	current_grade = forms.IntegerField(initial=1, help_text="Lớp (ĐH = 13): ")
	current_school = forms.CharField(max_length=50, help_text="Trường: ", required=False)
	health_info = forms.CharField(max_length=1000, help_text="Tình trạng sức khỏe: ", required=False)

	class Meta:
		model = Member
		exclude = ('user','team',)


class TeamForm(forms.ModelForm):
	team_name = forms.CharField(max_length=20, help_text="Tên đội: ")
	slogan = forms.CharField(max_length=20, help_text="Tiếng kêu: ")

	class Meta:
		model = Team
		fields = ('team_name','slogan')



