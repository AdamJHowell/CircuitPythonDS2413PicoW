import time
import board
from adafruit_onewire.bus import OneWireBus
import adafruit_ds2413

"""
pip install adafruit-circuitpython-onewire
pip install adafruit-circuitpython-ds2413
"""

one_wire_bus = OneWireBus( board.GP2 )
ds2413 = adafruit_ds2413.DS2413( one_wire_bus, one_wire_bus.scan()[0] )

ds2413_led = ds2413.IOA
ds2413_button = ds2413.IOB
ds2413_button.direction = adafruit_ds2413.INPUT

while not ds2413_button.value:
  ds2413_led.value = True
  time.sleep( 0.5 )
  ds2413_led.value = False
  time.sleep( 0.5 )
