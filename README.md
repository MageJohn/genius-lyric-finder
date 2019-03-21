# Genius Lyrics for DeaDBeeF Infobar plugin

Simple lyrics plugin for the [DeaDBeef Infobar](https://bitbucket.org/dsimbiriatin/deadbeef-infobar/wiki/Home) plugin. All it does, however, is accept the artist and title of a song and print the lyrics to stdout, so it may be useful beyond this. It uses the Python package [LyricsGenius](https://github.com/johnwmillr/LyricsGenius) by John Miller.

## Installation

The dependencies are Python 3 and the `lyricsgenius` package. Unless you have a better way, install `lyricsgenius` like this:
```
sudo pip3 install lyricsgenius
```

Clone the git repository to wherever you want and cd into the new directory:
```
git clone https://github.com/MageJohn/genius-lyric-finder.git
cd genius-lyric-finder
```

You will also need an access token for the Genius API, for which you need a Genius account. Go to the [Genius API Client management page](http://genius.com/api-clients), login, give an arbitrary name and a website (a link here will do), and click Save. Now get the Client Access Token and paste it into a file named `access_token.txt` next to the script.

To use the plugin from the Infobar plugin mark the script as executable:
```
chmod +x genius-lyric-finder.py
```

Then go into the Infobar preferences and set the "Lyric script path" option to point to `genius-lyric-finder.py`. You may want to disable the other lyric sources to make sure the script is used.

## Usage

Using the script without the Infobar plugin is perfectly possible, though there's no command line interface to speak of. Just pass the name of the artist and the name of the song to the script. Extra arguments are ignored.

```
./genius-lyric-finder.py "Jethro Tull" "Broadsword"
```

The Infobar plugin encodes spaces with underscores, and so the script will replace underscores with spaces again; existing spaces are ignored.
