from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
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
	return render(request, "debug.html", {'result': '{} !!! {}'.format(ct,ids)})
