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
    plt.pie(top_n["Cumulative Crime"], labels=top_n.index, autopct='%1.1f%%')
    plt.title(f"Top {n} Unsafest Countries in between 2009-2012 \n (Based on Total Crime % )")
    plt.show()    

userchoice = int( input("Enter number of countries : "))
plot_top_n_unsafest_countries(userchoice)
