from django.db import models
from account.models import User
from django.urls import reverse
from datetime import datetime


class Ideas(models.Model):
    user = models.ForeignKey(User, related_name='user_ideas', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    personal = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Ideas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portal:idea_detail', args=[self.id])

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')


class StartupBusiness(models.Model):
    user = models.ForeignKey(User, related_name='user_startup', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length=250, blank=True)
    founding_date = models.DateField(null=True)
    tag_line = models.CharField(blank=True, max_length=250)
    pitch = models.TextField(blank=True)
    pitch_video_url = models.URLField(blank=True)
    customer_model = models.CharField(max_length=250, blank=True)
    country = models.CharField(max_length=250, blank=True)
    full_address = models.CharField(max_length=250, blank=True)
    stage = models.CharField(max_length=250, blank=True)
    sector = models.CharField(max_length=250, blank=True)
    personal = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'StartupBusinesses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portal:business_detail', args=[self.id])

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')


class IdeaInvestments(models.Model):
    idea = models.ForeignKey(Ideas, related_name='invest_idea', on_delete=models.CASCADE)
    investor = models.ForeignKey(User, related_name='user_idea', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'IdeaInvestments'

    def __str__(self):
        return 'Investment on {}'.format(self.idea)

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')


class BusinessInvestments(models.Model):
    business = models.ForeignKey(StartupBusiness, related_name='invest_business', on_delete=models.CASCADE)
    investor = models.ForeignKey(User, related_name='user_business', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'BusinessInvestments'

    def __str__(self):
        return 'Investment on {}'.format(self.business)

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')


class BusinessTeams(models.Model):
    business = models.ForeignKey(StartupBusiness, related_name='team_business', on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name='member_business', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'BusinessTeams'

    def __str__(self):
        return 'Joined Team for {}'.format(self.business)

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')


class IdeaTeams(models.Model):
    idea = models.ForeignKey(Ideas, related_name='team_idea', on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name='member_idea', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'IdeaTeams'

    def __str__(self):
        return 'Joined team for {}'.format(self.idea)

    def day_created(self):
        return self.created.strftime('%d')

    def month_created(self):
        return self.created.strftime('%b')
