from faq_project.wsgi import application  # Replace with your project name
from vercel_wsgi import handle_wsgi

def handler(event, context):
    return handle_wsgi(application, event, context)
