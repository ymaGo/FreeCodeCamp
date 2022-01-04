import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df.drop(df[(df['value'] < df['value'].quantile(0.025)) | (df['value'] > df['value'].quantile(0.975))].index)

def draw_line_plot():
      # Draw line plot
    fig=plt.figure(figsize=(15,5),dpi=100)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.plot(df.index.values,df.value,color='r')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.copy()
    df_bar["year"] = pd.to_datetime(df_bar.index.values).year
    df_bar["month"] = pd.to_datetime(df_bar.index.values).month
    labels=['January','February','March','April','May','June','July','August','September','October','November','December']
    # Create new dataframe column with the labels instead of numbers
    df_bar["std_month"] = df_bar["month"].map(dict(zip(range(1,13), labels)))

    df_bar.groupby(['year', 'std_month'])['value'].mean().reset_index()
    
    # plot barplot
    fig=plt.figure(figsize=(10,6))
    sns.barplot(x='year',
                y="value",
               hue="std_month",
                hue_order=labels,
               data=df_bar)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box["year"] = pd.to_datetime(df_box.index.values).year
    df_box["month"] = pd.to_datetime(df_box.index.values).month
    labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Create new dataframe column with the labels instead of numbers
    df_box["std_month"] = df_box["month"].map(dict(zip(range(1,13), labels)))

    # Draw box plots (using Seaborn)
    fig,axes=plt.subplots(1,2,figsize=(30,10))
    L=sns.boxplot(x="year",y="value",data=df_box,ax=axes[0]) #左图
    L.set(title='Year-wise Box Plot (Trend)')
    L.set(xlabel='Year')
    L.set(ylabel='Page Views')
    R=sns.boxplot(x="std_month",y="value",data=df_box,ax=axes[1],order=labels) #右图
    R.set(title="Month-wise Box Plot (Seasonality)")
    R.set(xlabel='Month')
    R.set(ylabel='Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig