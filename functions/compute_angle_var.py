# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

import numpy as np
import time
from termcolor import colored
from globalParams import g
from termcolor import colored


class ComputeAngleVar:

  def main(self):
    no_of_samples = 1000

    roll_arr = []
    pitch_arr = []
    yaw_arr = []

    for i in range(no_of_samples):
      r_rad, p_rad, y_rad = g.serClient.get('/rpy')
      roll_arr.append(r_rad)
      pitch_arr.append(p_rad)
      yaw_arr.append(y_rad)

      percent = (i*100)/no_of_samples
      print(colored(f"reading_rpy_data...  {percent} percent complete", 'grey'))

      time.sleep(0.02)
    
    roll_variance = np.var(roll_arr)
    pitch_variance = np.var(pitch_arr)
    yaw_variance = np.var(yaw_arr)

    rpy_variance = [ roll_variance, pitch_variance, yaw_variance]
    print(colored("\n---------------------------------------------------------------", 'magenta'))
    print(colored("computed rpy variances:", 'cyan'))
    print(rpy_variance)

    g.serClient.send('/rpy-var', roll_variance, pitch_variance, yaw_variance)
    roll_variance, pitch_variance, yaw_variance = g.serClient.get('/rpy-var')

    rpy_variance = [ roll_variance, pitch_variance, yaw_variance]
    print(colored("stored rpy variances", 'green'))
    print(rpy_variance)
    print(colored("---------------------------------------------------------------", 'magenta'))
