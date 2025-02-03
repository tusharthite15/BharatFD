from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField(unique=True)  # Ensure questions are unique
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        if lang == 'hi':
            return self.question_hi or self.question
        elif lang == 'bn':
            return self.question_bn or self.question
        return self.question

    def get_translated_answer(self, lang='en'):
        if lang == 'hi':
            return self.answer_hi or self.answer
        elif lang == 'bn':
            return self.answer_bn or self.answer
        return self.answer