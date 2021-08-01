from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'image'
