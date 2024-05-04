import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# from globalParams import g

# from components.SetValueFrame import SetValueFrame
from functions.calibrate_acc import CalibrateAcc



class CalibrateAccFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="CALIBRATE ACC", font=('Monospace',16, 'bold') ,bootstyle="dark")
    
    self.frame = tb.Frame(self)
    
    self.calibrateAcc = CalibrateAcc()
    
    #create widgets to be added to frame1
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))
    self.calAccButton = tb.Button(self.frame, text="CALIBRATE ACC",
                               style=buttonStyleName, padding=20,
                               command=self.runCalibration)
    

    #add framed widgets to frame
    self.calAccButton.pack(side='top', expand=True, fill="both")


    #add label and frame to CalibrateAccFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)
  
  def runCalibration(self):
    self.calibrateAcc.main()
