import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pickup_dropoff(cleaned_df):
    '''
    Visualizing bins for pickup and drop off hours
        Input: Dataframe (cleaned)
        Output: Matplotlib charts
    '''

    pickup_bin = cleaned_df['pickup_bin']
    sns.displot(pickup_bin)
    plt.title("Pick up hours")
    plt.xlabel("Bin")

    dropoff_bin = cleaned_df['dropoff_bin']
    sns.displot(dropoff_bin)
    plt.title("Drop off hours")
    plt.xlabel("Bin")

    plt.show()