import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from globalParams import g

from components.SetValueFrame import SetValueFrame
from components.VisualizeImuFrame import VisualizeImuFrame


class GainSetupVizFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="VIZUALIZE GAIN", font=('Monospace',16, 'bold') ,bootstyle="dark")
    
    self.frame = tb.Frame(self)

    #create widgets to be added to frame
    g.filterGain = g.serClient.get("/gain")
    self.setFilterGain = SetValueFrame(self.frame, keyTextInit="FILTER_GAIN: ", valTextInit=g.filterGain,
                                middleware_func=self.setFilterGainFunc)
    self.vizImuFrame = VisualizeImuFrame(self.frame)

    #add framed widgets to frame
    self.setFilterGain.pack(side='top', expand=True, fill="both")
    self.vizImuFrame.pack(side='top', expand=True, fill="both")


    #add label and frame to GainSetupVizFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)


  def setFilterGainFunc(self, text):
    try:
      if text:
        isSuccessful = g.serClient.send("/gain", float(text))
        val = g.serClient.get("/gain")
        g.filterGain = val
    except:
      pass
  
    return g.filterGain
