import os
import csv
import random


START_FRAME = 100
START_SPEED = 60.0
START_YAW_RATE = 0.0
START_SIGNAL1 = 0
START_SIGNAL2 = 0

FRAME_NUM = 2000 #defines length of file
FULL_SPEED = 120.0
SIGNAL1_TRIGGER = 200

os.makedirs('./data', exist_ok=True)
write_location = './data/f_cam_out.csv' #folders have to exist

class Data_generator:
    def __init__(self):
        self.timestamp = 100.0
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
                self.speed = round(self.speed + 0.08, 2) #expecting precision of 2
                if (self.speed >= FULL_SPEED):
                    self.fullSpeed = True
            else:
                self.speed = round(FULL_SPEED - 0.05 + 0.1*random.random(), 2)
            self.yawRate = round(-1.0 + 2.0*random.random(), 6) #expecting same precision?
            if (self.frameId == 201):
                self.signal1 = random.randint(1, 15)
            if (self.signal1 >= 5):
                self.signal2 = 70 + random.randint(0, 20) #integer I expect
            return ret
        else:
            return None

with open(write_location, 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    generator = Data_generator()

    row = generator.generate()
    while (row != None):
        csv_writer.writerow(row)
        row = generator.generate()