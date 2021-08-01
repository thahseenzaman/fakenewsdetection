# Generated by Django 3.1.3 on 2021-04-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
    ]