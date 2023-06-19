# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht4x import sht4x

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht4x.SHT4X(i2c)

sht.heat_time = sht4x.TEMP_1

while True:
    for heat_time in sht4x.heat_time_values:
        print("Current Heat time setting: ", sht.heat_time)
        for _ in range(10):
            temperature, relative_humidity = sht.measurements
            print("Temperature: {:.2f} C".format(temperature))
            print("Humidity: {:.2f} %%".format(relative_humidity))
            print()
            time.sleep(0.5)
