import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *




class SelectValueFrame(tb.LabelFrame):
  def __init__(self, parentFrame, keyTextInit, valTextInit, initialComboValues=["None"], middileware_func=None):
    super().__init__(master=parentFrame, borderwidth=5, bootstyle='secondary')

    self.comboArrVal = initialComboValues
    self.comboVal = valTextInit

    self.middleware_func = middileware_func

    self.selected_val = tb.StringVar()

    # create widgets
    self.textFrame = tb.Frame(self)

    self.keyText = tb.Label(self.textFrame, text=keyTextInit, font=('Monospace',9, 'bold') ,bootstyle="danger")
    self.valText = tb.Label(self.textFrame, text=valTextInit, font=('Monospace',10), bootstyle="dark")

    self.selectFrame = tb.Frame(self)

  
    self.combobox = tb.Combobox(self.selectFrame, width=10,
                          font=('Monospace',10),
                          bootstyle="secondary",
                          values=self.comboArrVal,
                          textvariable=self.selected_val)
    self.combobox.set(self.comboVal)
    self.combobox.bind('<<ComboboxSelected>>', self.onSelect)
    


    # add widgets to Frames
    self.keyText.pack(side='left', fill='both')
    self.valText.pack(side='left', expand=True, fill='both')

    self.combobox.pack(side='left', expand=True, fill='both', pady=(5,0))

    self.textFrame.pack(side='top', expand=True, fill='x')
    self.selectFrame.pack(side='top', expand=True, fill='x')

  def setVal(self, value):
    self.valText.configure(text=value)
  
  def setComboVal(self, value):
    self.combobox.set(value)

  def setComboArrVal(self, values):
    self.combobox.configure(values=values)
  
  def getSelectedVal(self):
    value = self.selected_val.get()
    return value


  def onSelect(self, event):
    entryValue = self.selected_val.get()
    self.combobox.set(entryValue)

    if self.middleware_func == None:
      self.valText.configure(text="null")
    else:
      updatedValue = self.middleware_func(entryValue)
      self.valText.configure(text=str(updatedValue))




