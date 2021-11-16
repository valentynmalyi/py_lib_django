from rest_framework.response import Response
from rest_framework import views

from apps.prime import serializers


class PrimeNumber(views.APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request, n):
        serializer = serializers.PrimeNumberSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)

        return Response(data={"data": None})
