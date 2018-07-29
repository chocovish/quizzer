from django.db import models

# Create your models here.

class questions(models.Model):
    question = models.CharField(max_length=160)
    choice = models.CharField(max_length=200)
    answer = models.CharField(max_length=60)

    def __str__(self):
        return str(self.question)


class post(models.Model):
    title = models.CharField(max_length=30)
    published= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title