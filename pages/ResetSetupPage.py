import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from termcolor import colored
import time

from globalParams import g


class ResetSetupFrame(tk.Frame):
  def __init__(self, parentFrame):
    super().__init__(master=parentFrame)

    self.label = tb.Label(self, text="RESET ALL PARAMETERS", font=('Monospace',16, 'bold') ,bootstyle="dark")
    self.frame = tb.Frame(self)

    #create widgets to be added to frame1
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',10,'bold'))
    self.resetButton = tb.Button(self.frame, text="RESET ALL PARAMETERS",
                               style=buttonStyleName, padding=20,
                               command=self.open_reset_dialog_event)

    #add framed widgets to frame
    self.resetButton.pack(side='top', expand=True, fill="both")

    #add frame1, frame2 and frame3 to MainFrame
    self.label.pack(side="top", fill="x", padx=(220,0), pady=(5,0))
    self.frame.place(relx=0.5, rely=0.5, anchor="center")


  def open_reset_dialog_event(self):
    dialog = Messagebox.show_question(title="RESET WARNING!!!", message="This will reset all parameters on the controller's EEPROM to default.\nAre you sure you want to continue?")

    if dialog == "Yes":
      isSuccessful = self.resetAllParams()
      if isSuccessful:
        Messagebox.show_info("SUCCESS:\n\nParameters Reset was successful", "SUCCESS")
        print(colored("SUCCESS:\n\nParameters Reset was successful", 'green'))
      else:
        Messagebox.show_error("ERROR:\n\nSomething went wrong\nAttempt to reset was unsuccessful\nTry again", "ERROR")
        print(colored("ERROR:\n\nSomething went wrong\nAttempt to reset was unsuccessful\nTry again", 'red'))


  def resetAllParams(self):
    isSuccessful = g.serClient.send("/reset")
    return isSuccessful
