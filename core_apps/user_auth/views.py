from django.http import JsonResponse
from django.views import View
from loguru import logger

class TestLoggingView(View):
    def get(self, request):
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
        return JsonResponse({'message': 'Logging test done with loguru!'})

# Create your views here.
