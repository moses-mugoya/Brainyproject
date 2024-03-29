# Generated by Django 2.1.4 on 2019-07-05 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInvestments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invest_business', to='portal.StartupBusiness')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_business', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'BusinessInvestments',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='IdeaInvestments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invest_idea', to='portal.Ideas')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_idea', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'IdeaInvestments',
                'ordering': ('-created',),
            },
        ),
    ]
