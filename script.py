import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# rankings data:
wood_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_rankings = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood_rankings.head)
print(steel_rankings.head)

# function to plot rankings over time for 1 roller coaster here:
def plot_coaster_rankings(coaster_name, park_name, rankings_df):
    coaster_rankings = rankings_df[(rankings_df['Name'] == coaster_name) & (rankings_df['Park'] == park_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    ax.set_xticks(coaster_rankings['Year of Rank'].values)
    ax.set_yticks(coaster_rankings['Rank'].values)
    ax.invert_yaxis()
    plt.title('{} from {} Rankings'.format(coaster_name, park_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()

    # test:
plot_coaster_rankings('El Toro', 'Six Flags Great Adventure', wood_rankings)
plt.clf()

# function to plot rankings over time for 2 roller coasters:
def plot_2_coasters_rankings(coaster_1_name, park_1_name, coaster_2_name, park_2_name, rankings_df):
    coaster_rankings_1 = rankings_df[(rankings_df['Name'] == coaster_1_name) & (rankings_df['Park'] == park_1_name)]
    coaster_rankings_2 = rankings_df[(rankings_df['Name'] == coaster_2_name) & (rankings_df['Park'] == park_2_name)]
    fig, ax = plt.subplots()
    ax.plot(coaster_rankings_1['Year of Rank'], coaster_rankings_1['Rank'], label=coaster_1_name)
    ax.plot(coaster_rankings_2['Year of Rank'], coaster_rankings_2['Rank'], label=coaster_2_name)
    ax.invert_yaxis()
    plt.title('{} vs {} Rankings'.format(coaster_1_name, coaster_2_name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend()
    plt.show()

    # test:
plot_2_coasters_rankings('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood_rankings)
plt.clf()

# function to plot top n rankings over time:
def plot_top_n_coasters(n, rankings_df):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(10,10))
    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
    ax.invert_yaxis()
    ax.set_yticks([i for i in range(1, n+1)])
    plt.title('Top {} Rankings'.format(n))
    plt.legend(loc=4)
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()

    # test:
plot_top_n_coasters(5, wood_rankings)
plt.clf()

# load roller coaster data:
roller_coasters = pd.read_csv('roller_coasters.csv')

# function to plot histogram of column values:
def plot_histogram(coaster_df, column_name):
    plt.hist(coaster_df[column_name].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

    # test:
plot_histogram(roller_coasters, 'length')
plt.clf()

# function to plot inversions by coaster at a park:
def plot_inversions_by_coaster(coaster_df, park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    plt.bar(range(len(number_inversions)), number_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=90)
    plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('# of Inversions')
    plt.show()

    # test:
plot_inversions_by_coaster(roller_coasters, 'Six Flags Great Adventure')
plt.clf()

# function to plot pie chart of operating status:
def pie_chart_status(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)
    status_counts = [num_operating_coasters, num_closed_coasters]
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.show()

    # test:
pie_chart_status(roller_coasters)
plt.clf()

# function to create scatter plot of any two numeric columns:
def plot_scatter(coaster_df, column_1, column_2):
    plt.scatter(coaster_df[column_1], coaster_df[column_2])
    plt.title('Scatter Plot of {} vs. {}'.format(column_1, column_2))
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.show()

    # test:
plot_scatter(roller_coasters, 'speed', 'manufacturer')
plt.clf()

# function to create plot histogram of height values:
def plot_height_hist(coaster_df, less_than):
    heights = coaster_df[coaster_df['height'] <= less_than]['height'].dropna()
    plt.hist(heights)
    plt.title('Histogram of Roller Coaster Height')
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.show()
    
    # test:    
plot_height_hist(roller_coasters, 140)
plt.clf()  