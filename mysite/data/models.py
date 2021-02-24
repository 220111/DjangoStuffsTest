from django.db import connection, models
from django.db.models.fields.related import OneToOneField

# Create your models here.

class CollectedItem(models.Model):
    item_name = models.CharField(max_length=200)
    icon_image = models.ImageField(default="missing.png", upload_to='itemicons')
    detail_text = models.TextField(max_length=500, null=True)
    collect_date = models.DateField('date collected')
    related_item = models.ManyToManyField("self",blank=True,symmetrical=True)
    def __str__(self):
        return self.item_name