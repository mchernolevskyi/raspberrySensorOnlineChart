# raspberrySensorOnlineChart
Display online charts for data from sensors on Raspberry Pi quickly and easily.

To quickly launch do the following:

1. cd to the folder with dh11.py
2. Ensure Apache is running on Raspberry Pi
3. sudo mkdir /var/www/html/dh11
4. sudo chmod 777 /var/www/html/dh11
5. cp dh11/chart.html /var/www/html/dh11/chart.html
5. nohup python -u dev/dh11.py > /var/www/html/dh11/data.txt &
6. Point your browser to http://raspberry/dh11/chart.html
7. Enjoy :)

You can also start SimpleHttpServer, Nginx, etc. and you existing project dh11/ folder to view chart.html.
