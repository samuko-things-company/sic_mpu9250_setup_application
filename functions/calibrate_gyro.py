# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

import matplotlib.pyplot as plt
from collections import deque
import numpy as np
from globalParams import g
from termcolor import colored


class CalibrateGyro:
  def main(self):
      # How many sensor samples we want to store
      HISTORY_SIZE = 1000
  
      # Deque for axes
      gyro_x = deque(maxlen=HISTORY_SIZE)
      gyro_y = deque(maxlen=HISTORY_SIZE)
      gyro_z = deque(maxlen=HISTORY_SIZE)

      count = 0
      while len(gyro_x) < HISTORY_SIZE:
          try:
              gx, gy, gz = g.serClient.get("/gyro-raw")

              gyro_x.append(gx)
              gyro_y.append(gy)
              gyro_z.append(gz)

              count +=1
              percent = (count*100)/HISTORY_SIZE
              print(colored(f"reading_gyro_raw_data... {percent} percent complete", 'grey'))
          except:
              pass


      min_x = min(gyro_x)
      max_x = max(gyro_x)
      min_y = min(gyro_y)
      max_y = max(gyro_y)
      min_z = min(gyro_z)
      max_z = max(gyro_z)

      gx_offset = (max_x + min_x) / 2
      gy_offset = (max_y + min_y) / 2
      gz_offset = (max_z + min_z) / 2



      gyro_calibration = [ gx_offset, gy_offset, gz_offset]
      print(colored("\n---------------------------------------------------------------", 'magenta'))
      print(colored("computed gyro offsets in rad/s:", 'cyan'))
      print(gyro_calibration)

      g.serClient.send('/gyro-off', gx_offset, gy_offset, gz_offset)
      gx_offset, gy_offset, gz_offset = g.serClient.get('/gyro-off')

      gyro_calibration = [ gx_offset, gy_offset, gz_offset]
      print(colored("stored gyro offsets in rad/s:", 'green'))
      print(gyro_calibration)
      print(colored("---------------------------------------------------------------", 'magenta'))




      fig, (uncal, cal) = plt.subplots(2, 1)

      # Clear all axis
      uncal.cla()
      cal.cla()
      t = np.linspace(0, len(gyro_x), len(gyro_x))


      # plot uncalibrated data
      uncal.set_ylim([-1,1])
      uncal.grid(which = "major", linewidth = 0.5)
      uncal.grid(which = "minor", linewidth = 0.2)
      uncal.minorticks_on()

      uncal.plot(t, gyro_x, color='r')
      uncal.plot(t, gyro_y, color='g')
      uncal.plot(t, gyro_z, color='b')
      uncal.title.set_text("Uncalibrated Gyro")
      uncal.set(ylabel='rad/s')

      # plot calibrated data
      cal.set_ylim([-1,1])
      cal.grid(which = "major", linewidth = 0.5)
      cal.grid(which = "minor", linewidth = 0.2)
      cal.minorticks_on()

      cal.plot(t, [x - gyro_calibration[0] for x in gyro_x], color='r')
      cal.plot(t, [y - gyro_calibration[1] for y in gyro_y], color='g')
      cal.plot(t, [z - gyro_calibration[2] for z in gyro_z], color='b')
      cal.title.set_text("Calibrated Gyro")
      cal.set(ylabel='rad/s')

      fig.tight_layout()
      plt.show()
