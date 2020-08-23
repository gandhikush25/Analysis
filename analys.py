import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms



# 1) Run this part

#Merging two sheets

data = pd.read_csv('COVID-19_Nursing_Home_Dataset.csv') # required in your folder
data_2 = pd.read_csv('Star_Ratings.csv')  # required in your folder
sheets = [data,data_2]

merged_sheets = pd.concat(sheets,ignore_index=True)
x = merged_sheets.to_csv("output.csv")


# 2) Now run this part

# getting a merged sheet
data_1 = pd.read_csv('output.csv')

# I have changed Total Number of Occupied Beds to  TotalNumberofOccupiedBeds
# and Number of All Beds to NumberofAllBeds while creating the new column percent_of_occupbed

# Adding a new column
data_1['percent_of_occupbed'] = (data_1.TotalNumberofOccupiedBeds / data_1.NumberofAllBeds) * 100



#Plotting

#Figure_1
ax = data_1.plot.scatter(x= 'Provider State',y='TotalNumberofOccupiedBeds',label="bedoccupied")
data_1.plot.scatter(x='Provider State',y='Residents Total Confirmed COVID-19',label="Confirmed COVID-19",color="green" ,ax =ax)
plt.title("States Vs NumberofBed and Confirmed COVID-19 ")


#Figure_2
ax = data_1.plot.scatter(x= 'Provider State',y='NumberofAllBeds',label="Totalbeds",color='orange')
data_1.plot.scatter(x='Provider State',y='percent_of_occupbed',label="percent",color="green" ,ax =ax)

line = mlines.Line2D([0, 1], [0, 1], color='red')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)

plt.title("States Vs NumberofBed and '%'ofOccupBed ")


plt.show()



