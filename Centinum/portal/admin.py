from django.contrib import admin
from .models import StartupBusiness, Ideas, BusinessInvestments, IdeaInvestments, IdeaTeams, BusinessTeams


class StartAppAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'created', 'modified', 'personal', 'company_name', 'customer_model', 'pitch_video_url']
    list_filter = ['user', 'created']


admin.site.register(StartupBusiness, StartAppAdmin)


class IdeasAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'personal', 'created', 'modified']
    list_filter = ['user', 'created']


admin.site.register(Ideas, IdeasAdmin)


class AdminIdeaInvestments(admin.ModelAdmin):
    list_display = ['idea', 'investor', 'created', 'modified', 'approved']
    list_editable = ['approved']
    list_filter = ['idea', 'approved', 'investor']


admin.site.register(IdeaInvestments, AdminIdeaInvestments)


class AdminBusinessInvestments(admin.ModelAdmin):
    list_display = ['business', 'investor', 'created', 'modified', 'approved']
    list_editable = ['approved']
    list_filter = ['business', 'approved', 'investor']


admin.site.register(BusinessInvestments, AdminBusinessInvestments)


class AdminBusinessTeams(admin.ModelAdmin):
    list_display = ['business', 'member', 'created', 'modified']
    list_filter = ['business',  'member']


admin.site.register(BusinessTeams, AdminBusinessTeams)


class AdminIdeaTeams(admin.ModelAdmin):
    list_display = ['idea', 'member', 'created', 'modified']
    list_filter = ['idea',  'member']


admin.site.register(IdeaTeams, AdminIdeaTeams)

