# from django.urls import path
# from .views import FAQListView, faq_view  

# urlpatterns = [
#     path('faq/', faq_view, name='faq-page'),  # Renders FAQ page
#     path('api/faqs/', FAQListView.as_view(), name='faq-api'),  # API returns JSON
#     path('', faq_view, name='home'),  # Redirects root to FAQ page
# ]
from django.contrib import admin
from django.urls import path, include
from .views import NoLoginAdminLoginView


urlpatterns = [
    path('admin/login/', NoLoginAdminLoginView.as_view(), name='admin_login'),  # Custom admin login view
    path('admin/', admin.site.urls),  
    path('', include('faq_app.urls')),  # Include the app's URL patterns
]
