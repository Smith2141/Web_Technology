sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo rm /etc/nginx/sites-enabled/default 2> /dev/null
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test.conf
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start