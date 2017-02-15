from django.conf.urls import url
from . import views

urlpatterns = [
    # views.index means index function
    # ^ means start point $ means end point '^$' means nothing after 'music/'

    # music/
    url(r'^$', views.index, name='index'),

    # music./231/ identify integer   P followed by parameter that go to view.py  after that is reg-ex
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

]
