# 数据库导入的脚本
import json
# 如下四行代码必须要，用来加载此项目的上下文
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djan.settings')
import django

django.setup()


def main():
	from rgc.models import Person
	with open('../fixture_dir/one.json', encoding='utf8') as f:
		# 单行插入
		for item in json.load(f):
			item['fields'].pop('many')
			res = Person.objects.create(**item['fields'])
			print(res)

	with open('one.json', encoding='utf8') as f:
		# 批量插入(速度更快，因为是放在一个sql执行)
		bulk_list = []
		for item in json.load(f):
			item['fields'].pop('many')
			person = Person(**item['fields'])
			bulk_list.append(person)
		res = Person.objects.bulk_create(bulk_list)
		print(res)


if __name__ == '__main__':
	main()
