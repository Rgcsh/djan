from django.db import models



class Person(models.Model):
	class Meta:
		db_table = 'person'  # 添加表名

	name = models.CharField(max_length=30)
	age = models.IntegerField()
	other = models.CharField(max_length=10, null=True)
	time = models.DateTimeField(auto_now=True)
	url = models.URLField(max_length=100, null=True)
	bool = models.BooleanField(default=True)
	te = models.BooleanField(default=True)
	many = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	@classmethod
	def add(cls, info):
		return cls.objects.get_or_create(**info)

	@classmethod
	def get_by_name_age(cls, info):
		return cls.objects.get(**info)

	def get_absolute_url(self):
		return str(self.name)
