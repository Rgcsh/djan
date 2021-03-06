import ast

from django.db import models
from django.utils.translation import gettext_lazy as _


class ListFiled(models.CharField):
	description = _("Store a python list")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def to_python(self, value):
		if not value:
			value = []

		if isinstance(value, list):
			return value

		return ast.literal_eval(value)

	def get_prep_value(self, value):
		if value is None:
			return value

		return str(value)

	def value_to_string(self, obj):
		value = self.value_from_object(obj)
		return self.get_db_prep_value(value)
