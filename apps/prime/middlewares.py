from django.http import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.prime import exceptions


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # noinspection PyMethodMayBeStatic
    def process_exception(self, _, exception):
        if isinstance(exception, exceptions.DividedException):
            return JsonResponse({"error": str(exception)}, status=HTTP_400_BAD_REQUEST)
