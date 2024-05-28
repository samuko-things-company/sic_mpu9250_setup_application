# REFERENCE: https://learn.adafruit.com/adafruit-sensorlab-gyroscope-calibration/gyro-calibration-with-jupyter

#REFERENCE_1: https://teslabs.com/articles/magnetometer-calibration/
#REFERENCE_2: https://learn.adafruit.com/adafruit-sensorlab-magnetometer-calibration/magnetic-calibration-with-jupyter

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy import linalg

import time
from termcolor import colored
from globalParams import g
from termcolor import colored


class CalibrateMag:
  def __init__(self):
      self.b = np.zeros([3, 1])
      self.A_1 = np.eye(3)
      self.F = 1

      self.magArray = []

      self.mag_x = []
      self.mag_y = []
      self.mag_z = []

      self.calibrated = False

      self.HISTORY_SIZE = 10000

      self.fig, self.ax = plt.subplots(1, 1)
      self.ax.set_aspect(1)

      self.anim = None

      self.stop = False


  def calibrate(self):
      
      # ellipsoid fit
      s = np.array(self.magArray).T
      M, n, d = self.__ellipsoid_fit(s)
      
      # calibration parameters
      # note: some implementations of sqrtm return complex type, taking real
      M_1 = linalg.inv(M)
      self.b = -np.dot(M_1, n)
      self.A_1 = np.real(self.F / np.sqrt(np.dot(n.T, np.dot(M_1, n)) - d) * linalg.sqrtm(M))

      ################################################
      b_vect = [[0.0], [0.0], [0.0]]
      A_mat = [[0.0, 0.0, 0.0],[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

      time.sleep(0.1)
      g.serClient.send('/bvect', self.b[0][0], self.b[1][0], self.b[2][0])
      b_vect[0][0], b_vect[1][0], b_vect[2][0] = g.serClient.get('/bvect')
      time.sleep(0.05)
      
      for i in range(3):
        g.serClient.send(f'/amatR{i}', self.A_1[i][0], self.A_1[i][1], self.A_1[i][2])
        A_mat[i][0], A_mat[i][1], A_mat[i][2] = g.serClient.get(f'/amatR{i}')
        time.sleep(0.05)

      ################################################
      
      print(colored("\n---------------------------------------------------------------", 'magenta'))
      print(colored("computed A_1 matrix:", 'cyan'))
      print(self.A_1)
      print(colored("stored A_1 matrix:", 'green'))
      print(A_mat)
      print(colored("---------------------------------------------------------------", 'magenta'))

      print(colored("\n---------------------------------------------------------------", 'magenta'))
      print(colored("computed b vector:", 'cyan'))
      print(self.b)
      print(colored("stored b vector:", 'green'))
      print(b_vect)
      print(colored("---------------------------------------------------------------", 'magenta'))




  def __ellipsoid_fit(self, s):
      ''' Estimate ellipsoid parameters from a set of points.

          Parameters
          ----------
          s : array_like
            The samples (M,N) where M=3 (x,y,z) and N=number of samples.

          Returns
          -------
          M, n, d : array_like, array_like, float
            The ellipsoid parameters M, n, d.

          References
          ----------
          .. [1] Qingde Li; Griffiths, J.G., "Least squares ellipsoid specific
              fitting," in Geometric Modeling and Processing, 2004.
              Proceedings, vol., no., pp.335-340, 2004
      '''

      # D (samples)
      D = np.array([s[0]**2., s[1]**2., s[2]**2.,
                    2.*s[1]*s[2], 2.*s[0]*s[2], 2.*s[0]*s[1],
                    2.*s[0], 2.*s[1], 2.*s[2], np.ones_like(s[0])])

      # S, S_11, S_12, S_21, S_22 (eq. 11)
      S = np.dot(D, D.T)
      S_11 = S[:6,:6]
      S_12 = S[:6,6:]
      S_21 = S[6:,:6]
      S_22 = S[6:,6:]

      # C (Eq. 8, k=4)
      C = np.array([[-1,  1,  1,  0,  0,  0],
                    [ 1, -1,  1,  0,  0,  0],
                    [ 1,  1, -1,  0,  0,  0],
                    [ 0,  0,  0, -4,  0,  0],
                    [ 0,  0,  0,  0, -4,  0],
                    [ 0,  0,  0,  0,  0, -4]])

      # v_1 (eq. 15, solution)
      E = np.dot(linalg.inv(C),
                  S_11 - np.dot(S_12, np.dot(linalg.inv(S_22), S_21)))

      E_w, E_v = np.linalg.eig(E)

      v_1 = E_v[:, np.argmax(E_w)]
      if v_1[0] < 0: v_1 = -v_1

      # v_2 (eq. 13, solution)
      v_2 = np.dot(np.dot(-np.linalg.inv(S_22), S_21), v_1)

      # quadric-form parameters
      M = np.array([[v_1[0], v_1[3], v_1[4]],
                    [v_1[3], v_1[1], v_1[5]],
                    [v_1[4], v_1[5], v_1[2]]])
      n = np.array([[v_2[0]],
                    [v_2[1]],
                    [v_2[2]]])
      d = v_2[3]

      return M, n, d



  def onClick(self,event):   
      
      if self.stop == False:
          self.anim.event_source.stop()
          if self.calibrated == False:
              self.calibrate()
              self.mag_x = []
              self.mag_y = []
              self.mag_z = []
              self.magArray = []
              self.calibrated = True
          self.stop = True
      else:
          self.anim.event_source.start()
          self.stop = False

      
  def animate(self,i):
      try:
          if self.calibrated == False:
              mx, my, mz = g.serClient.get("/mag-raw")
          else:
              mx, my, mz = g.serClient.get("/mag-cal")
          
          self.magArray.append([mx,my,mz])
          self.mag_x.append(mx)
          self.mag_y.append(my)
          self.mag_z.append(mz)

          # Clear all axis
          self.ax.cla()

          # Display the sub-plots
          self.ax.scatter(self.mag_x, self.mag_y, color='r')
          self.ax.scatter(self.mag_y, self.mag_z, color='g')
          self.ax.scatter(self.mag_z, self.mag_x, color='b')
          
          if len(self.mag_x) == self.HISTORY_SIZE:
              self.anim.event_source.stop()
      except:
          pass
    

  def main(self):
      self.fig.canvas.mpl_connect('button_press_event', self.onClick)    
      self.anim = FuncAnimation(self.fig, self.animate, frames = np.arange(0, 10000, 1), interval=50)
      plt.show()
