# Generated by Django 3.2.6 on 2021-10-02 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_user_on_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='message',
            field=models.TextField(max_length=300),
        ),
    ]
