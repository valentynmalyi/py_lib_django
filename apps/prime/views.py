from rest_framework.response import Response
from rest_framework import views


class PrimeNumber(views.APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request, n):
        return Response(data={"is_prime": False})
