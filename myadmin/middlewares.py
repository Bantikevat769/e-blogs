# middleware.py

from django.http import HttpResponseForbidden

class SuperuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            return self.get_response(request)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
