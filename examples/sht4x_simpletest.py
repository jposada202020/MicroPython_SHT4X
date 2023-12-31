# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht4x import sht4x

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht4x.SHT4X(i2c)

while True:
    temperature, relative_humidity = sht.measurements
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Relative Humidity: {relative_humidity:.2%}%")
    print("")
    time.sleep(0.5)
