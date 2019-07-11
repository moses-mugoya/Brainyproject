from django.urls import re_path
from . import views


app_name = 'account'


urlpatterns = [
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^edit/$', views.edit, name='edit'),

]
