from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

from djan import settings


class BlackIpMiddleware(MiddlewareMixin):
	def process_request(self, request):
		if request.META['REMOTE_ADDR'] in getattr(settings, 'BLACK_IPS', []):
			return HttpResponseForbidden()
