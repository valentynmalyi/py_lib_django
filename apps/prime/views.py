from rest_framework.response import Response
from rest_framework import views

from apps.prime import serializers
from pylib_libs import divided_by_2_3


class PrimeNumber(views.APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request, n):
        serializer = serializers.PrimeNumberSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)
        if divided_by_2_3.utils.is_divided_by_2(n):
            return Response(data={"error": f"Число {n} делиться на 2"})

        return Response(data={"status": "ok"})
