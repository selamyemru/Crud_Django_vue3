from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        # Add validation to ensure the payload is not empty
        if not validated_data:
            raise serializers.ValidationError("Request payload cannot be empty.")

        # Proceed with creating the new instance
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Add validation to ensure the payload is not empty
        if not validated_data:
            raise serializers.ValidationError("Request payload cannot be empty.")

        # Proceed with updating the instance
        return super().update(instance, validated_data)