#PIE CHART
import matplotlib.pyplot as plt

country = ["Nigeria", "Ghana", "Rwanda", "Kenya", "Chad"]
no_of_lang = [92, 40, 50, 30, 20]
colors = ["skyblue", "gold", "red", "green", "yellow"]


plt.pie(no_of_lang, labels=country, autopct='%1.1f%%', startangle=140)
plt.axis("equal") #making sure the circle shape are in equal size, no part is more bigger than any other
plt.show() #display or print the pie chart