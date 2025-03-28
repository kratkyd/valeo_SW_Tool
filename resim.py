import csv


res_f = open('resim_out.csv', 'w')
csv_writer = csv.writer(res_f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

with open('f_cam_out.csv', 'r') as csv_cam, open('sensor_out.csv', 'r') as csv_sensor:
    csv_cam_reader = csv.reader(csv_cam)
    csv_sensor_reader = csv.reader(csv_sensor)

    sensor_row = next(csv_sensor_reader)
    next_sensor_row = next(csv_sensor_reader)

    for cam_row in csv_cam_reader:
        while(next_sensor_row != None and float(next_sensor_row[0]) < float(cam_row[0])):
            sensor_row = next_sensor_row
            print(sensor_row[1])
            next_sensor_row = next(csv_sensor_reader, None) #defaults to None
        cam_row[2] = round((float(cam_row[2]) + float(sensor_row[1]))/2, 2)
        csv_writer.writerow(cam_row)

res_f.close()