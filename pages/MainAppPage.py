import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from pages.I2CSetupPage import I2CSetupFrame
from pages.ResetSetupPage import ResetSetupFrame
from pages.GainSetupVizPage import GainSetupVizFrame
from pages.CalibrateGyroPage import CalibrateGyroFrame
from pages.CalibrateAccPage import CalibrateAccFrame
from pages.CalibrateMagPage import CalibrateMagFrame
from pages.ComputeGyroVariancePage import ComputeGyroVarFrame
from pages.ComputeAccVariancePage import ComputeAccVarFrame
from pages.ComputeAngleVariancePage import ComputeAngleVarFrame
from pages.ImuFrameSetupPage import ImuRefSetupFrame




class MainAppFrame(tb.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)


    # SIDEBAR NAVIGATION FRAME
    self.sideNavFrame = tb.LabelFrame(self, borderwidth=10)

    # MIAN CONTENT FRAME
    self.mainContentFrame = tb.Frame(self)


    #create widgets to be added to the sideNavFrame
    self.label = tb.Label(self.sideNavFrame, text="MENU", font=('Monospace',20, 'bold') ,bootstyle="secondary")

    buttonStyle = tb.Style()
    buttonStyleName = 'primary.Link.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',12, 'bold'))

    self.button1 = tb.Button(self.sideNavFrame, text="RESET PARAMS", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button1, self.displayResetPage))
    
    self.button2 = tb.Button(self.sideNavFrame, text="CHANGE FRAME", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button2, self.displayImuFrameSetupPage))
    
    self.button3 = tb.Button(self.sideNavFrame, text="CALIBRATE MAG", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button3, self.displayCalibrateMagPage))
    
    self.button4 = tb.Button(self.sideNavFrame, text="CALIBRATE GYR", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button4, self.displayCalibrateGyroPage))
    
    self.button5 = tb.Button(self.sideNavFrame, text="CALIBRATE ACC", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button5, self.displayCalibrateAccPage))
    
    self.button6 = tb.Button(self.sideNavFrame, text="VIZUALIZE GAIN", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button6, self.displayGainSetupVizPage))
    
    self.button7 = tb.Button(self.sideNavFrame, text="RPY VARIANCE", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button7, self.displayComputeAngleVariancePage))
    
    self.button8 = tb.Button(self.sideNavFrame, text="GYR VARIANCE", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button8, self.displayComputeGyroVariancePage))
    
    self.button9 = tb.Button(self.sideNavFrame, text="ACC VARIANCE", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button9, self.displayComputeAccVariancePage))
    
    self.button10 = tb.Button(self.sideNavFrame, text="I2C SETUP", style=buttonStyleName,
                             command= lambda: self.displayPage(self.button10, self.displayI2CSetupPage))
    
    
    
    
    
    
    # add widget to sideNavFrame
    self.label.pack(side="top", fill="x", padx=(40,0), pady=(0,25))
    self.button1.pack(side="top", fill="x", padx=5, pady=10)
    self.button2.pack(side="top", fill="x", padx=5, pady=10)
    self.button3.pack(side="top", fill="x", padx=5, pady=10)
    self.button4.pack(side="top", fill="x", padx=5, pady=10)
    self.button5.pack(side="top", fill="x", padx=5, pady=10)
    self.button6.pack(side="top", fill="x", padx=5, pady=10)
    self.button7.pack(side="top", fill="x", padx=5, pady=10)
    self.button8.pack(side="top", fill="x", padx=5, pady=10)
    self.button9.pack(side="top", fill="x", padx=5, pady=10)
    self.button10.pack(side="top", fill="x", padx=5, pady=10)

    
    ############Initialize the mainContentFrame ################
    self.displayPage(self.button1, self.displayResetPage)
    ############################################################


    #add framed widgets to MainAppFrame
    self.sideNavFrame.pack(side="left", fill="y", padx=10)
    self.mainContentFrame.pack(side="left", expand=True, fill="both", padx=5)


  
  def enable_all_nav_buttons(self):
    self.button1.configure(state="normal")
    self.button2.configure(state="normal")
    self.button3.configure(state="normal")
    self.button4.configure(state="normal")
    self.button5.configure(state="normal")
    self.button6.configure(state="normal")
    self.button7.configure(state="normal")
    self.button8.configure(state="normal")
    self.button9.configure(state="normal")
    self.button10.configure(state="normal")
  
  def displayPage(self, button, page):
    self.enable_all_nav_buttons()
    button.configure(state='disabled') # disable the clicked nav button
    self.delete_pages()
    page()

  def delete_pages(self):
    for frame in self.mainContentFrame.winfo_children():
      frame.destroy()


  def displayResetPage(self):
    self.resetFrame = ResetSetupFrame(self.mainContentFrame)
    self.resetFrame.pack(side="left", expand=True, fill="both")

  def displayImuFrameSetupPage(self):
    self.imuRefFrame = ImuRefSetupFrame(self.mainContentFrame)
    self.imuRefFrame.pack(side="left", expand=True, fill="both")
  
  def displayI2CSetupPage(self):
    self.i2cSetupFrame = I2CSetupFrame(self.mainContentFrame)
    self.i2cSetupFrame.pack(side="left", expand=True, fill="both")

  def displayGainSetupVizPage(self):
    self.i2cSetupFrame = GainSetupVizFrame(self.mainContentFrame)
    self.i2cSetupFrame.pack(side="left", expand=True, fill="both")

  def displayCalibrateGyroPage(self):
    self.calibrateGyroFrame = CalibrateGyroFrame(self.mainContentFrame)
    self.calibrateGyroFrame.pack(side="left", expand=True, fill="both")

  def displayCalibrateAccPage(self):
    self.calibrateAccFrame = CalibrateAccFrame(self.mainContentFrame)
    self.calibrateAccFrame.pack(side="left", expand=True, fill="both")

  def displayCalibrateMagPage(self):
    self.calibrateMagFrame = CalibrateMagFrame(self.mainContentFrame)
    self.calibrateMagFrame.pack(side="left", expand=True, fill="both")

  def displayComputeGyroVariancePage(self):
    self.computeGyroVarianceFrame = ComputeGyroVarFrame(self.mainContentFrame)
    self.computeGyroVarianceFrame.pack(side="left", expand=True, fill="both")

  def displayComputeAccVariancePage(self):
    self.computeAccVarianceFrame = ComputeAccVarFrame(self.mainContentFrame)
    self.computeAccVarianceFrame.pack(side="left", expand=True, fill="both")

  def displayComputeAngleVariancePage(self):
    self.computeAngleVarianceFrame = ComputeAngleVarFrame(self.mainContentFrame)
    self.computeAngleVarianceFrame.pack(side="left", expand=True, fill="both")