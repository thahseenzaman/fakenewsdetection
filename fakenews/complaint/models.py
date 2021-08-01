from django.db import models
from user.models import RegUser

class Complaint(models.Model):
    cid = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()

    complaint = models.CharField(max_length=20)
    replay = models.CharField(max_length=20)
    date = models.DateField()
    u=models.ForeignKey(RegUser,to_field='u_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'complaint'
