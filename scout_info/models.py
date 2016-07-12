from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from team_management.models import Member
# Create your models here.

#Model that hold information with regard to Scouting life
class Scout_Profile(models.Model):
	member = models.OneToOneField(Member)
	khan_quang = models.BooleanField(default=False)
	tan_sinh = models.BooleanField(default=False)
	hang_nhi = models.BooleanField(default=False)
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
	position = models.CharField(max_length = 4, choices=POSITION_CHOICES, null=True)
	khan_tan_sinh = models.URLField(max_length=200, null=True)
	khan_hang_nhi = models.URLField(max_length=200, null=True)

	def __str__(self):
		return self.member.user.get_full_name()

#Model that hold information about a Camp
class Camp(models.Model):
	name = models.CharField(max_length = 30, null=True)
	location = models.CharField(max_length = 30, null=True)
	start_date = models.DateField(default=timezone.now())
	end_date = models.DateField(default=timezone.now())
	members = models.ManyToManyField(Member)
	giay_trai = models.URLField(max_length=200, null=True)
	comment = models.TextField(max_length = 1000, null=True)
	slug = models.SlugField(default="")

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Camp,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

#Category for different Documents
class Category(models.Model):
	name = models.CharField(max_length = 30, null=False)
	slug = models.SlugField(default="")

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

#Model for a Document
class Document(models.Model):
	name = models.CharField(max_length = 100, null=False)
	slug = models.SlugField(default="")
	link = models.URLField(max_length=200, null=True)
	category = models.ForeignKey(Category)

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Document,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

#Model for Item in Inventory
class Item(models.Model):
	name = models.CharField(max_length = 100, null=False)
	slug = models.SlugField(default="")
	quantity = models.IntegerField(default=0)
	location = models.CharField(max_length = 100, null=False)
	keeper = models.ForeignKey(Member)
	note = models.TextField(max_length = 200, null=True)
	last_update = models.DateTimeField(default=timezone.now())

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Item,self).save(*args,**kwargs)

	def __str__(self):
		return self.name