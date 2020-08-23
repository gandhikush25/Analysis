import pandas as pd 
import matplotlib.pyplot as plt 


data_1 = pd.read_csv('output.csv')


data_1['percent_of_occupbed'] = (data_1.TotalNumberofOccupiedBeds / data_1.NumberofAllBeds) * 100

#Figure_3
ax = data_1.plot.scatter(x ="Provider State",y = 'Residents Total COVID-19 Deaths',label='Deaths',color='lightblue')
data_1.plot.scatter(x='Provider State',y='Staffing Rating Footnote',label='Staff Ratings',color='orange',ax=ax)
plt.title("States Vs Total COVID-19 Death and Staff Ratings ")

#Figure_4
ax = data_1.plot.scatter(x='Provider State',y='Residents Total Suspected COVID-19',color='yellow',label="Total_Cases")
data_1.plot.scatter(x = 'Provider State', y = 'Overall Rating Footnote',color='blue',label="Overall Rating",ax=ax)
plt.title("States Vs Total Suspected COVID-19 and Overall Rating ")


plt.show()