# Generated by Django 3.1.3 on 2021-04-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('feedback', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'feedback',
                'managed': False,
            },
        ),
    ]
