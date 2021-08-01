from django.db import models
from news.models import News
from user.models import RegUser
# Create your models here.


class Report(models.Model):
    n_u_id = models.IntegerField()
    date = models.DateField()
    reason = models.CharField(max_length=50)
    time = models.TimeField()
    status = models.CharField(max_length=50)
    n=models.ForeignKey(News,to_field='nid',on_delete=models.CASCADE)
    u=models.ForeignKey(RegUser,to_field='u_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'report'

