# main.py -- put your code here!

from machine import SPI, Pin

# WiPy (on Exp board, SD and User-LED jumper have to be removed!)
SPI    = machine.SPI(1, baudrate=328125, bits=8, polarity=0, phase=1, sck=18, mosi=23, miso=19)   # Changed this line in order to work with ESP32 DEV Kit with Loboris Micropython
RST    = machine.Pin(4)
CE     = machine.Pin(5)
DC     = machine.Pin(19)
LIGHT  = machine.Pin(2)
# PWR    = directly from 3V3 pin of the WiPy

import upcd8544

lcd = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)

lcd.data([0xff])
lcd.data([0xaa, 0x55, 0xaa, 0x55, 0xaa, 0x55, 0xaa])
