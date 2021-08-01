# Generated by Django 3.1.3 on 2021-04-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('friend_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'friends',
                'managed': False,
            },
        ),
    ]