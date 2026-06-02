#Bar Chart

import matplotlib.pyplot as plt #import matplot lib/mod to draw the chart and do the label
import numpy

workers = ["Joe", "Mark", "Mike", "Dare", "Kai"] #Data in list

salary = [ 2000, 9000, 4000, 6000, 2500 ] #Data in list

plt.bar(workers, salary, color = "red")  #Calling and styling the bar chart (plt.bar)

plt.title("The Paystub") #Title of the bar chart

plt.xlabel("Names of workers") #label for wx

plt.ylabel("Amount") #label for  y line 

plt.show( )  #The display or print of the bar chart