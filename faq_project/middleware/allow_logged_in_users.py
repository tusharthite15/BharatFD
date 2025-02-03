# my_project/middleware/allow_logged_in_users.py
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is accessing the admin and is logged in
        if request.path.startswith('/admin/') and request.user.is_authenticated:
            # Allow logged-in users to access admin
            if not request.user.is_staff:
                return HttpResponseForbidden("You do not have permission to access this page")
        return self.get_response(request)
