from django.db import models

# Create your models here.
class RegUser(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'reg_user'
