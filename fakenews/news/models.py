from django.db import models
from user.models import RegUser
#
# Create your models here.
class News(models.Model):
    nid = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    news = models.CharField(max_length=40)
    date = models.CharField(max_length=50)
    img = models.CharField(max_length=1000)
    fake = models.CharField(max_length=50)
    status = models.IntegerField()

    u=models.ForeignKey(RegUser,to_field='u_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'news'
