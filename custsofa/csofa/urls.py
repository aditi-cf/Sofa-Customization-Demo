from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^arm_all', views.arm_all, name='arm_all'),
    url(r'^arm_color_all', views.arm_color_all, name='arm_color_all'),
    url(r'^leg_all', views.leg_all, name='leg_all'),
    url(r'^leg_color_all', views.leg_color_all, name='leg_color_all'),
    url(r'^back_all', views.back_all, name='back_all'),
    url(r'^back_color_all', views.back_color_all, name='back_color_all'),
    url(r'^pipe_all', views.pipe_all, name='pipe_all'),
    url(r'^pipe_color_all', views.pipe_color_all, name='pipe_color_all'),
    url(r'^1$', views.index1, name='index1'),
]

