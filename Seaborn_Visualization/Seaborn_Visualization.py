# Seaborn visualization of trips.csv file to analyze passenger pick up / drop off time, passenger count, and distance vs fare

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("trips.csv")

df_clean = df.iloc[:, 1:]
df_clean[['fare_amount','extra','mta_tax', 'tip_amount','tolls_amount','improvement_surcharge','total_amount',
    'congestion_surcharge']] = df_clean[['fare_amount','extra','mta_tax','tip_amount','tolls_amount',
                                   'improvement_surcharge', 'total_amount','congestion_surcharge']].abs()

df_clean = df_clean[df_clean['passenger_count'] <= 6]
df_clean.reset_index(inplace = True, drop = True)

df_clean['tpep_pickup_datetime'] = pd.to_datetime(df_clean['tpep_pickup_datetime'])
df_clean['tpep_dropoff_datetime'] = pd.to_datetime(df_clean['tpep_dropoff_datetime'])

df_clean['pickup_time'] = df_clean['tpep_pickup_datetime'].dt.hour
df_clean['dropoff_time'] = df_clean['tpep_dropoff_datetime'].dt.hour

def time_bin(x):
    if (x >= 4 and x < 10):
        return "4:00 to 10:00"
    elif (x >= 10 and x < 16):
        return "10:00 to 16:00"
    else:
        return "22:00 to 4:00"

df_clean['pickup_bin'] = df_clean['pickup_time'].apply(time_bin)
df_clean['dropoff_bin'] = df_clean['dropoff_time'].apply(time_bin)

df_clean['pickup_bin'] = pd.Categorical(df_clean['pickup_bin'], ['22:00 to 4:00', '4:00 to 10:00', '10:00 to 16:00'])
df_clean['dropoff_bin'] = pd.Categorical(df_clean['dropoff_bin'], ['22:00 to 4:00', '4:00 to 10:00', '10:00 to 16:00'])


#1a. Visualizing bins for pickup and dropoff hours
pickup_bin = df_clean['pickup_bin']
sns.displot(pickup_bin)
plt.title("Pick up hours")
plt.xlabel("Bin")

dropoff_bin = df_clean['dropoff_bin']
sns.displot(dropoff_bin)
plt.title("Drop off hours")
plt.xlabel("Bin")

plt.show()


# #1b. Creating pie chart for passenger count
sns.set(rc={'figure.figsize':(10,10)})

df_pie_chart = df_clean['passenger_count'].value_counts().rename_axis("passenger_count").reset_index(name="occurence")
df_pie_chart = df_pie_chart.astype('int')

passenger_count_graph = df_pie_chart['occurence']
labels = df_pie_chart['passenger_count']
plt.pie(passenger_count_graph, labels = labels, autopct = '%.0f%%', textprops={'fontsize':15})
plt.title("Count of # of passengers", fontsize = 25)

plt.show()


#1c. Scatter plot of fare amount vs trip distance
sns.relplot(data=df_clean['fare_amount'], x = df_clean['trip_distance'], y=df_clean['fare_amount'])
