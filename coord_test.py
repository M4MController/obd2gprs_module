import serial

str_data = b'$GNRMC,1112845.000,A,5547.326349,N,03747.585533,E,0.00,93.83,190319,,,A*49'

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

print(get_location(str_data))

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1)

port.write('AT+CGNSPWR=1\r\n'.encode('utf-8'))
rcv = port.read(100)
print(rcv)

port.write('AT+CGNSIPR=115200'+'\r\n'.encode('utf-8'))
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

    if '$GNRMC' in fd:
        idx = fd.find('$GNRMC')
        dif = len(fd) - idx
