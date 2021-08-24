from django.db import models

# table의 모델 단, UserID가 문자열로서 사용되게 변경
class Board(models.Model):
    index = models.AutoField(primary_key=True)
    UserID = models.CharField(max_length=15)
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    #Hit = models.IntegerField(null=True)
    #Success_per = models.IntegerField(null=True)
    Reg_date = models.DateTimeField(null=True)

class Judge_State(models.Model):
    submit_idx = models.IntegerField()
    UserID = models.CharField(max_length=15)
    States = models.CharField(max_length=5) #perhaps true false?
    Memory_use = models.IntegerField()
    Time_Complex = models.IntegerField()
    Submission_Time = models.DateTimeField()

class User_Table(models.Model):
    UserID = models.CharField(max_length=15)
    PW = models.CharField(max_length=32)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)

class Code_History(models.Model):
    index = models.AutoField(primary_key=True)
    UserID = models.CharField(max_length=15)
    Board_idx = models.IntegerField()
    answer = models.TextField()