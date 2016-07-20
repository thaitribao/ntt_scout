from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.

class Song(models.Model):
	name = models.CharField(max_length = 30, default="", unique=True)
	lyric = models.TextField(max_length=2000, default="")
	link = models.URLField(max_length=300, null=True, blank=True)
	slug = models.SlugField(default="")

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Song,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

class Album(models.Model):
	name = models.CharField(max_length = 100, default="", unique=True)
	link = models.URLField(max_length=2000, default="")
	date_taken = models.DateField(default=timezone.now())
	slug = models.SlugField(default="")

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Album,self).save(*args,**kwargs)

	def __str__(self):
		return self.name
