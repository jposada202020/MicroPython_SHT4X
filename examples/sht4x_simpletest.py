# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht4x import sht4x

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht4x.SHT4X(i2c)


# print(sht.temperature_precision)
# sht.temperature_precision = sht4x.MEDIUM_PRECISION
# print(sht.temperature_precision)


while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: {:.2f} C".format(sht.temperature))
    print("Humidity: {:.2f} %%".format(sht.relative_humidity))
    print("")
    time.sleep(0.5)
