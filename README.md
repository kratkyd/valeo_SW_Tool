## Valeo DFC Applied Python Evaluation

This project is supposed to simulate a processing toolchain, as described in the assignment. The project contains following files:

### f_cam.py
This script simulates data as sent by a Front Camera device. Object *generator* of class *Cam_data_generator* is created, and on each call of *generator.generate()*, new row of data is created, based on assignment description, it is then written into *f_cam_out.csv* file (default in *./data* folder). When exit condition is fulfilled (amount of frames higher than 2000), method returns None, which ends the csv writing process.

When executed, one optional argument can be added to select path to a different folder to save output csv.

### sensor.py
Similar to *f_cam.py*, with different data, simulating a reference sensor device.

Again, one optional argument can be added to select non-default folder.

### resim.py
Simulates a reprocessing device. This script reads from two .csv files previously outputted by *f_cam.py* and *sensor.py*, processes the data as described in the assignment and creates *resim_out.csv* file with output data (again, default in *./data* folder).

When executed without arguments, the program reads, and writes into *./data* folder.

When used with one argument, it changes the output folder location (for example resim.py ./other_data_folder). 

When used with three arguments, first selects output folder, second input **file** *f_cam_out.csv*, and third input **file** *sensor_out.csv* (for example ./data ./folder/f_cam_out.csv ./other_folder/sensor.py)

## main.py
Imports previous three scripts as modules and runs them in proper order, as to generate all three required .csv files.

One optional argument can select folder in which all csv files will be stored.

---
All four python files are executable in linux due to shebangs, but files **resim_linux** and **resim_windows.exe**  are executable in coresponding OS without python dependency, and have the same functionality as **resim.py** script. These were built with Pyinstaller application.

https://github.com/pyinstaller

**data** folder in default run (without arguments) contains all created .csv files.

---
## Notes
- .data folder is created on every execution, if it doesn't exist already. Thought it to be more appropriate than adding empty folder (with some .gitignore) into the project.
- not all the values in *f_cam.py* and *sensor.py* have their own constants. Honestly there is so many of them, I don't actually know whether it would be good practice to write them all out or not. My guess was that it depends on the project, so I chose the ones that seemed significant to me
- the project might have too many commits, some of the actions probably could've been stuck together, but the separate goals were quite small and I didn't want to mix them together


These next notes are rather inconsequential, misunderstood assignment because of wording or similar issues
- not sure if I misunderstood something, but time in microseconds to 6 decimal places (so effectively measuring picoseconds) with random variation +/- 0.05 ms seemed unreasonable to me. I used seconds instead, because that means I go exactly into order of microseconds. If I'm mistaken, it would be an easy fix
- the usage of "value is greater or equal then" in the asssignment seems unclear to me, might've used < instead of <= somewhere, or vice versa because of that
- not sure if number of frames in *f_cam_out.csv* is supposed to be 2000, or if *FrameID* is supposed to go up to 2000