from rest_framework import serializers

from apps.prime import validators


class PrimeNumberSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=2, max_value=100)

    class Meta:
        extra_kwargs = {
            "n": {
                "validators": (validators.is_prime_validate,)
            }
        }

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
