from django.conf.urls import url
from . import views


# using namespace, so that the html can get the below urls in the correct app/section
app_name = 'music'

urlpatterns = [
    # views.index means index function
    # ^ means start point $ means end point '^$' means nothing after 'music/'

    # music/
    url(r'^$', views.index, name='index'),

    # music/<album_id>/ identify integer   P followed by parameter that go to view.py  after that is reg-ex
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),

    # music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),

]
