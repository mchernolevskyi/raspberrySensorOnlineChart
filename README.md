# raspberrySensorOnlineChart
Display online charts for data from sensors on Raspberry Pi quickly and easily.

To quickly launch do the following:

1. cd to the folder with dht11.py
2. Ensure Apache is running on Raspberry Pi
3. sudo mkdir /var/www/html/dht11
4. sudo chmod 777 /var/www/html/dht11
5. cp dht11/chart.html /var/www/html/dht11
5. nohup python -u dev/dht11.py > /var/www/html/dht11/data.txt &
6. Point your browser to http://raspberry/dht11/chart.html
7. Enjoy :)

You can also start SimpleHttpServer, Nginx, etc. and reuse existing project folder dht11/ with chart.html.
