'''
Alex Brigger
Final Project
ISTA 350
'''
    
import kaggle
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

kaggle.api.authenticate()
kaggle.api.dataset_download_files("tayyarhussain/best-selling-video-games-of-all-time")
with zipfile.ZipFile('best-selling-video-games-of-all-time.zip') as zip1:
    zip1.extractall('data')
df = pd.read_csv('data/best-selling video games of all time.csv', index_col="Title")


def main():
    

    df1 = df['Sales'].copy().head(10)/1000000
    fig, ax = plt.subplots()
    df1.plot.bar(color="Green", ax=ax)
    plt.xticks(fontsize=10)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.xticks(rotation=75, fontsize = 7)
    plt.xlabel('Games', fontsize=14)
    plt.title(('Best Selling Video Games of All Time'), fontsize=24)
    plt.ylabel('Sales (in Millions)', fontsize=14)
    plt.gcf().set_facecolor('#afafaf')
    plt.show()

    df2 = df.copy()
    publisher_sales = df2.groupby('Publisher(s)')['Sales'].sum()
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(publisher_sales.values, labels=publisher_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('Total Sales by Publisher for Top 50 Games', size = 16)
    plt.tight_layout()
    plt.show()
    
    df3 = df.copy()
    df3['Initial release date'] = pd.to_datetime(df3['Initial release date'])
    df3 = df3.sort_values(by='Initial release date')

    yearly_sales = df3.groupby(df3['Initial release date'].dt.year)['Sales'].sum()


    x = yearly_sales.index
    y = yearly_sales.values
    plt.scatter(x=x, y=y, color='royalblue')

    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--")

    plt.xticks(rotation=45)
    plt.ylabel('Sales', size = "13")
    plt.xlabel('Year',size = "13")
    plt.title('Total Sales of Video Games Released That Year',size = "14")
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.set_facecolor("lightgrey")

    plt.show()


if __name__ == "__main__":
    main()
