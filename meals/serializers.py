from rest_framework import serializers
from .models import Meal, Component, Label, Quantity

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class QuantitySerializer(serializers.ModelSerializer):
    component = ComponentSerializer()

    class Meta:
        model = Quantity
        fields = ('component', 'amount')

class MealSerializer(serializers.ModelSerializer):
    components = QuantitySerializer(source='quantity_set', many=True, read_only=True)
    labels = LabelSerializer(many=True)

    class Meta:
        model = Meal
        fields = '__all__'