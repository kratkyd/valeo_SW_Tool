#!/usr/bin/env python3
import os
import sys
import csv

#default file locations
SENSOR_READ_LOCATION = './data/sensor_out.csv'
CAM_READ_LOCATION = './data/f_cam_out.csv'
RESIM_WRITE_LOCATION = './data/resim_out.csv'
os.makedirs('./data', exist_ok=True)

def resim_process():
    with open(CAM_READ_LOCATION, 'r') as csv_cam, open(SENSOR_READ_LOCATION, 'r') as csv_sensor, open(RESIM_WRITE_LOCATION, 'w', newline='') as res_f:
        csv_cam_reader = csv.reader(csv_cam)
        csv_sensor_reader = csv.reader(csv_sensor)
        csv_writer = csv.writer(res_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        sensor_row = next(csv_sensor_reader)
        next_sensor_row = next(csv_sensor_reader)

        for cam_row in csv_cam_reader:
            while(next_sensor_row != None and float(next_sensor_row[0]) < float(cam_row[0])):
                sensor_row = next_sensor_row
                next_sensor_row = next(csv_sensor_reader, None)
            cam_row[2] = round((float(cam_row[2]) + float(sensor_row[1]))/2, 3)
            csv_writer.writerow(cam_row)

if __name__ == '__main__':
    # optional arguments
    # 1 argument - output folder location
    # 3 arguments - output folder, cam input file, sensor input file
    if (len(sys.argv) > 1):
        RESIM_WRITE_LOCATION = sys.argv[1] + '/resim_out.csv'
    if (len(sys.argv) == 4):
        CAM_READ_LOCATION = sys.argv[2]
        SENSOR_READ_LOCATION = sys.argv[3]

    resim_process()