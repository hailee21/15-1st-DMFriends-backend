# Generated by Django 3.1.4 on 2020-12-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_member_random_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='random_token',
            field=models.IntegerField(),
        ),
    ]
