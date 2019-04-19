# -*- coding: utf-8 -*-
import requests
import os
from m4m_imu import *
from m4m_utils import *
from m4m_obd import *
from m4m_led import *
from m4m_gsm import *

print(cur_date(), "Power on\n")
#redOn()

#IMU START -> thread
imu_ev = threading.Event()
imu_t = threading.Thread(target=imu_connect, args=())
imu_t.do_run = True
imu_t.start()
imu_ev.set()

#GSM START
gsm_con = gsm_start()

#sim check

#eth check

#obd START
obd_con = obd_start()
#if not obd_con.is_connected():
	#gsm_sendSMS(gsm_con, PHONE, MSG_OBD_DISCONNECT_ENG)

mac = getMAC()
data = {}
lat, lon = 0, 0

#nginx START
os.system("sudo service nginx start") #?


#gsm_call(gsm_con, PHONE)
#beep()

try:
	while True:
	    if obd_con.is_connected():
	        data = obd_read(obd_con)
	        print(data)
	        json_send(mac, 8, data)

	    if gsm_con:
	        lat, lon = gsm_getGPS(gsm_con)
	        print(lat, ' ', lon)
	        json_send(mac, 7, {'lat': lat, 'lon': lon})

	    time.sleep(10)
except KeyboardInterrupt:
    if gsm_con != None:
        gsm_con.close()
finally:
	imu_t.do_run = False
	if gsm_con:
		gsm_con.close()
