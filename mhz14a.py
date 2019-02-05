import serial
import time
import sys
import datetime

class MHZ14A():
    packet = [0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79]
    zero = [0xff, 0x87, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf2]
    def __init__(self,ser="/dev/serial0"):
        self.serial = serial.Serial(ser,9600,timeout=5.0,interCharTimeout=0.0,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,dsrdtr=False)
        time.sleep(1)

    def get(self):
	self.serial.write(bytearray(self.packet))
	self.serial.read(size=9)
	time.sleep(0.5)
    self.serial.write(bytearray(self.packet))
	res = self.serial.read(size=9)
	res = bytearray(res)
	checksum = 0xff & (~(res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7])+1)
	if res[8] == checksum and (res[2]<<8)|res[3] > 0:
	    return '{0:s}\t{1:0.0f} C\t{2:0.0f} ppm'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), res[4]-40, (res[2]<<8)|res[3])
	else:
		return ""
    def close(self):
        self.serial.close


def main():
    while True:
	co2 = None
	try:
		co2 = MHZ14A()
        	print co2.get()
		co2.close()
    	except Exception as e:
        	print "Error: " + str(e)
		if co2 is not None:
			co2.close()
	time.sleep(60)

if __name__ == '__main__':
    main()
