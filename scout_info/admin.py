from django.contrib import admin
from .models import Camp, Scout_Profile, Document, Category
# Register your models here.
class CampAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class DocumentAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

admin.site.register(Camp, CampAdmin)
admin.site.register(Scout_Profile)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Category, CategoryAdmin)