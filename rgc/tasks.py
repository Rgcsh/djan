import time

from celery import task


# 可以做一些耗时并且用户不用必须等待的操作，
@task
def task_job(name):
	print(name)
	time.sleep(20)
	import random
	return 'yes {}'.format(random.randint(1,10000))
