from rest_framework import serializers
from pylib_libs import divided_by_2_3


class PrimeNumberSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=2, max_value=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    # noinspection PyMethodMayBeStatic
    def validate_n(self, n: int):
        divided_by_2_3.utils.is_divided(n)
