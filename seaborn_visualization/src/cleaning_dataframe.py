import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from time_bin import time_bin

def cleaning_data(trips_df):
    '''
    Cleaning the trips dataframe
        Input: Dataframe - raw data
        Output: Dataframe - cleaned data
    '''

    cleaned_df = trips_df.iloc[:, 1:]
    cleaned_df[['fare_amount','extra','mta_tax', 'tip_amount',
                'tolls_amount','improvement_surcharge', 'total_amount',
                'congestion_surcharge']] = cleaned_df[['fare_amount','extra','mta_tax',
                                                            'tip_amount','tolls_amount', 'improvement_surcharge',
                                                            'total_amount','congestion_surcharge']].abs()

    cleaned_df = cleaned_df[cleaned_df['passenger_count'] <= 6]
    cleaned_df.reset_index(inplace = True, drop = True)

    cleaned_df['tpep_pickup_datetime'] = pd.to_datetime(cleaned_df['tpep_pickup_datetime'])
    cleaned_df['tpep_dropoff_datetime'] = pd.to_datetime(cleaned_df['tpep_dropoff_datetime'])

    cleaned_df['pickup_time'] = cleaned_df['tpep_pickup_datetime'].dt.hour
    cleaned_df['dropoff_time'] = cleaned_df['tpep_dropoff_datetime'].dt.hour

    cleaned_df['pickup_bin'] = cleaned_df['pickup_time'].apply(time_bin)
    cleaned_df['dropoff_bin'] = cleaned_df['dropoff_time'].apply(time_bin)

    cleaned_df['pickup_bin'] = pd.Categorical(cleaned_df['pickup_bin'], ['22:00 to 4:00', '4:00 to 10:00', '10:00 to 16:00'])
    cleaned_df['dropoff_bin'] = pd.Categorical(cleaned_df['dropoff_bin'], ['22:00 to 4:00', '4:00 to 10:00', '10:00 to 16:00'])

    return cleaned_df