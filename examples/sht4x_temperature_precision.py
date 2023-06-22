# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht4x import sht4x

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht4x.SHT4X(i2c)

sht.temperature_precision = sht4x.MEDIUM_PRECISION

while True:
    for temperature_precision in sht4x.temperature_precision_values:
        print("Current Temperature precision setting: ", sht.temperature_precision)
        for _ in range(10):
            temperature, relative_humidity = sht.measurements
            print("Temperature: {:.2f} C".format(sht.temperature))
            print("Humidity: {:.2f} %%".format(sht.relative_humidity))
            time.sleep(0.5)
        sht.temperature_precision = temperature_precision
