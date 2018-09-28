from django.contrib import admin

# Register your models here.
from blog.models import Blog


@admin.register(Blog)
class PersonAdmin(admin.ModelAdmin):
	# http://www.liujiangblog.com/course/django/158  自定制Admin
	prepopulated_fields = {'url': ('name',)}
	list_filter = ('name', 'age', 'bool')
