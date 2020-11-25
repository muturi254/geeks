from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth.models import User

from api.models import Todo, Category
from api.serializers import TodoSerializer, CategorySerializer, UserSerializer, UserCreationSerializer, LogOutSerializer

# Create your views here.
class TasksView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreation(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    
class SignOut(generics.CreateAPIView):
    serialialzer_class = LogOutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serialialzer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = request.data.get('refresh_token')
        success_messsage = {"success": "User is successfull logged out"}
        error_message = {"error": "Token is invalid or expired"}

        try:
            token = RefreshToken(token)
            token.blacklist()
        except TokenError as error:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        return Response(success_messsage, status=status.HTTP_200_OK)

