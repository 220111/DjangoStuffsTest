from django.db import models
from django.db.models.fields import Field

# Create your models here.

class List(models.Model):
    list_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.list_name

class ListItem(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.item_text

class SubListItem(models.Model):
    list = models.ForeignKey(ListItem, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.item_text