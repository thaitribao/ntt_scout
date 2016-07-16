#This is urls.py for scout_info
from django.conf.urls import url 
from . import views

urlpatterns = [
	#url(r'^$', views.index, name='index_page'),
	url(r'^camp/$',views.camp_index, name='camp_index'),#View all camps
	url(r'^camp/add/$', views.add_camp, name='add_camp'), #Add a new camp
	url(r'^camp/(?P<camp_name_slug>[\w\-]+)/$', views.camp, name='camp'), #View a specific camp
	url(r'^camp/(?P<camp_name_slug>[\w\-]+)/edit/$', views.edit_camp, name='edit_camp'),
 	#url(r'^camp/add_camp/$',views.add_camp, name='add_camp'),
	#url(r'^team/(?P<team_slug>[\w\-]+)/add_mem/$', views.team_add_member_list, name='team_add_member_list'),
	#url(r'^team/(?P<team_slug>[\w\-]+)/add_mem/(?P<member_id>[0-9]+)/$', views.team_add_member, name='team_add_member'),	
	#url(r'^team/(?P<team_slug>[\w\-]+)/remove_mem/(?P<member_id>[0-9]+)/$', views.remove_member, name='remove_member'),		
	url(r'^profile/(?P<member_id>[0-9]+)/$', views.scout_profile, name='profile'),#View a Scout profile
	url(r'^profile/(?P<member_id>[0-9]+)/add_profile/$', views.add_profile, name='add_profile'), # Add a new profile
	url(r'^profile/(?P<member_id>[0-9]+)/edit/$', views.edit_profile, name='edit_profile'),
	url(r'^document/$',views.document_index, name='document_index'), #View all documents
	url(r'^document/category/$', views.category_index, name='category_index'), #View all categories
	url(r'^document/category/(?P<category_slug>[\w\-]+)/$', views.category, name='category'), #View a category
	url(r'^document/category/(?P<category_slug>[\w\-]+)/edit/$', views.edit_category, name='edit_category'),
	url(r'^document/category/(?P<category_slug>[\w\-]+)/delete/$', views.category_delete_confirmation, name='category_delete_confirmation'),
	url(r'^document/category/(?P<category_slug>[\w\-]+)/delete/confirmed/$', views.delete_category, name='delete_category'),
	url(r'^document/add_category/$', views.add_category, name='add_category'), #Add a new category
	url(r'^document/add_document/$', views.add_document, name = 'add_doc'),#Add a new document
	url(r'^document/(?P<document_slug>[\w\-]+)/edit/$', views.edit_document, name='edit_document'),
	url(r'^document/(?P<document_slug>[\w\-]+)/delete/$', views.document_delete_confirmation, name='document_delete_confirmation'),
	url(r'^document/(?P<document_slug>[\w\-]+)/delete/confirmed/$', views.delete_document, name='delete_document'),
	url(r'^item/$', views.item_index, name='item_index'),#View all items
	url(r'^item/add_item/$', views.add_item, name='add_item'), #Add a new item to the inventory
	url(r'^item/(?P<item_slug>[\w\-]+)/edit/$', views.edit_item, name='edit_item'),
]