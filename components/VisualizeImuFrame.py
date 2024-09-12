import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from vpython import *
import numpy as np
import math as m

from globalParams import g




class VisualizeImuFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    ##############################
    self.xAxis=None
    self.yAxis=None
    self.zAxis=None
    self.xArrow=None
    self.yArrow=None
    self.zArrow=None
    self.myBox=None
    self.myObj=None
    ##############################

    self.displayFrame = tb.Frame(self)
    self.canvasFrame = tb.Frame(self)

    #create widgets to be added to the textFame
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))

    self.button1 = tb.Button(self.displayFrame, text="VIZUALIZE IMU", style=buttonStyleName,
                             padding=20, command=self.start_imu_viz)

    #add created widgets to displayFrame
    self.button1.pack(side='left', fill='both', padx=10, pady=30)

    #create widgets to be added to the canvasFame
    self.canvas = tb.Canvas(self.canvasFrame, width=20, height=10,autostyle=False ,bg="#FFFFFF", relief='flat')

    #add created widgets to canvasFame
    self.canvas.pack(side='left', expand=True, fill='both')

    # initialize canvas
    
    # add displayFrame and canvasFrame to GraphFrame
    self.displayFrame.pack(side='top', expand=True, fill='x', padx=10, pady=20)
    self.canvasFrame.pack(side='top', expand=True, fill='both')

    ############################################


  def start_imu_viz(self):
    ##----------------------------------------------------------------##
    scene.range=5
    scene.forward=vector(-1,-1,-1)
    scene.width=500
    scene.height=500

    self.xAxis = arrow(length=1.25, shaftwidth=.08, color=color.red,
                  axis=vector(0,0,1), opacity=1.0) # (y,z,x)
    self.yAxis = arrow(length=1.25, shaftwidth=.08, color=color.green,
                  axis=vector(1,0,0), opacity=1.0) # (y,z,x)
    self.zAxis = arrow(length=1.25, shaftwidth=.08, color=color.blue,
                  axis=vector(0,1,0), opacity=1.0) # (y,z,x)
    
    self.xArrow = arrow(length=3, shaftwidth=.1, color=color.red,
                    axis=vector(0,0,1), opacity=.3) # (y,z,x)
    self.yArrow = arrow(length=3, shaftwidth=.1, color=color.green,
                  axis=vector(1,0,0), opacity=.3) # (y,z,x)
    self.zArrow = arrow(length=3, shaftwidth=.1, color=color.blue,
                  axis=vector(0,1,0), opacity=.3) # (y,z,x)
    
    self.myBox = box()
    self.myBox.length = 3.5
    self.myBox.width = 1.5
    self.myBox.height = 0.2
    self.myBox.opacity = 0.3 

    g.frameId = int(g.serClient.get("/frame-id"))

    if g.frameList[g.frameId] == "ENU":    
      self.myBox.length = 1.5
      self.myBox.width = 3.5
    
    self.myObj = compound([self.myBox])

    self.vizualize_imu()


  def vizualize_imu(self):
    try:
      roll, pitch, yaw = g.serClient.get('/rpy')

      ##### perform axis computations #####################
      up=np.array([0,0,1]) # (x,y,z)
      x_vect=np.array([m.cos(yaw)*m.cos(pitch), m.sin(yaw)*m.cos(pitch), -1.00*m.sin(pitch)]) # (x,y,z)
      y_vect = np.cross(up,x_vect) # (x,y,z)
      z_vect = np.cross(x_vect,y_vect) # (x,y,z)

      z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)

      y_rot = np.cross(z_rot, x_vect)
      #######################################################

      
      ######### draw axis in vpyton ########################
      self.xArrow.axis = vector(x_vect[1], x_vect[2], x_vect[0])# (y,z,x)
      self.xArrow.length = 3

      self.yArrow.axis = vector(y_rot[1], y_rot[2], y_rot[0])# (y,z,x)
      self.yArrow.length = 2

      self.zArrow.axis = vector(z_rot[1], z_rot[2], z_rot[0])# (y,z,x)
      self.zArrow.length = 1.5

      self.myObj.axis = vector(x_vect[1], x_vect[2], x_vect[0]) # (y,z,x)
      self.myObj.up = vector(z_rot[1], z_rot[2], z_rot[0]) # (y,z,x)

      self.canvas.after(10, self.vizualize_imu)
    except:
      scene.delete()
      exit()