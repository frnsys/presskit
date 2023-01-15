Dependencies:

```
pip install click==8.0.4 PyYAML=5.4 Jinja2==3.1.2
```

Command:

```
python build.py path/to/config.yml path/to/assets path/to/output
```

Config description:

```
title: game title
meta:
  description: description for social media/search engine embeds
  image: path to social media embed image
  url: url that you will upload the press kit HTML file to
header:
  image: path to header image
  alt: alt text for the header image
release_date: when the game was released
platforms:
  - name: platform name
    url: url to game on platform
languages: (optional)
  - optional listing of languages
prices:
  - list of prices in different currencies
website: main game website
about:
  SectionName: different sections describing the game
  ListName:
    - can also
    - have lists of text
videos:
  - title: video title
    url: youtube url
images:
  - title: image title
    url: path to imgae
press: (optional)
  articles: (optional)
    - title: article title
      url: article url
      publication: article publication
      author: article author
      quote: optional quote
  awards: (optional)
    - name: award name
      url: url to the award site
      image: optional award image
      year: award year
developers:
  - name: developer/studio name
    url: developer/studio url
    description: developer/studio description
    socials:
      - name: social platform name
        url: social media url
    logos:
      - path to logos (e.g. for light/dark variants)
credits:
  SectionName:
    - name: name
      url: optional url
streaming_ok: boolean, whether or not to give streamers permission to use gameplay footage
```