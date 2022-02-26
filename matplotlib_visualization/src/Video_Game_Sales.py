# Analyzing and visualizing Video Game Sales file

import pandas as pd
import matplotlib.pyplot as plt
from console_wii import wii_best_year
from publisher_atari import atari_regional_sales

file_path = ("C:\\Users\Jonathan\Desktop\Jupyter_Notebook\GitHub_Files\matplotlib_visualization\dataset\Video_Games_Sales.csv")

def create_dataframe(file_path):
    df = pd.read_csv(file_path)
    return df

video_game_sales_df = create_dataframe(file_path)



def dataset_analysis(video_game_sales_df):
    wii_best_year(video_game_sales_df)
    atari_regional_sales(video_game_sales_df)


if __name__ == "__main__":
    dataset_analysis(video_game_sales_df)