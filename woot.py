#!/usr/bin/python

# This script toggles the DTE pin of a serial port
# this pin currently drives a relay to turn on/off
# these rotating lights in Mickey's office during
# a woot-off on woot.com

import serial
import urllib
import re
import time
import platform

if platform.system() == 'Linux':
	port = serial.Serial('/dev/ttyUSB0')
else:
	port = serial.Serial('COM3')

port.setDTR(False)

while True:
	woot = urllib.urlopen('http://woot.com').read()
	match = re.search('lights.gif', woot)
	if match:
		print "wootoff detected"
		port.setDTR(True)
	else:
		print "no wootoff detected"
		port.setDTR(False)
	time.sleep(60*5) # Sleep for 5 minutes
