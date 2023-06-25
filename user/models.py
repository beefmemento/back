from django.db import models
from django.contrib.auth.models import AbstractUser


# 다대 다 관계
class Defaultuser(AbstractUser):
    name = models.CharField(max_length=255, blank=False, primary_key=True)
    nickname = models.CharField(max_length=255, blank=False)
    major = models.CharField(max_length=255, blank=False)
    number = models.CharField(max_length=255, blank=False)

class Subject(models.Model): # 과목 릴레이션
    title = models.CharField(max_length=200, primary_key=True) # 과목 명
    professor = models.CharField(max_length=200) # 교수 이름
    code = models.CharField(max_length=200) # 과목 코드


    # def __str__(self):
    #     return f"{self.title} : {self.professor}"


class User_to_subject(models.Model): # 관계 릴레이션
    username = models.ForeignKey(Defaultuser, on_delete=models.CASCADE)
    subjectname = models.ForeignKey(Subject, on_delete=models.CASCADE)
