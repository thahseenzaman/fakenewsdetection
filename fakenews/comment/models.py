from django.db import models
from user.models import RegUser
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    comment = models.CharField(max_length=20)
    date = models.DateField()


    class Meta:
        managed = False
        db_table = 'comment'
