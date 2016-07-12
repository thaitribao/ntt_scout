from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=20, default="")
    slogan = models.CharField(max_length=20, default="")
    slug = models.SlugField(default="")
    max_capacity = 8

    def save(self, *args, **kwargs):
        self.slug = slugify(self.team_name)
        super(Team,self).save(*args,**kwargs)

    def __str__(self):
        return self.team_name


class Member(models.Model):
    user = models.OneToOneField(User) #one profile correspond to one user
    #picture = models.ImageField(upload_to='profile_images', blank = True) #optional profile pics
    birthday = models.DateField(default=timezone.now()) #birthday
    team = models.ForeignKey(Team, null=True)
    join_date = models.DateField(default=timezone.now())
    #contact info
    address = models.CharField(max_length=500, default="", null=True)
    facebook = models.CharField(max_length=30, default="", null=True)
    dad_name = models.CharField(max_length=40, default="", null=True)
    dad_phone = models.PositiveIntegerField(default=0, null=True)
    mom_name = models.CharField(max_length=40, default="", null=True)
    mom_phone = models.PositiveIntegerField(default=0, null=True)
    home_phone = models.PositiveIntegerField(default=0, null=True)
    #school info
    current_grade = models.PositiveIntegerField(default=6, validators=[MaxValueValidator(13), MinValueValidator(1)])
    current_school = models.CharField(max_length=50, default="", null=True)
    health_info = models.TextField(max_length=1000, default="", null=True)

    def __str__(self):
        return self.user.get_full_name()


class Comment(models.Model):
    member = models.ForeignKey(Member)
    date = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User)
    comment = models.TextField(null=True, max_length=1000)

    def __str__(self):
        return self.member.user.get_full_name()
#Scout-related info should be another model 