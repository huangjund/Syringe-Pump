# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:21:18 2023

@author: Administrator
"""

import serial #import module
import keyboard
import time

ser = serial.Serial(port="COM6", baudrate=9600, bytesize=8, timeout=1) #open serial port
ser.write("q7h10d\r\n".encode('utf-8')) #type of syringe
ser.write("q7h12d\r\n".encode('utf-8')) #unit of the speed
ser.write("q1h12d\r\n".encode('utf-8')) #speed(integer digit)
ser.write("q2h00d\r\n".encode('utf-8')) #speed(decimal place)
ser.write("q3h0d\r\n".encode('utf-8')) #timer(hours)
ser.write("q4h0d\r\n".encode('utf-8')) #minutes
ser.write("q5h8d\r\n".encode('utf-8')) #seconds
ser.write("q6h3d\r\n".encode('utf-8')) #backward
#ser.write("q6h2d\r\n".encode('utf-8')) #forward
time.sleep(1)
if keyboard.is_pressed('ctrl'): #in case of danger -- emergency use
    ser.write("q6h6d".encode('utf-8'))#stop the syringe
    print("stop the experiment immediately!“）
ser.close() #close the serial port