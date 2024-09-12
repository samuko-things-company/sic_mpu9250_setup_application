import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

import serial.tools.list_ports
from serial_comm_lib import SerialComm

import time

from globalParams import g
from components.SelectValueFrame import SelectValueFrame





class SerialConnectFrame(tb.Frame):
  def __init__(self, parentFrame, next_func=None):
    super().__init__(master=parentFrame)

    self.next_func = next_func

    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',12,'bold'))

    self.frame = tb.LabelFrame(self, borderwidth=10, bootstyle='primary')

    #create widgets to be added to frame
    self.selectPort = SelectValueFrame(self.frame, keyTextInit="PORT: ", valTextInit=g.port,
                                       initialComboValues=self.refreshPortlist(),
                                       middileware_func=self.selectPortFunc)
    
    self.connectButton = tb.Button(self.frame, text="CONNECT",
                               style=buttonStyleName, padding=10, width=20,
                               command=self.connect_serial_func)
    
    self.refreshButton = tb.Button(self.frame, text="REFRESH",
                               style=buttonStyleName, padding=10, width=20,
                               command=self.refresh_serial_func)

    #add framed widgets to frame
    self.selectPort.pack(side='top', fill="both", pady=(5,35))
    self.connectButton.pack(side='top', fill="both", pady=10)
    self.refreshButton.pack(side='top', fill="both", pady=10)

    # add frame to Serial ConnectFrame
    self.frame.place(relx=0.5, rely=0.5, anchor="center")


  def selectPortFunc(self, port_name):
    try:
      if port_name:
        g.port = port_name
    except:
      pass

    return g.port
  
  def refreshPortlist(self):
    try:
      port_list = [port.device for port in serial.tools.list_ports.comports()]
      if len(port_list)==0:
        return ['None']
      return port_list
    except:
      port_list = ['None']


  def connectToPort(self, name):
    try:
      g.serClient = SerialComm(name)
      time.sleep(6)
      data = g.serClient.get("/gain")
      # print(data)
      return True
    except:
      return False

  
  def refresh_serial_func(self):
    port_list = self.refreshPortlist()
    self.selectPort.setComboArrVal(port_list)
    self.selectPort.setComboVal("None")
    self.selectPort.setVal("None")


  def connect_serial_func(self):
    port = self.selectPort.getSelectedVal()
    serIsConnected = self.connectToPort(port)
    if serIsConnected:
      # print("connection successful")
      Messagebox.show_info(f"SUCCESS:\n\nSIC_MPU9250 module found on port: {port}\n\nclick OK to continue", "SUCCESS")
      self.next_func()
    else:
      # print("Error connecting to driver")
      Messagebox.show_error(f"ERROR:\n\nno SIC_MPU9250 module module found on port: {port}\n\ntry again or try another port", "ERROR")
