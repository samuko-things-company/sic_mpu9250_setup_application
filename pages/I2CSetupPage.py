import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from globalParams import g

from components.SetValueFrame import SetValueFrame



class I2CSetupFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="I2C ADDRESS SETUP", font=('Monospace',16, 'bold') ,bootstyle="dark")
    self.frame = tb.Frame(self)

    #create widgets to be added to frame
    g.i2cAddress = int(g.serClient.get("/i2c"))
    self.setI2Caddress = SetValueFrame(self.frame, keyTextInit="I2C_ADDRESS: ", valTextInit=g.i2cAddress,
                                middleware_func=self.setI2CaddressFunc)

    #add framed widgets to frame
    self.setI2Caddress.pack(side='top', expand=True, fill="both")


    #add label and frame to I2CSetupFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)


  def setI2CaddressFunc(self, text):
    try:
      if text:
        isSuccessful = g.serClient.send("/i2c", float(text))
        val = int(g.serClient.get("/i2c"))
        g.i2cAddress = val
    except:
      pass
  
    return g.i2cAddress
