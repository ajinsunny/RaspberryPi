import serial, time, io
from datetime import datetime as dt
port = "/dev/pts/1"
ser = serial.Serial(port, 115200)
sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser,1), encoding = 'ascii')

time.sleep(.5)
print("Started: Waiting on Data")
sio.write(unicode("Started: Waiting on Data\r"))
sio.flush()

while True:
    data = sio.readline()
    print (data.rstrip('\r\n')) 


ser.close()


