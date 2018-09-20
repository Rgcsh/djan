from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection

from rgc.models import Person


def index(request):
	# return render(request, "debug.html")
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
	print(request.__init__)
	name = request.GET['name']
	age = int(request.GET['age'])
	Person.add({'name': name, 'age': age})
	res = Person.get_by_name_age({'name': name, 'age': age})
	return render(request, "debug.html", {'result': res.name})


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


@cache_page(10)
def redis(request):
	# cache 实际调用的是redis/client，也就是说 通过cache可以操作任何redis方法
	cache.set('rgc', 'val', timeout=None)
	print(type(cache))
	print(cache.get('rgc'), cache.ttl('rgc'))

	# 最好改为全局变量
	red = get_redis_connection('origin_redis')
	print(red)
	red.hset('hs', 'name', 'val')
	import random
	return HttpResponse('redis test success!{}'.format(random.random()))
