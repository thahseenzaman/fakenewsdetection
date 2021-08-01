from django.db import models

# Create your models here.
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'
