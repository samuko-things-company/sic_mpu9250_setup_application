import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from globalParams import g
from pages.SerialConnectPage import SerialConnectFrame
from pages.MainAppPage import MainAppFrame



class App(tb.Window):
  def __init__(self, title, size):
    super().__init__()
    self.title(title)
    self.geometry(f'{size[0]}x{size[1]}')
    self.resizable(False,False)

    self.windowFrame = tb.Frame(self)
    self.windowFrame.pack(side="left", expand=True, fill='both')

    #####################################################################################
    self.connectToPortFrame = SerialConnectFrame(self.windowFrame, next_func=self.startMainApp)
    self.connectToPortFrame.pack(side="left", expand=True, fill="both", pady=(0,10))
    #####################################################################################

  # def startMainApp(self):
  #   self.delete_pages()
  #   self.mainAppFrame = tb.Frame(self.windowFrame)
  #   self.label = tb.Label(self.mainAppFrame, text="MENU", font=('Monospace',20, 'bold') ,bootstyle="secondary")
  #   self.label.pack(side="top", fill="x", padx=(40,0), pady=(0,25))
  #   self.mainAppFrame.pack(side="left", expand=True, fill="both", pady=(0,10))
  
  def startMainApp(self):
    self.delete_pages()
    self.mainAppFrame = MainAppFrame(self.windowFrame)
    self.mainAppFrame.pack(side="left", expand=True, fill="both", pady=(0,10))

  def delete_pages(self):
    for frame in self.windowFrame.winfo_children():
      frame.destroy()





if __name__ == "__main__":
  g.app = App(title="My Test GUI App", size=(900,650))
  g.app.mainloop()