#!/usr/bin/python

import serial
from time import sleep

port = serial.Serial('/dev/ttyUSB0')
port.setDTR(True)

while True:
	choice = raw_input('on | off | daemon | quit: ')
	if choice == 'on':
		port.setDTR(False)
	elif choice == 'off':
		port.setDTR(True)
	elif choice == 'quit':
		port.close()
		quit()
