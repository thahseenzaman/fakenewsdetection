from django.db import models
from user.models import RegUser
# Create your models here.
class Feedback(models.Model):
    id= models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    feedback = models.CharField(max_length=20)
    date = models.DateField()
    u=models.ForeignKey(RegUser,to_field='u_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feedback'
