from django.db import models

# Create your models here.
class Pr(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    request = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'pr'
