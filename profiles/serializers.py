from rest_framework import serializers
from .models import CustomUser, Subscription

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username') 
        
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже используется.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Имя пользователя занято.")
        return value

class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all(),
        default=serializers.CurrentUserDefault() 
    )
    
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=CustomUser.objects.all()
    )

    class Meta:
        model = Subscription
        fields = ('subscriber', 'author') 
        
    # Валидация против самоподписки:
    def validate(self, data):
        if data['subscriber'] == data['author']:
            raise serializers.ValidationError("Нельзя подписаться на самого себя.")
        return data