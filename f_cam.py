#!/usr/bin/env python3
import os
import sys
import csv
import random

START_TIME = 100.0
START_FRAME = 100
START_SPEED = 60.0
START_YAW_RATE = 0.0
START_SIGNAL1 = 0
START_SIGNAL2 = 0

FRAME_NUM = 2000 #defines length of file
FULL_SPEED = 120.0

CAM_WRITE_LOCATION = './data/f_cam_out.csv' #default write location
os.makedirs('./data', exist_ok=True)


class Cam_data_generator:
    def __init__(self):
        self.timestamp = START_TIME
        self.frameId = START_FRAME
        self.speed = START_SPEED
        self.yawRate = START_YAW_RATE
        self.signal1 = START_SIGNAL1
        self.signal2 = START_SIGNAL2

        self.fullSpeed = False


    def generate(self):
        if (self.frameId < FRAME_NUM+START_FRAME):
            ret = [self.timestamp, self.frameId, self.speed, self.yawRate, self.signal1, self.signal2]
            self.timestamp = round(self.timestamp + 0.0277 - 0.00005 + 0.0001*random.random(), 6)
            self.frameId += 1
            if (not self.fullSpeed):
                self.speed = round(self.speed + 0.08, 3) #expecting precision of 3 decimals
                if (self.speed >= FULL_SPEED):
                    self.fullSpeed = True
            else:
                self.speed = round(FULL_SPEED - 0.05 + 0.1*random.random(), 3)
            self.yawRate = round(-1.0 + 2.0*random.random(), 3) #expecting precision of 3 decimals
            if (self.frameId == 201):
                self.signal1 = random.randint(1, 15)
            if (self.signal1 >= 5):
                self.signal2 = 70 + random.randint(0, 20) #expecting integer
            return ret
        else:
            return None

def f_cam_write():
    with open(CAM_WRITE_LOCATION, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        generator = Cam_data_generator()

        row = generator.generate()
        while (row != None):
            csv_writer.writerow(row)
            row = generator.generate()

if __name__ == '__main__':
    #optional output folder argument, folder needs to exist!
    if (len(sys.argv) > 1):
        CAM_WRITE_LOCATION = sys.argv[1] + '/f_cam_out.csv'
    f_cam_write()