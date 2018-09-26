from django.test import TestCase

# Create your tests here.
from rgc.models import Person


class PersonTestCase(TestCase):
	def test_person_url(self):
		name = 'one'
		Person.objects.create(**{'name': name, 'age': 1})
		per = Person.objects.get(**{'name': name})
		url = per.get_absolute_url()
		print(url)
		self.assertEqual(url, name)
