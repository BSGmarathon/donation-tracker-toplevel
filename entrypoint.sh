#!/bin/sh
python manage.py migrate --noinput

# Make the folder where we are going to store the fonts
mkdir -p /var/www/html/static/res/fonts || true
#
## Collect the fonts we need for the tracker from the GDQ website if they are missing in the volume
#for font in 'cubano-regular-webfont.eot' 'cubano-regular-webfont.woff' 'cubano-regular-webfont.ttf' 'cubano-regular-webfont.svg' \
# 'MuseoSans_700-webfont.eot' 'MuseoSans_700-webfont.woff' 'MuseoSans_700-webfont.ttf' 'MuseoSans_700-webfont.svg' \
# 'MuseoSans_300-webfont.eot' 'MuseoSans_300-webfont.woff' 'MuseoSans_300-webfont.ttf' 'MuseoSans_300-webfont.svg' \
# 'MuseoSans_300_Italic-webfont.eot' 'MuseoSans_300_Italic-webfont.woff' 'MuseoSans_300_Italic-webfont.ttf' 'MuseoSans_300_Italic-webfont.svg' ;
#  do
#    if [ ! -f "/var/www/html/static/res/fonts/$font" ]; then
#      echo "https://tracker.gamesdonequick.com/static/res/fonts/$font"
#      curl "https://tracker.gamesdonequick.com/static/res/fonts/$font" -o "/var/www/html/static/res/fonts/$font"
#    fi
#  done

# Copy over the fonts from what we downloaded before
cp -r /var/www/html/fonts /var/www/html/static/res

# Remove the already stored generated files, or ignore
rm -rf /var/www/html/static/gen || true

# Collect all the static assets
python manage.py collectstatic --noinput

if [ -x "$(command -v daphne)" ]; then
    echo "Using daphne server"
  daphne -b 0.0.0.0 -p 8000 tracker_development.asgi:application
elif [ -x "$(command -v gunicorn)" ]; then
    echo "Using gunicorn server (pls use daphne)"
    gunicorn --bind 0.0.0.0:8000 tracker_development.wsgi
else
    echo "Daphne and Gunicorn not installed: Using built-in server."
    python manage.py runserver 0.0.0.0:8000
fi