from django.db import models

# Create your models here.


class AuthUser(models.Model):
    
    user_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    phone_number = models.IntegerField(unique=True, null=True)
    date_joined = models.DateTimeField("Date of joining")
    is_active = models.BooleanField(default=False)
    address = models.CharField(null=True, max_length=100)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)


class PortalQuestion(models.Model):

    ques_id = models.AutoField(primary_key=True, null=False)
    text = models.CharField(max_length=500, null=False)
    timestamp = models.DateTimeField("Date Question is Published")
    deadline = models.DateTimeField("Date to be Answered Within")
    asked_by_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    is_recommended = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ques_id)


class PortalRecommendation(models.Model):

    recommendation_id = models.AutoField(primary_key=True, null=False)
    ques_id = models.ForeignKey(PortalQuestion, on_delete=models.CASCADE)
    by_id = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    recommendation_answer = models.CharField(max_length=500, null=False)

    def __str__(self):
        return  str(self.recommendation_id)


class Department(models.Model):

    department_id = models.AutoField(primary_key=True, null=False)
    department_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return  str(self.department_name)

    
class AuthViewer(models.Model):
    
    authid = models.AutoField(primary_key=True, null=False)
    question_id = models.ForeignKey(PortalQuestion, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
