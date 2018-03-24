# importing django functions
from django.conf.urls import url
from . import views

# this is the url pattern
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
