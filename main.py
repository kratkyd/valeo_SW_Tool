#!/usr/bin/env python3
import sys

import f_cam
import sensor
import resim

if __name__ == '__main__':
    # optional argument - data folder location. Default ./data
    if (len(sys.argv) > 1):
        f_cam.CAM_WRITE_LOCATION = sys.argv[1] + '/f_cam_out.csv'
        sensor.SENSOR_WRITE_LOCATION = sys.argv[1] + '/sensor_out.csv'
        resim.RESIM_WRITE_LOCATION = sys.argv[1] + '/resim_out.csv'
        resim.CAM_READ_LOCATION = sys.argv[1] + '/f_cam_out.csv'
        resim.SENSOR_READ_LOCATION = sys.argv[1] + '/sensor_out.csv'
    f_cam.f_cam_write()
    sensor.sensor_write()
    resim.resim_process()
