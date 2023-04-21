# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:21:15 2023

@author: Administrator
"""

import serial #import module
import time
ser = serial.Serial(port="COM4", baudrate=9600, bytesize=8, timeout=1) #open serial port
#ser.write("q7h10d\r\n".encode('utf-8')) #type of syringe
#ser.write("q7h12d\r\n".encode('utf-8')) #unit of the speed
#ser.write("q57h10d\r\n".encode('utf-8')) #type of syringe
#ser.write("q57h12d\r\n".encode('utf-8'))
ser.write("q1h3d\r\n".encode('utf-8')) #speed(integer digit)---ID0
ser.write("q2h00d\r\n".encode('utf-8')) #speed(decimal place) –ID0
ser.write("q51h3d\r\n".encode('utf-8')) #ID5
ser.write("q52h00d\r\n".encode('utf-8'))#ID5
#id4
ser.write("q3h00d\r\n".encode('utf-8')) #timer(hours)
ser.write("q4h00d\r\n".encode('utf-8')) #minutes
ser.write("q5h10d\r\n".encode('utf-8')) #seconds
ser.write("q6h1d\r\n".encode('utf-8')) #save
#id5
ser.write("q53h00d\r\n".encode('utf-8')) #timer(hours)
ser.write("q54h00d\r\n".encode('utf-8')) #minutes
ser.write("q55h10d\r\n".encode('utf-8')) #seconds
ser.write("q56h1d\r\n".encode('utf-8')) #save
ser.write("q6h2d\r\n".encode('utf-8')) #forward
time.sleep(2)
ser.write("q56h3d\r\n".encode('utf-8')) #backward
time.sleep(2)
ser.close() #close the serial port