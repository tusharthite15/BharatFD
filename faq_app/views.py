from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from .models import FAQ
from django.conf import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 1500)  # Default TTL of 25 minutes

# Template View with Cache
@cache_page(CACHE_TTL)  # Cache the page for the defined TTL
def faq_view(request):
    return render(request, 'faq.html')

def insights_view(request):
    return render(request, 'insights.html')

def contact_view(request):
    return render(request, 'contact.html')

# API View for FAQ data
class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')
        faqs = FAQ.objects.all().distinct()
        data = []
        for faq in faqs:
            data.append({
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            })
        return Response(data)
