heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn thingspeakdata.wsgi:application --preload --log-file - 