# Analyzing and visualizing Video Game Sales file

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Video Games Sales.csv")


# Q1 - The year with the highest global sales is 2009. 'Blank' year has been left in the chart for reference

df_1_platform = df[df['Platform'] == 'Wii']
df_1_columns = df_1_platform[['Year_of_Release', 'Global_Sales']]
df_1_final = df_1_columns.groupby("Year_of_Release", dropna = False)['Global_Sales'].sum()

df_1_final.plot.bar(title = "Wii Yearly Global Sales",
                    ylabel = "Global Sales",
                    xlabel = "Year of Release",
                    y="Global_Sales",
                    figsize=(20,10))


# Q2 - Sales of Atari over time for each region

df_2_publisher = df[df['Publisher'] == 'Atari']
df_2_columns = df_2_publisher[['Year_of_Release','NA_Sales','EU_Sales','JP_Sales']]
df_2_final = df_2_columns.groupby("Year_of_Release", dropna=True)['NA_Sales', 'EU_Sales', 'JP_Sales'].sum()
df_2_final = df_2_final.reset_index()

ax = df_2_final.plot(kind = "line", x = "Year_of_Release", y = "EU_Sales", color = "b", label = "EU_Sales", figsize=(20,10))
df_2_final.plot(kind = "line", x = "Year_of_Release", y = "NA_Sales", color = "g", label = "US_Sales", ax = ax)
df_2_final.plot(kind = "line", x = "Year_of_Release", y = "JP_Sales", color = "r", label = "JP_Sales", ax = ax)

ax.set_xlabel("Year Of Release")
ax.set_ylabel("Sales")
ax.set_title("Yearly Atari Sales by Region")
plt.show()
