#------------------------ boot database  ----------------------------------------
chmod 777 /var/www/localhost/cgi-bin/test.py
service fcgiwrap start
echo "Starting nginx";
nginx -g "daemon off;";
