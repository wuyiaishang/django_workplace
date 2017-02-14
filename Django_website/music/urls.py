from django.conf.urls import url
from . import views

urlpatterns = [
    # views.index means index function
    # ^ means start point $ means end point '^$' means nothing after 'music/'
    url(r'^$', views.index, name='index'),
]
