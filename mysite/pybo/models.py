from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)  #글자 수에 제한이 있고 200자로 제한함
    content = models.TextField() #글자 수에 제한이 없을 때
    create_date = models.DateTimeField() #날짜, 시간관련 속성일 때

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Foreign Key: 어떤 모델이 다른 모델을 속성으로 가질때
    # on_delete=models.CASCADE : 답변에 연결된 질문이 삭제되면 답변도 함께 삭제함.
    content = models.TextField()
    create_date = models.DateTimeField()
