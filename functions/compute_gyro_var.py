# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

import numpy as np
import time
from termcolor import colored
from globalParams import g
from termcolor import colored


class ComputeGyroVar:

  def main(self):
    no_of_samples = 1000

    roll_rate_arr = []
    pitch_rate_arr = []
    yaw_rate_arr = []

    for i in range(no_of_samples):
      r_rate, p_rate, y_rate = g.serClient.get('/gyro-cal')
      roll_rate_arr.append(r_rate)
      pitch_rate_arr.append(p_rate)
      yaw_rate_arr.append(y_rate)

      percent = (i*100)/no_of_samples
      print(colored(f"reading_gyro_cal_data...  {percent} percent complete", 'grey'))

      time.sleep(0.02)


    roll_rate_variance = np.var(roll_rate_arr)
    pitch_rate_variance = np.var(pitch_rate_arr)
    yaw_rate_variance = np.var(yaw_rate_arr)


    gyro_variance = [ roll_rate_variance, pitch_rate_variance, yaw_rate_variance]
    print(colored("\n---------------------------------------------------------------", 'magenta'))
    print(colored("computed gyro variances:", 'cyan'))
    print(gyro_variance)

    g.serClient.send('/gyro-var', roll_rate_variance, pitch_rate_variance, yaw_rate_variance)
    roll_rate_variance, pitch_rate_variance, yaw_rate_variance = g.serClient.get('/gyro-var')

    gyro_variance = [ roll_rate_variance, pitch_rate_variance, yaw_rate_variance]
    print(colored("stored gyro variances", 'green'))
    print(gyro_variance)
    print(colored("---------------------------------------------------------------", 'magenta'))
