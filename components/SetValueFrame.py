import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *




class SetValueFrame(tb.LabelFrame):
  def __init__(self, parentFrame, keyTextInit, valTextInit, middleware_func=None):
    super().__init__(master=parentFrame, borderwidth=5, bootstyle='secondary')

    self.middleware_func = middleware_func

    # create widgets
    self.textFrame = tb.Frame(self)

    self.keyText = tb.Label(self.textFrame, text=keyTextInit, font=('Monospace',9, 'bold') ,bootstyle="danger")
    self.valText = tb.Label(self.textFrame, text=valTextInit, font=('Monospace',10), bootstyle="dark")

    self.setFrame = tb.Frame(self)

    self.entry = tb.Entry(self.setFrame, width=8, font=('Monospace',10),
                          bootstyle="secondary")
    
    buttonStyle = tb.Style()
    buttonStyleName = 'primary.TButton'
    buttonStyle.configure(buttonStyleName, font=('Monospace',8,'bold'))
    self.button = tb.Button(self.setFrame, text="SET", style=buttonStyleName,
                            command=self.onClick)


    # add widgets to Frames
    self.keyText.pack(side='left', fill='both')
    self.valText.pack(side='left', expand=True, fill='both')

    self.entry.pack(side='left', expand=True, fill='both', padx=0.5, pady=(5,0))
    self.button.pack(side='left', fill='both', pady=(5,0))

    self.textFrame.pack(side='top', expand=True, fill='x')
    self.setFrame.pack(side='top', expand=True, fill='x')


  def onClick(self):
    entryValue = self.entry.get()
    if self.middleware_func == None:
      self.valText.configure(text="null")
    else:
      updatedValue = self.middleware_func(entryValue)
      self.valText.configure(text=str(updatedValue))
    




