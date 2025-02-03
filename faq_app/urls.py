# from django.urls import path
# from .views import FAQListView, faq_view,insights_view,contact_view
#
# urlpatterns = [
#     path('faq/', faq_view, name='faq-page'),  # Renders FAQ page this is home page
#     path('api/faqs/', FAQListView.as_view(), name='faq-api'),  # API returns JSON
#     path('', faq_view, name='home'),  # Redirects root to FAQ page
#     path('insights/', insights_view, name='insights'),  # Add the insights URL pattern
#     path('contact/', contact_view, name='contact'),  # Add the insights URL pattern
#
# ]
from django.urls import path
from django.shortcuts import redirect
from .views import FAQListView, faq_view, insights_view, contact_view

urlpatterns = [
    path('', lambda request: redirect('/faq/')),  # Ensure the correct slash format
    path('faq/', faq_view, name='faq-page'),
    path('api/faqs/', FAQListView.as_view(), name='faq-api'),
    path('insights/', insights_view, name='insights'),
    path('contact/', contact_view, name='contact'),
]