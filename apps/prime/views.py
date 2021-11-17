from rest_framework.response import Response
from rest_framework import views, status

from apps.prime import serializers
from pylib_libs import divided_by_2_3, divided_by_5_7


class PrimeNumber(views.APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request, n):
        serializer = serializers.PrimeNumberSerializer(data={"n": n})
        try:
            serializer.is_valid(raise_exception=True)
        except (divided_by_2_3.exceptions.DividedException, divided_by_5_7.exceptions.DividedException) as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={"status": "ok"})
