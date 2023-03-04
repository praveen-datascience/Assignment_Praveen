import pandas as pd
import matplotlib.pyplot as plt

#read csv file
df_crime = pd.read_csv("nationality_and_offence2.csv")
#check first 5 rows
print(df_crime.head())
#Check for missing values
missing_val = df_crime.isnull().sum()



def calc_cumulative_Crime():
    """ This function is used to group the data based on different countries
        so that it can be reusable for different plots.
    """
    #group results based on Countries column
    df_crime_countries = df_crime.groupby('Countries')
    #calculate the total crime
    df_sum_crime = df_crime_countries['Total'].sum()
    #set a name for the unnamed calculated column
    final_sum_crime = df_sum_crime.reset_index(name='Cumulative Crime')
    return final_sum_crime
    
def plot_top_n_unsafest_countries(n):
    """ This function is used to take number value n as an argument
        and find out the top n Unsafest Countries.
        Here I used pie chart to display cumulative values based on
        countries
    """
    final_sum_crime = calc_cumulative_Crime()
    #order the values based on descending order
    final_sum_crime_sorted = final_sum_crime.sort_values(by='Cumulative Crime', ascending=False)
    #take top n values
    top_n = final_sum_crime_sorted.head(n).set_index('Countries')
    return top_n
        

userchoice = int( input("Enter number of countries : "))
top_n = plot_top_n_unsafest_countries(userchoice)
plt.pie(top_n["Cumulative Crime"], labels=top_n.index, autopct='%1.1f%%')
plt.title(f"Top {userchoice} Unsafest Countries in between 2009-2012 \n (Based on Total Crime % )")
plt.show()

def plot_diff_crimes_in_unsafest_country():
    """ This function is used to  find out the 4 different crimes in Most dangerous
        country.
        Here I used multi line plot to display crime values in 3 different years
    """
    # group the original dataset by country and calculate the sum of the total crimes
    df_crime_countries = df_crime.groupby('Countries')['Total'].sum()
    # sort the countries based on cumulative crime and get the top 1
    Top_1 = df_crime_countries.sort_values(ascending=False).head(1)
    # get the crime data for only the top 1 country from the original dataset
    df_top5 = df_crime[df_crime['Countries'].isin(Top_1.index)]

    # group the top 1 dataset by country and year and calculate the sum of the first four crimes
    df_top1_crime = df_top5.groupby(['Countries', 'Year'])['Murder', 'Robbery', 'Theft','Child Sex Offences'].sum().reset_index()
    #store top country name to display in title
    top_country_name = df_top1_crime['Countries'][0]
    
    years = df_top1_crime.iloc[:,1]
    y1 = df_top1_crime.iloc[0:,2]
    y2 = df_top1_crime.iloc[0:,3]
    y3 = df_top1_crime.iloc[0:,4]
    y4 = df_top1_crime.iloc[0:,5]

    data = {
        
        'Year': years,
        'Murder': y1,
        'Robbery': y2,
        'Theft': y3,
        'Child Sex Offences': y4,
    }

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Loop through each crime and plot its line
    for crime in ['Murder', 'Robbery', 'Theft','Child Sex Offences']:
        ax.plot(data['Year'], data[crime], label=crime, marker='o')

    # Set the title, x-label and y-label
    ax.set_title('Crime Rates over the Years in ' + top_country_name)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Incidents')

    # Set the x-axis tick locations and labels
    ax.set_xticks(data['Year'])
    ax.set_xticklabels(data['Year'])

    # Move x-axis tick labels outside of the graph
    fig.subplots_adjust(bottom=0)

    # Set the legend
    ax.legend()

    # Show the plot
    plt.show()
    
plot_diff_crimes_in_unsafest_country()

def plot_south_asian_crime():
    """ This function is used to  find out the total crimes in
        south asian countries in between 2009-2012.
        Here I used Bar chart to display cumulative values based on
        countries
    """
    final_sum_crime = calc_cumulative_Crime()
    # Filter the dataframe to only include Bangladesh , Bhutan , India , Pakistan , Nepal , and Sri Lanka
    filtered_df = final_sum_crime[final_sum_crime['Countries'].isin(['Sri Lanka', 'India','Pakistan','Bangladesh','Nepal','Bhutan'])]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the data using a bar chart
    ax.bar(filtered_df['Countries'], filtered_df['Cumulative Crime'])

    # Set the x-label and y-label
    ax.set_xlabel('Country')
    ax.set_ylabel('Total Crimes')

    # Set the title of the plot
    ax.set_title('Total Crimes by South Asian Countries during 2009-2012')

    # Display the plot
    plt.show()


plot_south_asian_crime()
