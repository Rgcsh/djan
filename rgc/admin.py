from django.contrib import admin
from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from rgc.models import Person

AdminSite.empty_value_display = ''  # 空字符显示
admin.site.disable_action('delete_selected')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ['name', 'age', 'other', 'time']
	# fields = (('name', 'age'), 'other')
	readonly_fields = ['other']
	ordering = ['-time']
	search_fields = ['age', 'name']  # 两个字段中模糊搜素
	# disable_action = ['delete_selected']
	fieldsets = (
		('Edit', {
			'classes': ('wide',),
			'fields': ('name', 'age', 'many',),
			'description': {'name': 'dfdf'},
		}),
		('UnEdit', {
			'classes': ('collapse',),
			'fields': ('url', 'other',),
		}),
	)
	filter_vertical = ('many',)
	actions = ['some_test', 'export_selected_objects', 'delete_selected']
	# actions_on_top = False
	# actions_on_bottom = True
	actions_selection_counter = False
	date_hierarchy = 'time'

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
