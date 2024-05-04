from vpython import *
import numpy as np
import math as m


from globalParams import g


# toRad = 2*np.pi/360
# toDeg = 1/toRad

class VizualizeImu:
  def main(self):
    try:

      ##----------------------------------------------------------------##
      scene.range=5
      scene.forward=vector(-1,-1,-1)
      scene.width=600
      scene.height=600

      xAxis = arrow(length=1.25, shaftwidth=.1, color=color.red,
                    axis=vector(0,0,1)) # (y,z,x)
      yAxis = arrow(length=1.25, shaftwidth=.1, color=color.green,
                    axis=vector(1,0,0)) # (y,z,x)
      zAxis = arrow(length=1.25, shaftwidth=.1, color=color.blue,
                    axis=vector(0,1,0)) # (y,z,x)

      xArrow = arrow(length=3, shaftwidth=.08, color=color.red,
                    axis=vector(0,0,1), opacity=.3) # (y,z,x)
      yArrow = arrow(length=3, shaftwidth=.08, color=color.green,
                    axis=vector(1,0,0), opacity=.3) # (y,z,x)
      zArrow = arrow(length=3, shaftwidth=.08, color=color.blue,
                    axis=vector(0,1,0), opacity=.3) # (y,z,x)

      myBox = box()
      myBox.length = 3.5
      myBox.width = 1.5
      myBox.height = 0.25
      myBox.opacity = 0.3 

      myObj = compound([myBox])
      ##----------------------------------------------------------------##


      ##----------------------------------------------------------------##
      while True:
        roll, pitch, yaw = g.serClient.get('rpy')

        ##### perform axis computations #####################
        up=np.array([0,0,1]) # (x,y,z)
        x_vect=np.array([m.cos(yaw)*m.cos(pitch), m.sin(yaw)*m.cos(pitch), -1.00*m.sin(pitch)]) # (x,y,z)
        y_vect = np.cross(up,x_vect) # (x,y,z)
        z_vect = np.cross(x_vect,y_vect) # (x,y,z)

        z_rot = z_vect*m.cos(roll)+(np.cross(x_vect,z_vect))*m.sin(roll)

        y_rot = np.cross(z_rot, x_vect)
        #######################################################

        
        ######### draw axis in vpyton ########################
        xArrow.axis = vector(x_vect[1], x_vect[2], x_vect[0])# (y,z,x)
        xArrow.length = 3

        yArrow.axis = vector(y_rot[1], y_rot[2], y_rot[0])# (y,z,x)
        yArrow.length = 2

        zArrow.axis = vector(z_rot[1], z_rot[2], z_rot[0])# (y,z,x)
        zArrow.length = 1.5

        myObj.axis = vector(x_vect[1], x_vect[2], x_vect[0]) # (y,z,x)
        myObj.up = vector(z_rot[1], z_rot[2], z_rot[0]) # (y,z,x)

    except:
      print("process ended")

    ##----------------------------------------------------------------##