#!/bin/sh
# Start/stop the cron daemon.
#
### BEGIN INIT INFO
# Provides:          ppp0
# Required-Start:    $remote_fs $syslog $time
# Required-Stop:     $remote_fs $syslog $time
# Should-Start:      $network $named slapd autofs ypbind nscd nslcd winbind
# Should-Stop:       $network $named slapd autofs ypbind nscd nslcd winbind
# Default-Start:     2 3 4 5
# Default-Stop:
# Short-Description: Starts ppp0 interface as default.
### END INIT INFO

pppd call gprs &
ifconfig eth0 down
ifconfig wlan0 down
route add -net 0.0.0.0 ppp0
python3 /home/pi/obd2gprs_module/main.py &
