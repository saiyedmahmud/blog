# Generated by Django 3.2.6 on 2021-10-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='on_date',
            field=models.DateField(auto_created=True),
        ),
    ]
