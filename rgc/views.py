from celery.result import AsyncResult
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.urls import path
from django.views.decorators.cache import cache_page, cache_control
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny
import logging
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers
from django_redis import get_redis_connection

from rgc.models.person import Person


# from djan.urls import urlpatterns

# @xframe_options_deny
# @xframe_options_exempt
def index(request):
	# urlpatterns.append(path('index/', index))
	print('dfdfdfs')
	# print(urlpatterns)
	# print(4/0)
	log = logging.getLogger('django.server')
	log.debug('welcome in to index!')
	log.error('welcome in to index!')
	log.warning('welcome in to index!')
	# return render(request, "debug.html")
	# log_one = logging.getLogger('admin')
	# log_one.info('welcome in to index!!!')
	# from django.core.mail import send_mail  # 导入django发送邮件模块
	# send_mail('subject', 'message', '2020956572@qq.com', ['2020956572@qq.com'], fail_silently=False)
	return HttpResponse('Hello!!!欢迎！！！')


def init(request):
	return HttpResponse('Hello!!!欢迎！！！')


def reg(request):
	a = request.GET['a']
	b = request.GET['b']
	# return HttpResponseRedirect(reverse(new_reg,args=(a,b)))
	# return HttpResponseRedirect('/new_reg1/{}/{}/'.format(a,b))
	return HttpResponseRedirect('/new_reg1/?a={}&b={}'.format(a, b))


def new_reg(request, a, b):
	return HttpResponse('Hello!!!欢迎！！！reg_new:{}'.format(int(a) + int(b)))


def new_reg1(request):
	a = request.GET['a']
	b = request.GET['b']
	return HttpResponse('Hello!!!欢迎！！！reg_new1:{}'.format(int(a) + int(b)))


def register(request):
	keys = request.GET.keys()  # 返回所有请求参数的key
	if 'name' and 'age' in keys:
		name = request.GET['name']
		age = int(request.GET['age'])
		Person.add({'name': name, 'age': age})
		res = Person.get_by_name_age({'name': name, 'age': age})
		return render(request, "debug.html", {'result': res.name})
	return render(request, "debug.html", {'result': 'please input name and age!'})


# return HttpResponse(res.name, status=200, reason='Not test')


def debug_view(request):
	"""
	测试使用
	:param request:
	:return:
	"""
	Person.add({'name': 'df', 'age': 12})
	return render(request, "debug.html")


def export(request):
	ct = request.GET['ct']
	ids = request.GET['ids']
	return render(request, "debug.html", {'result': '{} !!! {}'.format(ct, ids)})


def post(request):
	re = ''
	if request.method == 'POST':
		if 'name' in request.POST.keys():
			print('df')
		print(request.POST)
		re = request.POST['name']
		print(request.content_type)
	x = csrf(request)
	csrf_token = x['csrf_token']
	return HttpResponse('{} ; {}'.format(str(re), csrf_token))


# 所有人访问此接口都会使用10s的缓存
# @cache_page(10)
def redis(request):
	# cache 实际调用的是redis/client，也就是说 通过cache可以操作任何redis方法
	cache.set('is_name', 'value', timeout=None)
	print(type(cache))
	print(cache.get('rgc'), cache.ttl('rgc'))

	# 最好改为全局变量
	red = get_redis_connection('origin_redis')
	print(red)
	red.hset('hs', 'name', 'val')
	import random
	return HttpResponse('redis test success!{}'.format(random.random()))


# @vary_on_cookie
@vary_on_headers('User-Agent')
def cookie_random(request):
	import random
	res = HttpResponse('redis test success!{}'.format(random.random()))
	# patch_vary_headers(res, ['Cookie'])
	return res


@cache_control(public=True, max_age=10)
def cache_pub(request):
	import random
	return HttpResponse('redis test success!{}'.format(random.random()))


@cache_control(max_age=10)
def cache_pri(request):
	import random
	response = HttpResponse('redis test success!{}'.format(random.random()))
	# patch_cache_control(response, private=True, max_age=10)
	# print(response['Cache-Control'])
	return response


from django.dispatch import receiver
import django.dispatch

# 创建信号
work_done_signal = django.dispatch.Signal(providing_args=['path', 'time'])


# views函数
def create_signal(request):
	url_path = request.path
	print('send signal!')
	# 发送信号
	result = work_done_signal.send_robust(create_signal, path=url_path, time='2019-01-01')
	print(result[0][1])
	return JsonResponse({'name': 'OK'})


# 信号接收器
@receiver(work_done_signal, sender=create_signal)
def view_callback(sender, **kwargs):
	# 处理函数
	print(sender)
	print('处理信号！{}，{}'.format(kwargs['time'], kwargs['path']))
	return 4 / 0


# celery的使用
# https://www.cnblogs.com/znicy/p/5626040.html
# 开启celery方式，控制台输入:python manage.py celery worker -c 4 --loglevel=info
# 查询任务执行情况，控制台输入：python manage.py celery flower    ;浏览器输入 http://localhost:5555/ 查看
def celery_test(request):
	from rgc.tasks import task_job
	task_info = {'name': 'rgc', 'age': 1}
	# 向 celery添加任务
	result = task_job.delay(task_info)
	# result.id 指 此任务的id,在后面查询结果时会用到
	return JsonResponse({'status': str(result.id)})


# celery结果获取
def get_celery_result(request):
	# 任务id
	if 'id' in request.GET.keys():
		id = request.GET['id']
		# 获取 celery任务执行的结果及是否成功
		result = AsyncResult(id)
		# if result.state!='PENDING':
		# 	result.forget()
		return JsonResponse({'result': result.result, 'is_success': result.successful(), 'state': result.state})
	else:
		return JsonResponse({'warn': 'please input id!!'})
