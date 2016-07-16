#This is urls.py
from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index_page'),
	url(r'^team/add_team/$', views.add_team, name='add_team'),
	url(r'^team/(?P<team_slug>[\w\-]+)/$', views.team, name='team'),
	url(r'^team/(?P<team_slug>[\w\-]+)/add_mem/$', views.team_add_member_list, name='team_add_member_list'),
	url(r'^team/(?P<team_slug>[\w\-]+)/add_mem/(?P<member_id>[0-9]+)/$', views.team_add_member, name='team_add_member'),	
	url(r'^team/(?P<team_slug>[\w\-]+)/remove_mem/(?P<member_id>[0-9]+)/$', views.remove_member, name='remove_member'),		
	url(r'^team/(?P<team_slug>[\w\-]+)/edit/$',views.edit_team, name='edit_team'),
	url(r'^team/(?P<team_slug>[\w\-]+)/delete/$', views.team_delete_confirmation, name='team_delete_confirmation'),
	url(r'^team/(?P<team_slug>[\w\-]+)/delete/confirmed/$', views.delete_team, name='delete_team'),
	url(r'^member/$', views.member_index, name='member_index'),
	url(r'^member/(?P<member_id>[0-9]+)/$', views.member, name='member'),
	url(r'^member/(?P<member_id>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
	url(r'^member/(?P<member_id>[0-9]+)/edit/$', views.edit_member, name='edit_member'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^register/$', views.register, name='register'),
]