from django.http import HttpResponse
from .models import Album


def index(request):
    html = ""
    # get all the records in the album table
    all_ablum = Album.objects.all()
    for album in all_ablum:
        # url not add "music/" at beginning. relative path
        url = str(album.id) + "/"
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2>" + album_id + "</h2>")
