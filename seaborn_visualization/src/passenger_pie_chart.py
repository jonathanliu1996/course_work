import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def passenger_pie_chart(cleaned_df):
    '''
    Creating a pie chart to showcase passenger count and %
    Input: Dataframe (cleaned)
    Output: Piecharts
    '''

    sns.set(rc={'figure.figsize':(7,7)})

    pie_chart_df = cleaned_df['passenger_count'].value_counts().rename_axis("passenger_count").reset_index(name="occurence")
    pie_chart_df = pie_chart_df.astype('int')

    passenger_count_graph = pie_chart_df['occurence']
    labels = pie_chart_df['passenger_count']
    plt.pie(passenger_count_graph, labels = labels, autopct = '%.0f%%', textprops={'fontsize':15})
    plt.title("Count of # of passengers", fontsize = 20)

    plt.show()