<p align="center"><img width="250" alt="CSGO Statistics" src="img/logo.png"></p>

<br/>


<h2 align="center">Top FR Music Of The Week</h2>
<br/>

<br/>

## Requirements

- Install requirements (`pip install -r requirements.txt`)

## Usage

Here is an example script:

```python
import snepAPI


snep = snepAPI.SNEP()

#Top Singles of the week
singlesList = snep.getSinglesList(nbRang=10) #MAX nbRang = 200
print(singlesList)

#Top Albums of the week
albumsList = snep.getAlbumsList(nbRang=10) #MAX nbRang = 200
print(albumsList)

```
