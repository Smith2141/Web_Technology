sudo rm /etc/nginx/sites-enabled/default 2> /dev/null
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.py   /etc/gunicorn.d/test.py
#sudo rm /etc/gunicorn.d/default 2> /dev/null
#sudo /etc/init.d/mysql start

sudo gunicorn -c /home/box/web/etc/gunicorn.py hello:application
sudo gunicorn -c /home/box/web/etc/gunicorn-django.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart
