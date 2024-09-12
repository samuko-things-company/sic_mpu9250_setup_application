# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

import matplotlib.pyplot as plt
from collections import deque
import numpy as np
from globalParams import g
from termcolor import colored


class CalibrateAcc:
  def average(self, val):
      ans = 0
      for i in val:
        ans= ans + i
      
      ans = ans/len(val)
      
      return ans
  def main(self):
      # How many sensor samples we want to store
      HISTORY_SIZE = 1000
  
      # Deque for axes
      acc_x = deque(maxlen=HISTORY_SIZE)
      acc_y = deque(maxlen=HISTORY_SIZE)
      acc_z = deque(maxlen=HISTORY_SIZE)

      count = 0
      while len(acc_x) < HISTORY_SIZE:
          try:
              ax, ay, az = g.serClient.get("/acc-raw")

              acc_x.append(ax)
              acc_y.append(ay)
              acc_z.append(az)

              count +=1
              percent = (count*100)/HISTORY_SIZE
              print(colored(f"reading_acc_raw_data...  {percent} percent complete", 'grey'))
          except:
              pass

      g.frameId = int(g.serClient.get("/frame-id")) ## 0 - NWU,  1 - ENU,  2 - NED

      if g.frameList[g.frameId] == "NWU":
        ax_offset = self.average(acc_x)
        ay_offset = self.average(acc_y)
        az_offset = (self.average(acc_z) - 9.8)

      elif g.frameList[g.frameId] == "ENU":
        ax_offset = self.average(acc_x)
        ay_offset = self.average(acc_y)
        az_offset = (self.average(acc_z) - 9.8)
      
      elif g.frameList[g.frameId] == "NED":
        ax_offset = self.average(acc_x)
        ay_offset = self.average(acc_y)
        az_offset = (self.average(acc_z) + 9.8)



      acc_calibration = [ ax_offset, ay_offset, az_offset ]
      print(colored("\n---------------------------------------------------------------", 'magenta'))
      print(colored("computed acc offsets in m/s^2::", 'cyan'))
      print(acc_calibration)

      g.serClient.send('/acc-off', ax_offset, ay_offset, az_offset)
      ax_offset, ay_offset, az_offset = g.serClient.get('/acc-off')

      acc_calibration = [ ax_offset, ay_offset, az_offset ]
      print(colored("stored acc offsets in m/s^2:", 'green'))
      print(acc_calibration)
      print(colored("---------------------------------------------------------------", 'magenta'))


      fig, (uncal, cal) = plt.subplots(nrows=2)

      # Clear all axis
      uncal.cla()
      cal.cla()
      t = np.linspace(0, len(acc_x), len(acc_x))


      # plot uncalibrated data
      uncal.plot(t, acc_x, color='r')
      uncal.plot(t, acc_y, color='g')
      uncal.plot(t, acc_z, color='b')
      uncal.title.set_text("Uncalibrated Acc")
      uncal.set(ylabel='g')

      uncal.grid(which = "major", linewidth = 0.5)
      uncal.grid(which = "minor", linewidth = 0.2)
      uncal.minorticks_on()


      # plot calibrated data
      cal.plot(t, [x - acc_calibration[0] for x in acc_x], color='r')
      cal.plot(t, [y - acc_calibration[1] for y in acc_y], color='g')
      cal.plot(t, [z - acc_calibration[2] for z in acc_z], color='b')
      cal.title.set_text("Calibrated Acc")
      cal.set(ylabel='g')

      cal.grid(which = "major", linewidth = 0.5)
      cal.grid(which = "minor", linewidth = 0.2)
      cal.minorticks_on()



      fig.tight_layout()
      plt.show()
