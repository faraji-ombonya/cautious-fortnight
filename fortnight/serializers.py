from rest_framework import serializers


class PredictSerializer(serializers.Serializer):
    age = serializers.FloatField()  # Change from IntegerField to FloatField
    sex = serializers.FloatField()
    cp = serializers.FloatField()
    trestbps = serializers.FloatField()
    chol = serializers.FloatField()
    fbs = serializers.FloatField()
    restecg = serializers.FloatField()
    thalach = serializers.FloatField()
    exang = serializers.FloatField()
    oldpeak = serializers.FloatField()
    slope = serializers.FloatField()
    ca = serializers.FloatField()
    thal = serializers.FloatField()

    def create(self, validated_data):
        """
        return the validated data
        """
        return validated_data
