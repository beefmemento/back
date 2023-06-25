from django.db import models
from user.models import Defaultuser

class Post(models.Model):
    title = models.CharField(max_length=200) # 과목 명
    content = models.TextField(blank=True) # 한 줄 소개
    semester = models.CharField(max_length=20)   # 수강한 학기
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00) # 받은 학점
    professor = models.CharField(max_length=255)  # 교수이름
    created_at = models.DateTimeField(auto_now_add=True) # 게시물 작성 날짜
    updated_at = models.DateTimeField(auto_now=True) # 수정날짜
    
    mentor = models.ForeignKey(Defaultuser, on_delete=models.CASCADE) # 연결하는 FK
