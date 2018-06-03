export DJANGO_SECRET_KEY='-&&(*q*sr4n7_f7dnt_cy-3z5kl5)x!@ercssp*3*k58-jojs2'
export DJANGO_DEBUG=''
DJANGO_SETTINGS_MODULE=locallibrary.prodsettings gunicorn -b 127.0.0.1:8200 locallibrary.wsgi:application
