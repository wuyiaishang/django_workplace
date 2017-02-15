from django.db import models


class Album(models.Model):
    # variable name must be the column name
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # similar with toString(), also show in the admin interface
    def __str__(self):
        return self.artist + '-' + self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    # similar with toString(), also show in the admin interface
    def __str__(self):
        return self.album + '-' + self.song_title
