#! /bin/sh

### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start sensors
### END INIT INFO

cd /home/pi/raspberrySensorOnlineChart && ./dht11-start.sh && ./mhz14a-start.sh
