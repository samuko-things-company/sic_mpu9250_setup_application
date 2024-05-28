# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

import numpy as np
import time
from termcolor import colored
from globalParams import g
from termcolor import colored


class ComputeAccVar:

  def main(self):
    no_of_samples = 1000

    lin_accx_arr = []
    lin_accy_arr = []
    lin_accz_arr = []

    for i in range(no_of_samples):

      lin_accx, lin_accy, lin_accz = g.serClient.get('/acc-cal')
      lin_accx_arr.append(lin_accx)
      lin_accy_arr.append(lin_accy)
      lin_accz_arr.append(lin_accz)

      percent = (i*100)/no_of_samples
      print(colored(f"reading_acc_cal_data...  {percent} percent complete", 'grey'))

      time.sleep(0.02)

    lin_accx_variance = np.var(lin_accx_arr)
    lin_accy_variance = np.var(lin_accy_arr)
    lin_accz_variance = np.var(lin_accz_arr)

    lin_acc_variance = [ lin_accx_variance, lin_accy_variance, lin_accz_variance]
    print(colored("\n---------------------------------------------------------------", 'magenta'))
    print(colored("computed acc variances:", 'cyan'))
    print(lin_acc_variance)

    g.serClient.send('/acc-var', lin_accx_variance, lin_accy_variance, lin_accz_variance)
    lin_accx_variance, lin_accy_variance, lin_accz_variance = g.serClient.get('/acc-var')

    lin_acc_variance = [ lin_accx_variance, lin_accy_variance, lin_accz_variance]
    print(colored("stored acc variances", 'green'))
    print(lin_acc_variance)
    print(colored("---------------------------------------------------------------", 'magenta'))
