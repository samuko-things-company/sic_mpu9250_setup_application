import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from globalParams import g

from components.SelectValueFrame import SelectValueFrame



class ImuRefSetupFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="IMU REFERENCE FRAME", font=('Monospace',16, 'bold') ,bootstyle="dark")
    self.frame = tb.Frame(self)

    #create widgets to be added to frame
    g.frameId = int(g.serClient.get("/frame-id"))
    self.selectFrameId = SelectValueFrame(self.frame, keyTextInit=f"IMU REF FRAME: ", valTextInit=g.frameList[g.frameId],
                                            initialComboValues=g.frameList, middileware_func=self.selectFrameIdFunc)

    #add framed widgets to frame
    self.selectFrameId.pack(side='top', expand=True, fill="both")


    #add label and frame to ImuRefSetupFrame
    self.label.pack(side="top", fill="x", padx=(250,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.3)
  

  def selectFrameIdFunc(self, frame_val_str):
    try:
      if frame_val_str:
        
        if frame_val_str == g.frameList[0]:
          isSuccessful = g.serClient.send("/frame-id", 0)
          
        elif frame_val_str == g.frameList[1]:
          isSuccessful = g.serClient.send("/frame-id", 1)
        
        if frame_val_str == g.frameList[2]:
          isSuccessful = g.serClient.send("/frame-id", 2)

    except:
      pass

    g.frameId = int(g.serClient.get("/frame-id"))
    return g.frameList[g.frameId]
