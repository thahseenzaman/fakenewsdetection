from django.db import models
from user.models import RegUser
# Create your models here.
class Friends(models.Model):
    # u_id = models.IntegerField()
    friend_id = models.IntegerField()
    status = models.CharField(max_length=20)
    u=models.ForeignKey(RegUser,to_field='u_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'friends'

