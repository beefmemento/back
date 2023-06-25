from rest_framework import serializers
from .models import Defaultuser, Subject, User_to_subject

class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defaultuser
        fields = ['username', 'name', 'nickname', 'major', 'number']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title', 'professor', 'code']

from rest_framework import serializers

class UserToSubjectSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', queryset=Defaultuser.objects.all())
    subjectname = serializers.SlugRelatedField(slug_field='title', queryset=Subject.objects.all())

    class Meta:
        model = User_to_subject
        fields = ['username', 'subjectname']


