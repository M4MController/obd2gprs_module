# -*- coding: utf-8 -*-
import json
from datetime import datetime
from datetime import timezone
from gpiozero import Buzzer
from time import sleep

def getMAC():
    try:
        try:
            mac = open("/sys/class/net/ppp0/address").read()
        except:
            mac = open("/sys/class/net/eth0/address").read()
    except:
        mac = "00:00:00:00:00:00"
    return mac[0:17]

def json_send(mac, sensor_id, data):
    json_data = {
        "controller_mac": mac,
        "sensor_id": sensor_id,
        "value": json.dumps(data),
        "hash": "some hash here",
        "timestamp": datetime.now().replace(tzinfo=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    }
    #response = requests.post("https://receiver.meter4.me/sensor.addRecord", json=json_data)
    #print(response.status_code, response.json())

def cur_date():
    return datetime.now().replace(tzinfo=timezone.utc).strftime("%b %d %H:%M:%S m4m: ")


def beep():
    buzzer = Buzzer(17)
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
