#!/usr/bin/env python3
import os
import sys
import csv
import random

START_TIME = 100.0
START_SPEED = 60.0

FULL_SPEED = 120.0
MAX_TIME = 160.0 #defines lentgh of file

SENSOR_WRITE_LOCATION = './data/sensor_out.csv' #default write location
os.makedirs('./data', exist_ok=True)

class Data_generator:
    def __init__(self):
        self.timestamp = START_TIME
        self.speed = START_SPEED

        self.fullSpeed = False

    def generate(self):
        if (self.timestamp <= 160.0):
            ret = [self.timestamp, self.speed]
            self.timestamp = round(self.timestamp + 0.2 - 0.01 + 0.02*random.random(), 6)
            if (not self.fullSpeed):
                self.speed = round(self.speed+0.56, 3)
                if (self.speed >= FULL_SPEED):
                    self.fullSpeed = True
            else:
                self.speed = round(FULL_SPEED - 0.1 + 0.2*random.random(), 3)

            return ret
        else:
            return None

def sensor_write():
    with open(SENSOR_WRITE_LOCATION , 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        generator = Data_generator()

        row = generator.generate()
        while (row != None):
            csv_writer.writerow(row)
            row = generator.generate()

if __name__ == '__main__':
    #optional output folder argument, folder needs to exist!
    if (len(sys.argv) > 1):
        SENSOR_WRITE_LOCATION = sys.argv[1] + '/sensor_out.csv'
    sensor_write()