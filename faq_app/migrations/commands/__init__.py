from django.core.management.base import BaseCommand
from faq_app.models import FAQ

class Command(BaseCommand):
    help = 'Add sample FAQs to the database'

    def handle(self, *args, **kwargs):
        FAQs = [
            {
                "question": "What is the payment platform?",
                "answer": "The payment platform is a secure system that allows users to make online transactions, manage subscriptions, and process payments seamlessly.",
                "question_hi": "भुगतान प्लेटफॉर्म क्या है?",
                "answer_hi": "भुगतान प्लेटफॉर्म एक सुरक्षित सिस्टम है जो उपयोगकर्ताओं को ऑनलाइन लेनदेन करने, सदस्यता प्रबंधित करने और भुगतान को सुचारु रूप से संसाधित करने की सुविधा देता है।",
                "question_bn": "পেমেন্ট প্ল্যাটফর্ম কি?",
                "answer_bn": "পেমেন্ট প্ল্যাটফর্ম হল একটি নিরাপদ সিস্টেম যা ব্যবহারকারীদের অনলাইন লেনদেন করতে, সদস্যতা পরিচালনা করতে এবং পেমেন্ট সহজে প্রক্রিয়া করতে সক্ষম করে।"
            },
            {
                "question": "How do I make a payment?",
                "answer": "To make a payment, log in to your account, select the service or product you wish to pay for, and follow the prompts to complete the transaction securely.",
                "question_hi": "मैं भुगतान कैसे करूं?",
                "answer_hi": "भुगतान करने के लिए, अपने खाते में लॉगिन करें, उस सेवा या उत्पाद का चयन करें जिसके लिए आप भुगतान करना चाहते हैं, और सुरक्षित रूप से लेनदेन पूरा करने के लिए संकेतों का पालन करें।",
                "question_bn": "আমি কীভাবে পেমেন্ট করব?",
                "answer_bn": "পেমেন্ট করতে, আপনার অ্যাকাউন্টে লগইন করুন, আপনি যে সেবা বা পণ্যটির জন্য পেমেন্ট করতে চান তা বেছে নিন এবং লেনদেনটি সুরক্ষিতভাবে সম্পন্ন করতে নির্দেশাবলী অনুসরণ করুন।"
            },
            # Add more FAQs here...
        ]

        for faq_data in FAQs:
            FAQ.objects.create(**faq_data)

        self.stdout.write(self.style.SUCCESS('Successfully added FAQs'))