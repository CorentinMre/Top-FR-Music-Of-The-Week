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
## Example result of top 10 singles

```json
[
  {
    "rang": "1",
    "coverUrl": "https://images.music-story.com/img/album_/1752890--kmt.jpeg",
    "titre": "DIE",
    "artiste": "GAZO",
    "editeur": "BSB PROD",
    "rangPrecedent": "1er"
  },
  {
    "rang": "2",
    "coverUrl": "https://images.music-story.com/img/album_/1751806--fade-up.jpeg",
    "titre": "FADE UP",
    "artiste": "ZEG P",
    "editeur": "BELIEVE / ON DA TRAX",
    "rangPrecedent": "2e"
  },
  {
    "rang": "3",
    "coverUrl": "https://images.music-story.com/img/album_/1735240--calm-down.jpeg",
    "titre": "CALM DOWN",
    "artiste": "REMA",
    "editeur": "VIRGIN RECORDS FRANCE / VIRGIN RECORDS S&D",
    "rangPrecedent": "5e"
  },
  {
    "rang": "4",
    "coverUrl": "https://images.music-story.com/img/album_/1756745--petete.jpeg",
    "titre": "PETETE",
    "artiste": "GAMBI",
    "editeur": "WARNER / REC. 118",
    "rangPrecedent": "3e"
  },
  {
    "rang": "5",
    "coverUrl": "https://images.music-story.com/img/album_A/1747083-alonzo-quartiers-nord.jpeg",
    "titre": "TOUT VA BIEN",
    "artiste": "ALONZO",
    "editeur": "ONLY PRO",
    "rangPrecedent": "4e"
  },
  {
    "rang": "6",
    "coverUrl": "https://images.music-story.com/img/album_S/1748067-soolking-sans-visa.jpeg",
    "titre": "BALADER",
    "artiste": "SOOLKING",
    "editeur": "CAPITOL MUSIC FRANCE / CAPITOL",
    "rangPrecedent": "6e"
  },
  {
    "rang": "7",
    "coverUrl": "https://images.music-story.com/img/album_/1755693--doja.jpeg",
    "titre": "DOJA",
    "artiste": "CENTRAL CEE",
    "editeur": "WARNER / CENTRAL CEE",
    "rangPrecedent": "8e"
  },
  {
    "rang": "8",
    "coverUrl": "https://images.music-story.com/img/album_/1751797--chop-nouvelle-ecole.jpeg",
    "titre": "CHOP (NOUVELLE ÉCOLE)",
    "artiste": "FRESH",
    "editeur": "BELIEVE / ICB RECORDS",
    "rangPrecedent": "7e"
  },
  {
    "rang": "9",
    "coverUrl": "https://images.music-story.com/img/album_J/1748379-jul-extraterrestre.jpeg",
    "titre": "J'AI TOUT SU",
    "artiste": "JUL",
    "editeur": "BELIEVE / D'OR ET DE PLATINE",
    "rangPrecedent": "9e"
  },
  {
    "rang": "10",
    "coverUrl": "https://images.music-story.com/img/album_H/1740156-harry-styles-as-it-was",
    "titre": "AS IT WAS",
    "artiste": "HARRY STYLES",
    "editeur": "SONY MUSIC ENTERTAINMENT / COLUMBIA",
    "rangPrecedent": "10e"
  }
]
```