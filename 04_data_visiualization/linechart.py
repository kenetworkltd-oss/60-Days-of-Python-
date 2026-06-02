#Line Chart

import matplotlib.pyplot as plt #import matplot lib/mod to draw the chart and do the label

import numpy 

months = ["Janury", "Febuary", "March", "April", "May"] #data for the chart

Sales = [500, 300, 400, 200, 100] #data for the chart

plt.plot(months, Sales, linestyle = "solid", color = "red", marker = "o")  #Calling and styling the plot (plt.plot/line)

plt.title("Monthly Sales in 2025") #Title of the whole chart

plt.xlabel("The Months") #label for X line

plt.ylabel("The Sales") #label for y line

plt.show( )  #The display or print of the chart