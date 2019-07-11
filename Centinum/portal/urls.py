from django.urls import re_path
from . import views

app_name = 'portal'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^home/all/ideas/', views.home, name='home'),
    re_path(r'^home/all/business/startups/', views.home_biz, name='home_biz'),
    re_path(r'investor/business', views.investor, name='investor'),
    re_path(r'investor/idea/', views.investor_idea, name='investor_idea'),
    re_path(r'entrepreneur/', views.entrepreneur, name='entrepreneur'),
    re_path(r'innovator/', views.innovator, name='innovator'),
    re_path(r'investments/business/', views.investments_business, name='investment_biz'),
    re_path(r'investments/', views.investments, name='investments'),
    re_path('^add/idea/', views.add_idea, name='add_idea'),
    re_path('^add/business/startup/', views.add_business, name='add_business'),
    re_path(r'^edit/business/(?P<id>\d+)/', views.edit_business, name='edit_business'),
    re_path('^add/idea/', views.add_idea, name='add_idea'),
    re_path(r'^edit/idea/(?P<id>\d+)/', views.edit_idea, name='edit_idea'),
    re_path(r'^(?P<id>\d+)/idea/detail/', views.idea_detail, name='idea_detail'),
    re_path(r'^(?P<id>\d+)/business/detail/', views.business_detail, name='business_detail'),
    re_path(r'^(?P<id>\d+)/idea/invest/', views.invest_idea, name='idea_invest'),
    re_path(r'^(?P<id>\d+)/business/invest/', views.invest_business, name='invest_business'),
    re_path(r'^(?P<id>\d+)/idea/join/', views.join_idea, name='join_idea'),
    re_path(r'^(?P<id>\d+)/business/join/', views.join_business, name='join_business'),
    re_path(r'terms/conditions/', views.terms, name='terms'),
    re_path(r'privacy/', views.privacy, name='privacy'),

]
