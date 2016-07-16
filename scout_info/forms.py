#This is forms.py
from django import forms
from .models import Scout_Profile, Camp, Category, Document, Item
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone
from team_management.models import Member

#Form for creating a new camp
class CampForm(forms.ModelForm):
	name = forms.CharField(max_length=30, help_text="Tên kì trại: ")
	location = forms.CharField(max_length=30, help_text="Địa điểm: ")
	start_date = forms.DateField(widget=SelectDateWidget(years=range(timezone.now().year-10,timezone.now().year+1)), initial=timezone.now().date(), help_text="Ngày khởi hành")
	end_date = forms.DateField(widget=SelectDateWidget(years=range(timezone.now().year-10,timezone.now().year+1)), initial=timezone.now().date(), help_text="Ngày kết thúc")
	members = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), help_text="Danh sách người tham gia", required = False)
	giay_trai = forms.URLField(max_length=300, help_text="Link Google Drive cho giấy trại", required=False)
	comment = forms.CharField(widget=forms.Textarea, help_text="Nhận xét về kì trại")
	class Meta:
		model = Camp
		fields = ('name','location','start_date','end_date','members','giay_trai','comment')

#Form for creating a new Scout profile
class Scout_ProfileForm(forms.ModelForm):
	NONE = 'NON'
	SENIOR_PATROL_LEADER = 'SPL' 
	ASSISTANT_SENIOR_PATROL_LEADER = 'ASPL'
	ASSISTANT_TROOP_LEADER = 'ATL'
	TROOP_LEADER = 'PL'
	SUPER_TROOP_LEADER = 'STL'
	POSITION_CHOICES = (
		(NONE,'Không có'),
		(SENIOR_PATROL_LEADER, 'Đội trưởng Nhất'),
		(ASSISTANT_SENIOR_PATROL_LEADER,'Phụ tá Đội trưởng Nhất'),
		(ASSISTANT_TROOP_LEADER,'Thiếu phó/Phụ tá'),
		(TROOP_LEADER,'Thiếu trưởng'),
		(SUPER_TROOP_LEADER,'Liên đoàn Trưởng'),
	)
	khan_quang = forms.BooleanField(help_text="Đã có khăn quàng")
	tan_sinh = forms.BooleanField(help_text="Đã Tuyên hứa")
	hang_nhi = forms.BooleanField(help_text="Đã được trao Hạng Nhì")
	position = forms.ChoiceField(help_text="Chức vụ",choices=POSITION_CHOICES,widget=forms.RadioSelect())
	khan_tan_sinh = forms.URLField(help_text="Link Google Drive cho chương trình Tân Sinh", required=  False)
	khan_hang_nhi = forms.URLField(help_text="Link Google Drive cho chương trình Hạng Nhì", required = False)
	class Meta:
		model = Scout_Profile
		fields = ('khan_quang','tan_sinh','hang_nhi','position','khan_tan_sinh','khan_hang_nhi')


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=30, help_text="Tên thể loại: ")

	class Meta:
		model = Category
		fields = ('name',)


class DocumentForm(forms.ModelForm):
	name = forms.CharField(max_length=30, help_text="Tên tài liệu: ")
	category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Thể loại: ", required = False)
	link = forms.URLField(help_text="Link Google Drive cho tài liệu: ")

	class Meta:
		model = Document
		fields = ('name','category','link')

class ItemForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Tên vật dụng: ")
	quantity = forms.IntegerField(initial=0, help_text="Số lượng: ")
	location = forms.CharField(max_length=100, help_text="Địa điểm: ")
	keeper = forms.ModelChoiceField(queryset=Member.objects.all(), help_text="Người giữ: ")
	note = forms.CharField(widget=forms.Textarea, help_text="Ghi chú")

	class Meta:
		model = Item
		fields = ('name','quantity','location', 'keeper','note')

