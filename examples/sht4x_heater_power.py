# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_sht4x import sht4x

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
sht = sht4x.SHT4X(i2c)

sht.heater_power = sht4x.HEATER20mW

while True:
    for heater_power in sht4x.heater_power_values:
        print("Current Heater power setting: ", sht.heater_power)
        for _ in range(10):
            temperature, relative_humidity = sht.measurements
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Relative Humidity: {relative_humidity:.2%}%")
            print()
            time.sleep(0.5)
        sht.heater_power = heater_power
