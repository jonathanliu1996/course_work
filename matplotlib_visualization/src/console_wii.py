import pandas as pd
import matplotlib.pyplot as plt

def wii_best_year(video_game_sales_df):
    '''
    Printing a bar chart of wii sales by year
        Input: Dataframe
        Output: Matplotlib bar chart
        Results: The year with the highest global sales is 2009. 'Blank' year (NaN) has been left in the chart for reference
    '''

    wii_df = video_game_sales_df[video_game_sales_df['Platform'] == 'Wii']
    wii_df = wii_df[['Year_of_Release', 'Global_Sales']]
    wii_df['Year_of_Release'] = wii_df['Year_of_Release'].astype('Int64')

    wii_year_df = wii_df.groupby("Year_of_Release", dropna = False)['Global_Sales'].sum()

    wii_year_df.plot.bar(title = "Wii Yearly Global Sales",
                        ylabel = "Global Sales",
                        xlabel = "Year of Release",
                        y="Global_Sales",
                        zorder = 3)
    plt.xticks(rotation = 45)
    plt.grid(alpha = 0.5, zorder = 0)
    plt.show()