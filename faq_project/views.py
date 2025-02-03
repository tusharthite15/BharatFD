# views.py
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

class NoLoginAdminLoginView(LoginView):
    template_name = 'admin/login.html'

    def form_valid(self, form):
        # Automatically log in any user
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
