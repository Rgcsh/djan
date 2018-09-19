from django.contrib import admin
from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
# from rgc.widgets import RichTextEditorWidget
from django.utils.html import format_html

from rgc.models import Person

AdminSite.empty_value_display = ''  # 空字符显示
admin.site.disable_action('delete_selected')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	# http://www.liujiangblog.com/course/django/158  自定制Admin
	prepopulated_fields = {'url': ('name',)}
	list_filter = ('name', 'age', 'bool')
	list_per_page = 10
	list_display = ['name', 'age', 'other', 'bool', 'time', 'red_name', ]
	# fields = (('name', 'age'), 'other')
	readonly_fields = ['other', 'many']
	ordering = ['-time']
	list_editable = ['other']
	search_fields = ['age', 'name']  # 两个字段中模糊搜素
	# disable_action = ['delete_selected']
	fieldsets = (
		('Edit', {
			'classes': ('wide',),
			'fields': ('name', 'age', 'many',),
			'description': format_html('<span style="color:red">Enable Edit Field!</span>'),
		}),
		('UnEdit', {
			'classes': ('collapse',),
			'fields': ('url', 'other', 'bool',),
			'description': 'Disable Edit field!',
		}),
	)

	filter_vertical = ('many',)
	actions = ['some_test', 'export_selected_objects', 'delete_selected']
	# actions_on_top = False
	# actions_on_bottom = True
	actions_selection_counter = False
	date_hierarchy = 'time'

	def red_name(self, obj):
		return format_html('<span style="color:red">{}</span>'.format(obj.name))

	def some_test(self, request, queryset):
		# do something for yourself!
		res = str([item.name for item in queryset])
		self.message_user(request, '{} are update success!!'.format(res), level=messages.SUCCESS)

	def export_selected_objects(modeladmin, request, queryset):
		selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
		ct = ContentType.objects.get_for_model(queryset.model)
		print([item.name for item in queryset])
		print(selected, ct)
		return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

	def get_actions(self, request):
		actions = super().get_actions(request)
		if request.user.username[0].upper() != 'j':
			if 'delete_selected' in actions:
				del actions['delete_selected']
		return actions

	some_test.short_description = 'some_test by rgc!'
	export_selected_objects.short_description = 'export_selected'
