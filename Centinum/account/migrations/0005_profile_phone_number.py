# Generated by Django 2.1.4 on 2019-07-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190710_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
