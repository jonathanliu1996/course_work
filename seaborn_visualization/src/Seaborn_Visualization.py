#Seaborn visualization of trips.csv file to analyze passenger pick up / drop off time, passenger count, and distance vs fare

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from time_bin import time_bin
from cleaning_dataframe import cleaning_data
from pickup_dropoff_bins import pickup_dropoff
from passenger_pie_chart import passenger_pie_chart
from fare_trip_scatter import fare_trip_scatter



file = "C:\\Users\\Jonathan\\Desktop\\Jupyter_Notebook\\GitHub_Files\\seaborn_visualization\\dataset\\trips.csv"


def read_data(file):
    trips_df = pd.read_csv(file)
    return trips_df


trips_df = read_data(file)

#Calling method to clean the trips_df
cleaned_df = cleaning_data(trips_df)


def creating_charts(cleaned_df):
    '''
    Using cleaned dataframe to create charts
        Input: Dataframe (cleaned)
        Output: Calling methods for histogram, piechart, and scatter plot
    '''
    
    pickup_dropoff(cleaned_df)
    passenger_pie_chart(cleaned_df)
    fare_trip_scatter(cleaned_df)


if __name__ == "__main__":
    read_data(file)
    creating_charts(cleaned_df)



