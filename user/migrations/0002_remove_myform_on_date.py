# Generated by Django 3.2.6 on 2021-09-29 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myform',
            name='on_date',
        ),
    ]
