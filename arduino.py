from string import digits
import serial
import time
import pyautogui as pg

arduinoData = serial.Serial('/dev/cu.usbserial-1130', 9600) #com12should be changed to actual port on arduino

while True:     #Allows us to keep checking the incoming data from Arduino
    incoming_data = str (arduinoData.readline())
    y = "".join(c for c in incoming_data if c in digits)
    print(y)
    if y>"560":
        pg.scroll(1)
    if y<"460":
        pg.scroll(-1)
    incoming_data = "";  #clears used data so we can get a new set and check it

