# from django.contrib.auth import get_user_model, authenticate
# from rest_framework import viewsets, permissions
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import UserSerializer
# from django.contrib.auth import authenticate, login
# from django.views import View
# from django.http import JsonResponse

from rest_framework import viewsets
from .models import Defaultuser, Subject, User_to_subject
from .serializers import DefaultUserSerializer, SubjectSerializer, UserToSubjectSerializer

class DefaultUserViewSet(viewsets.ModelViewSet):
    queryset = Defaultuser.objects.all()
    serializer_class = DefaultUserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class UserToSubjectViewSet(viewsets.ModelViewSet):
    queryset = User_to_subject.objects.all()
    serializer_class = UserToSubjectSerializer
