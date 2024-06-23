#!/bin/sh

for font in 'cubano-regular-webfont.eot' 'cubano-regular-webfont.woff' 'cubano-regular-webfont.ttf' 'cubano-regular-webfont.svg' \
 'MuseoSans_700-webfont.eot' 'MuseoSans_700-webfont.woff' 'MuseoSans_700-webfont.ttf' 'MuseoSans_700-webfont.svg' \
 'MuseoSans_300-webfont.eot' 'MuseoSans_300-webfont.woff' 'MuseoSans_300-webfont.ttf' 'MuseoSans_300-webfont.svg' \
 'MuseoSans_300_Italic-webfont.eot' 'MuseoSans_300_Italic-webfont.woff' 'MuseoSans_300_Italic-webfont.ttf' 'MuseoSans_300_Italic-webfont.svg' ;
  do
    if [ ! -f "/var/www/html/static/res/fonts/$font" ]; then
      echo "https://tracker.gamesdonequick.com/static/res/fonts/$font"
      curl "https://tracker.gamesdonequick.com/static/res/fonts/$font" -o "./fonts/$font"
    fi
  done