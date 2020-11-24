from rest_framework import serializers

from api.models import Todo, Category
from django.contrib.auth.models import User

# serializer classes 
class TodoSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Todo
        fields = ['name', 'pub_date', 'category', 'owner']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    Todo= serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'Todo']