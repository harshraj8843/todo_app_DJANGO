from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(default='', max_length=100)
    last_date = models.DateField(default='01/01/2001', auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class Done(models.Model):
    name = models.CharField(default='', max_length=100)
    last_date = models.DateField(default='01/01/2001', auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name