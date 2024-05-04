import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from functions.calibrate_gyro import CalibrateGyro



class CalibrateGyroFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="CALIBRATE GYR", font=('Monospace',16, 'bold') ,bootstyle="dark")
    
    self.frame = tb.Frame(self)
    
    self.calibrateGyro = CalibrateGyro()

    
    #create widgets to be added to frame
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))
    self.calGyroButton = tb.Button(self.frame, text="CALIBRATE GYR",
                               style=buttonStyleName, padding=20,
                               command=self.runCalibration)
    

    #add framed widgets to frame
    self.calGyroButton.pack(side='top', expand=True, fill="both")


    #add label and frame to CalibrateGyroFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)
  
  def runCalibration(self):
    self.calibrateGyro.main()
