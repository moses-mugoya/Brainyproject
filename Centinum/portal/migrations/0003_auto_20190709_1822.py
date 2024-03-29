# Generated by Django 2.1.4 on 2019-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_businessinvestments_ideainvestments'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupbusiness',
            name='company_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='startupbusiness',
            name='customer_model',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='startupbusiness',
            name='founding_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='startupbusiness',
            name='pitch',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='startupbusiness',
            name='pitch_video_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='startupbusiness',
            name='tag_line',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
