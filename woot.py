#!/usr/bin/python

# This script toggles the DTE pin of a serial port
# this pin currently drives a relay to turn on/off
# these rotating lights in Mickey's office during
# a woot-off on woot.com

import serial

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
