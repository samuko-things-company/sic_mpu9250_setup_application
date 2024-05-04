# smc_app
This is a child project of the Samuko Motor Control (**`smc`**) project. It contains source code of its GUI application. The application requires that you have the **`smc_l298n_pid_driver module`** is connected to your PC via the FTDI programmer for USB serial communication. Without the module, only the start page can be viewed.

### App Demo
![](./docs/smc_app_overview.gif)

## Run the GUI app
- Ensure you have python3 installed on your PC

- Download (by clicking on the green Code button above) or clone the repo into your PC
	> you can use this command if you want to clone the repo:
  >
	>  ```git clone https://github.com/samuko-things-company/smc_app.git``` 

- Ensure you have the **`smc_l298n_pid_driver module`** interfaced with your preferred motors and connected to the PC.

- Install the following python packages before you run the application
	> PySerial:
	> ```pip3 install pyserial``` 
  >
	> [tkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/installation/):
	>  ```pip3 install ttkbootstrap``` 

- In the root folder run the `main.py`
	>  ```python3 main.py``` 