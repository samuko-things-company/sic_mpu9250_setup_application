# sic_mpu9250_setup_application
This is a child project of the Samuko IMU Compute for MPU9250 (**`sic_mpu9250`**) project. It contains source code of its GUI application. The application requires that you have the **`sic_mpu9250_driver module`** is connected to your PC via the FTDI programmer for USB serial communication. Without the module, only the start page can be viewed.

## Run the GUI app
- Ensure you have python3 installed on your PC

- Download (by clicking on the green Code button above) or clone the repo into your PC
	> you can use this command if you want to clone the repo:
  >
	> ```git clone https://github.com/samuko-things-company/sic_mpu9250_setup_application.git```

- Ensure you have the **`sic_mpu9250_driver module`** interfaced with the MPU9250 module and connected to the PC.

- Install the following python packages before you run the application
	> PySerial:
	> ```pip3 install pyserial```
  >
	> [tkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/):
	> ```pip3 install ttkbootstrap```
  >
  > Matplotlib:
	> ```pip3 install matplotlib```
  >
  > Termcolor:
	> ```pip3 install termcolor```
  >
  > VPython:
	> ```pip3 install vpython```

- In the root folder run the `main.py`
	> ```python3 main.py```