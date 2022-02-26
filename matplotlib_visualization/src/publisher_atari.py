import pandas as pd
import matplotlib.pyplot as plt

def atari_regional_sales(video_game_sales_df):
    '''
    Printing a line graph for yearly Atari sales, by NA, EU and JP region
        Input: DataFrame
        Output: Matplotlib line graph
        Results: JP had more sales compared to the other 2 regions, with a peak of ~17.6m sales in 1983
    '''

    atari_df = video_game_sales_df[video_game_sales_df['Publisher'] == 'Atari']

    atari_df = atari_df[['Year_of_Release','NA_Sales','EU_Sales','JP_Sales']]

    atari_yearly_df = atari_df.groupby("Year_of_Release", dropna=True)['NA_Sales', 'EU_Sales', 'JP_Sales'].sum()

    atari_yearly_df.reset_index(inplace = True)

    ax = atari_yearly_df.plot(kind = "line", x = "Year_of_Release", y = "EU_Sales", color = "b", label = "EU_Sales", zorder=3)
    atari_yearly_df.plot(kind = "line", x = "Year_of_Release", y = "NA_Sales", color = "g", label = "US_Sales", ax = ax)
    atari_yearly_df.plot(kind = "line", x = "Year_of_Release", y = "JP_Sales", color = "r", label = "JP_Sales", ax = ax)

    ax.set_xlabel("Year Of Release")
    ax.set_ylabel("Sales (Millions)")
    ax.set_title("Yearly Atari Sales (By Region)")
    plt.grid(alpha = 0.5, zorder=0)
    plt.show()