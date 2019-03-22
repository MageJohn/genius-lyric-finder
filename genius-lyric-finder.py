#!/usr/bin/python3
import sys
import os.path
from urllib.parse import unquote
import lyricsgenius

ACCESS_TOKEN = "access_token.txt"

try:
    with open(os.path.join(os.path.dirname(__file__), ACCESS_TOKEN)) \
            as token_file:
        genius = lyricsgenius.Genius(token_file.readline().strip())
except FileNotFoundError:
    print("Couldn't find access token file {}".format(ACCESS_TOKEN))
    sys.exit(1)

genius.verbose = False
genius.remove_section_headers = False

if len(sys.argv) > 1:
    artist = unquote(sys.argv[1].replace('_', ' '))
else:
    print("No artist passed")
    sys.exit(2)

if len(sys.argv) > 2:
    title = unquote(sys.argv[2].replace('_', ' '))
else:
    print("No song title passed")
    sys.exit(3)

song = genius.search_song(title, artist)

if song:
    print(song.lyrics)
else:
    sys.exit(4)

sys.exit(0)
