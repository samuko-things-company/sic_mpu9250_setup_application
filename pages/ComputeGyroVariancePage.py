import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from functions.compute_gyro_var import ComputeGyroVar



class ComputeGyroVarFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="COMPUTE GYR VARIANCE", font=('Monospace',16, 'bold') ,bootstyle="dark")
    
    self.frame = tb.Frame(self)
    
    self.computeGyroVar = ComputeGyroVar()

    
    #create widgets to be added to frame
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))
    self.computeGyroVarButton = tb.Button(self.frame, text="COMPUTE GYR VARIANCE",
                               style=buttonStyleName, padding=20,
                               command=self.runComputation)
    

    #add framed widgets to frame
    self.computeGyroVarButton.pack(side='top', expand=True, fill="both")


    #add label and frame to ComputeGyroVarFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)
  
  def runComputation(self):
    self.computeGyroVar.main()