from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_translation_methods(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            question_hi="डजांगो क्या है?",
            answer_hi="डजांगो एक वेब फ्रेमवर्क है।"
        )
        self.assertEqual(faq.get_translated_question('hi'), "डजांगो क्या है?")
        self.assertEqual(faq.get_translated_answer('hi'), "डजांगो एक वेब फ्रेमवर्क है।")