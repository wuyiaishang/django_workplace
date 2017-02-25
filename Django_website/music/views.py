from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album

'''
# This method should add --- from django.template import loader
def index(request):
    # get all the records in the album table
    all_ablum = Album.objects.all()

    # serching the file under the templates folder
    template = loader.get_template('music/index.html')

    # add data/parameter to index.html
    context = {
        'all_album': all_ablum,
    }

    # pass the data set above
    return HttpResponse(template.render(context, request))
    '''


# the second method (using shortcut), clean code  --- from django.shortcuts import render
def index(request):
    all_ablum = Album.objects.all()
    context = {
        'all_album': all_ablum,
    }
    return render(request, 'music/index.html', context)

    '''
    # html code is nested with python code, which is not recommended.
    html = ""
    for album in all_ablum:
        # url not add "music/" at beginning. relative path
        url = str(album.id) + "/"
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)
    '''


def detail(request, album_id):
    # deal with 404 error
    '''
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album not exit")
    '''
    # using following codes to replace the above one

    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

    # return HttpResponse("<h2>" + album_id + "</h2>")


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        # according to the value of radio(song) to get song object
        select_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You didn't select valid song",
        })
    else:
        select_song.is_favorite = True
        select_song.save()
        return render(request, 'music/detail.html', {'album': album})
