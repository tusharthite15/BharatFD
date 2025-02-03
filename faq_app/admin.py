from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import FAQ
from .utils import translate_text  # Ensure this matches the file name and function

# Custom Admin Site
class NoAuthAdminSite(AdminSite):
    site_header = 'No Auth Admin'
    site_title = 'Admin Panel'

    def has_permission(self, request):
        # Allow all users to access the admin panel
        return True

# Create an instance of NoAuthAdminSite
admin_site = NoAuthAdminSite()

# Register your models to the custom admin site
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

    def save_model(self, request, obj, form, change):
        try:
            # Translate question and answer to Hindi and Bengali before saving
            obj.question_hi = translate_text(obj.question, 'hi')
            obj.question_bn = translate_text(obj.question, 'bn')
            obj.answer_hi = translate_text(obj.answer, 'hi')
            obj.answer_bn = translate_text(obj.answer, 'bn')
        except Exception as e:
            # Handle errors, you can log the error or provide fallback values
            print(f"Translation error: {e}")

        super().save_model(request, obj, form, change)

# Register only once
admin_site.register(FAQ, FAQAdmin)  # ✅ Corrected: Only one registration
