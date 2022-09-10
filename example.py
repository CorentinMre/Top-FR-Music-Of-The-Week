
import snepAPI


snep = snepAPI.SNEP()

#Top Singles of the week
singlesList = snep.getSinglesList(nbRang=10) #MAX nbRang = 200
print(singlesList)

#Top Albums of the week
albumsList = snep.getAlbumsList(nbRang=10) #MAX nbRang = 200
print(albumsList)
