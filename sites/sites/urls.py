from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('sites/', views.site_list, name='siteList'),
    path('sitecreate/', csrf_exempt(views.site_create), name='siteCreate'),
]