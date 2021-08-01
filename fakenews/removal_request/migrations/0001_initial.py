# Generated by Django 3.1.3 on 2021-04-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemovalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('request', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'removal_request',
                'managed': False,
            },
        ),
    ]
