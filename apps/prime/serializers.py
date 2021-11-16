from rest_framework import serializers


class PrimeNumberSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=2, max_value=100)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
