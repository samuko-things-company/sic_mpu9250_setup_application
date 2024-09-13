
import serial
import time

class SerialComm:
  
  def __init__(self, port, baud=115200, timeOut=0.1):
    self.ser = serial.Serial(port, baud, timeout=timeOut)

  def send_msg(self, msg_to_send):
    data = ""
    prev_time = time.time()
    while data=="":
      try:
        self.ser.write(msg_to_send.encode())   # send a single or multiple byte    
        data = self.ser.readline().decode().strip()
        if time.time()-prev_time > 2.0:
          raise Exception("Error getting response from arduino nano, wasted much time \n")
      except:
        raise Exception("Error getting response from arduino nano, wasted much time \n")
    return data

  
  def send(self, cmd_route, val1=0, val2=0, val3=0, val4=0):
    cmd_str = cmd_route+","+str(val1)+","+str(val2)+","+str(val3)+","+str(val4)
    data = self.send_msg(cmd_str)
    if data == "1":
      return True
    else:
      return False
  
  
  def get(self, cmd_route):
    data = self.send_msg(cmd_route).split(',')
    if len(data)==1:
      return float(data[0])
    elif len(data)==2:
      return float(data[0]), float(data[1])
    elif len(data)==3:
      return float(data[0]), float(data[1]), float(data[2])
    elif len(data)==4:
      return float(data[0]), float(data[1]), float(data[2]), float(data[3])