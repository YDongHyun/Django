from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True) #계정 삭제시 모든글 삭제
    subject = models.CharField(max_length=200) #제목의 최대 길이
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):  #제목을 str로 출력
        return self.subject

class Answer (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE) #Question을 모델 속성으로
    content = models.TextField()
    create_date = models.DateTimeField()

    #기존 모델을 속성으로 사용하기위해 ForeignKey(다른 모델과 연결)를 사용
    #on_delete=models.CASCADE 답변과 연결된 질문이 삭제되면 답변도 삭제된다.
    #파이보 앱 등록 ->setting
# Create your models here.
