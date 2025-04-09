from django.db import models

# Create your models here.
# django has support for ORM-Object Relational Mapping,
# means we can use python code to define databases

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

