from django.core.wsgi import get_wsgi_application
from vercel_wsgi import make_lambda_handler

application = get_wsgi_application()
handler = make_lambda_handler(application)
