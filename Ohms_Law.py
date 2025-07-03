# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
import inquirer
import os
from mpl_toolkits import mplot3d
from matplotlib.tri import Triangulation

# Ohm's Law
# I=V/R

questions = [
        inquirer.List('variable',
                      message="Which variable do you want to solve for?",
                      choices=['Solve for voltage in volts', 'Solve for resistance in Ohms', 'Solve for current in amps']),]
answers = inquirer.prompt(questions)
print(answers["variable"])
choice=answers["variable"]
if choice == 'Solve for voltage in volts':
   i = float(input("Enter the mass in kg: "))
   r = float(input("Enter the acceleration in m/s^2: "))
   v = i*r;
   print("The voltage is: ",v, " volts")
   x = np.linspace(0,i,100)
   y = np.linspace(0,r,100)
   z = np.linspace(0,v,100)
   fig = plt.figure()
   ax = plt.axes(projection='3d')
   ax.plot3D(x, y, z, 'green')
   ax.set_title('3D plot Ohms Law')
   plt.show()
elif choice == 'Solve for resistance in Ohms':
   i = float(input("Enter the current in amps: "))
   v = float(input("Enter the voltage in volts: "))
   r = v/i;
   print("The resistance is: ",r, " Ohms")
   x = np.linspace(0,i,100)
   y = np.linspace(0,v,100)
   z = np.linspace(0,r,100)
   fig = plt.figure()
   ax = plt.axes(projection='3d')
   ax.plot3D(x, y, z, 'green')
   ax.set_title('3D plot Ohms Law')
   plt.show()
elif choice == 'Solve for current in amps':
   v = float(input("Enter the mass in kg: "))
   r = float(input("Enter the acceleration in m/s^2: "))
   i = v/r;
   print("The current is: ",v, " amps")
   x = np.linspace(0,v,100)
   y = np.linspace(0,r,100)
   z = np.linspace(0,i,100)
   fig = plt.figure()
   ax = plt.axes(projection='3d')
   ax.plot3D(x, y, z, 'green')
   ax.set_title('3D plot Ohms Law')
   plt.show()
