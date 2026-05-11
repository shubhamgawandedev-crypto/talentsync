from django.db import models
from users.models import User


class Job(models.Model):

    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    salary = models.CharField(max_length=100)

    skills = models.TextField()

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title