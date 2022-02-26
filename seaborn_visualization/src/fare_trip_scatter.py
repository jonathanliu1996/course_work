import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fare_trip_scatter(cleaned_df):
    '''
    Creating a scatter plot to showcase fare amount vs trip distance
        Input: Dataframe (cleaned)
        Output: Scatter plot
    '''
    
    sns.relplot(data=cleaned_df['fare_amount'], x = cleaned_df['trip_distance'], y=cleaned_df['fare_amount'])
    plt.show()