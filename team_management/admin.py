from django.contrib import admin
from .models import Member, Team,Comment

class MemberAdmin(admin.ModelAdmin):
	list_display = ('user','team','home_phone','join_date')


class TeamAdmin(admin.ModelAdmin):
	list_display = ('team_name','slogan',)
	prepopulated_fields = {'slug':('team_name',)}
# Register your models here.

admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Comment)