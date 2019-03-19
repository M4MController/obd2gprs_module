import serial
import time

def get_location(data):
    idx = data.find(b'V')

    if idx == -1:
        idx = data.find(b'A')
        lat_deg = int(data[idx+2:idx+4])
        lat_remainder = data[idx+4:idx+13]
        lon_deg = int(data[idx+16:idx+19])
        lon_remainder = data[idx+19:idx+28]
        lat = lat_deg + float(lat_remainder) / 60
        lon = lon_deg + float(lon_remainder) / 60
        return lat, lon
    else:
        return 0, 0

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

port.write('AT+CGNSPWR=1\r\n'.encode('utf-8'))
rcv = port.read(100)
print(rcv)

port.write('AT+CGNSIPR=115200\r\n'.encode('utf-8'))
rcv = port.read(100)
print(rcv)

port.write('AT+CGNSTST=1\r\n'.encode('utf-8'))
rcv = port.read(100)
print(rcv)

port.write('AT+CGNSINF\r\n'.encode('utf-8'))
rcv = port.read(200)
print(rcv)

while True:
    fd = port.read(200)

    if b'$GNRMC' in fd:
        idx = fd.find(b'$GNRMC')
        dif = len(fd) - idx
        data, fd1 = b'', b''
        
        if dif < 46:
            fd1 = port.read(200)
            data = fd[idx:] + fd1[:46-dif]
        else:
            data = fd[idx:idx+46]

        print(get_location(data))
        time.sleep(5)
