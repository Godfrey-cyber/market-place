# auth_app/views.py
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, LoginSerializer
from django.shortcuts import render
import jwt

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            response = Response({'msg': 'Login successful'})
            response.set_cookie(key='token', value=token, httponly=True, samesite='None', secure=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
