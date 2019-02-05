# raspberrySensorOnlineChart
Display online charts for data from sensors on Raspberry Pi quickly and easily.

To quickly launch do the following:

0. git clone while in /home/pi
1. cd raspberrySensorOnlineChart
2. Ensure Apache is running on Raspberry Pi
3. sudo cp -r sensor /var/www/html
4. sudo chmod 777 /var/www/html/sensor
5. sudo cp start-sensor.sh /etc/init.d
6. sudo chmod 755 /etc/init.d/start-sensor.sh
7. sudo update-rc.d start-sensor.sh defaults
8. sudo reboot :) (or start /etc/init.d/start-sensor.sh manually)
9. Point your browser to http://raspberryPi/sensor/dht11.html or http://raspberryPi/sensor/mhz14a.html

You can also start SimpleHttpServer, Nginx, etc. and reuse existing project folder sensor with chart HTML files.
