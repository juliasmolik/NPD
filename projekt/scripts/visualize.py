import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, math, textwrap 

def visualize_co2_change(csv_file):
    """
    Function used to visualize the results obtained. It creates a barplot showing 
    5 countries each that have increased and decreased CO2 emissions per capita the 
    most in the given range of years. 
    
    :param csv_file: a csv file that contains calculated data
    """
    
    df = pd.read_csv(csv_file)
    
    # directory where the results are saved
    path = './projekt/results/plots/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    plt.figure(figsize=(20, 8))
    
    ax = sns.barplot(x = 'Country Name', y = 'Change of CO2 emission', data = df, palette = 'Blues')
    for i in ax.containers:
        ax.bar_label(i, fmt="%.2e", fontsize=5)
    plt.xticks(rotation=45)
    plt.ylabel('Change of CO$_2$ emission')
    s_year = list(set(df["Start year"]))[0]
    e_year = list(set(df["End year"]))[0]
    # if there are 10 years in the data
    if e_year-s_year >= 10:
        plt.title("Countries (per capita) that have reduced and increased CO$_2$ emissions the most over the past 10 years ({}-{})".format(s_year, e_year))
    else:
        plt.title("Countries (per capita) that have reduced and increased CO$_2$ emissions the most in the years {}-{}".format(s_year, e_year))
    plt.grid(axis="y")
    ax.set_xticklabels([textwrap.fill(t.get_text(), 25, break_long_words = False)  for t in ax.get_xticklabels()])
    #plt.show()
    plt.savefig(path+"change_of_co2_emissions.png", bbox_inches = 'tight')

def visualize_co2_per_capita(csv_file):
    """
    Function used to visualize the results obtained. It creates a barplot showing 
    5 countries that had the highest CO2 emissions per capita in the given years.
    
    :param csv_file: a csv file that contains calculated data
    """
    
    df = pd.read_csv(csv_file)
    
    # directory where the results are saved
    path = './projekt/results/plots/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    plt.figure(figsize=(20, 8))
    
    # if there are no more than 5 years in the data - show them all in the graph
    if len(list(set(df["Year"]))) <= 5:
        ax = sns.barplot(x = 'Country Name', y = 'CO2 per capita', hue = "Year", data = df)
        for i in ax.containers:
            ax.bar_label(i, fmt="%.2e", fontsize=6)
        plt.ylabel('CO$_2$ emission per capita')
        plt.xticks(rotation=45)
        plt.title("Countries with the highest CO$_2$ emissions per capita")
        plt.grid(axis="y")
        #plt.show()
        plt.savefig(path+"co2_per_capita.png", bbox_inches = 'tight')
        
    # otherwise combine data from years to visualize several years simultaneously
    else:
        data = []
        # how many years to put together (how many year ranges in the legend)
        bins = math.ceil(len(list(set(df["Year"])))/5)
        years = []
        # now the years will be in ranges - to the list add the starting year of the range and the ending year 
        for i in range(0,len(list(set(df["Year"]))), bins):
            # the starting year
            years.append(list(set(df["Year"]))[i])
            # the ending year 
            years.append(list(set(df["Year"]))[i]+bins-1)
        # sub-dataframe that applies to the years in the created range 
        for i in range(0,len(years)-1, 2):
            sub_df_year = df[(df["Year"] >= years[i]) & (df["Year"] <= years[i+1])]
            countries = list(set(sub_df_year["Country Name"]))
            for country in countries:
                sub_df_country = sub_df_year[sub_df_year["Country Name"] == country]
                data.append([country, list(sub_df_country["Country Code"])[0], sum(sub_df_country["CO2 per capita"].tolist()), "{}-{}".format(years[i], years[i+1])])
        
        # creating a new dataframe that represents data for the combined years
        df_edit = pd.DataFrame(data, columns=["Country Name", "Country Code", "Sum of CO2 per capita", "Year"])
        
        ax = sns.barplot(x = 'Country Name', y = 'Sum of CO2 per capita', hue = "Year", data = df_edit)
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
        for i in ax.containers:
            ax.bar_label(i, fmt="%.2e", fontsize=6)
        plt.ylabel('Sum of CO$_2$ emission per capita')
        plt.xticks(rotation=45)
        plt.title("Countries with the highest sum of CO$_2$ emissions per capita")
        plt.grid(axis="y")
        ax.set_xticklabels([textwrap.fill(t.get_text(), 25, break_long_words = False)  for t in ax.get_xticklabels()])
        #plt.show()
        plt.savefig(path+"co2_per_capita.png", bbox_inches = 'tight')
        
            
    
def visualize_gdp_per_capita(csv_file):
    """
    Function used to visualize the results obtained. It creates a barplot showing 
    5 countries that had the highest GDP per capita in the given years.
    
    :param csv_file: a csv file that contains calculated data
    """
    
    df = pd.read_csv(csv_file)
    
    # directory where the results are saved
    path = './projekt/results/plots/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    plt.figure(figsize=(20, 8))
    
    # if there are no more than 5 years in the data - show them all in the graph
    if len(list(set(df["Year"]))) <= 5:
        ax = sns.barplot(x = 'Country Name', y = 'GDP per capita', hue = "Year", data = df)
        for i in ax.containers:
            ax.bar_label(i, fmt="%.2e", fontsize=6)
        plt.ylabel('GDP per capita')
        plt.xticks(rotation=45)
        plt.title("Countries with the highest GDP per capita")
        plt.grid(axis="y")
        #plt.show()
        plt.savefig(path+"gdp_per_capita.png", bbox_inches = 'tight')
    # otherwise combine data from years to visualize several years simultaneously
    else:
        data = []
        # how many years to put together (how many year ranges in the legend)
        bins = math.ceil(len(list(set(df["Year"])))/5)
        years = []
        # now the years will be in ranges - to the list add the starting year of the range and the ending year 
        for i in range(0,len(list(set(df["Year"]))), bins):
            # the starting year
            years.append(list(set(df["Year"]))[i])
            # the ending year 
            years.append(list(set(df["Year"]))[i]+bins-1)
        # sub-dataframe that applies to the years in the created range
        for i in range(0,len(years)-1, 2):
            sub_df_year = df[(df["Year"] >= years[i]) & (df["Year"] <= years[i+1])]
            countries = list(set(sub_df_year["Country Name"]))
            for country in countries:
                sub_df_country = sub_df_year[sub_df_year["Country Name"] == country]
                data.append([country, list(sub_df_country["Country Code"])[0], sum(sub_df_country["GDP per capita"].tolist()), "{}-{}".format(years[i], years[i+1])])
        
        # creating a new dataframe that represents data for the combined years
        df_edit = pd.DataFrame(data, columns=["Country Name", "Country Code", "Sum of GDP per capita", "Year"])
        
        ax = sns.barplot(x = 'Country Name', y = 'Sum of GDP per capita', hue = "Year", data = df_edit)
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
        for i in ax.containers:
            ax.bar_label(i, fmt="%.2e", fontsize=6)
        plt.ylabel('Sum of GDP per capita')
        plt.xticks(rotation=45)
        plt.title("Countries with the highest sum of GDP per capita")
        plt.grid(axis="y")
        ax.set_xticklabels([textwrap.fill(t.get_text(), 25, break_long_words = False)  for t in ax.get_xticklabels()])
        #plt.show()
        plt.savefig(path+"gdp_per_capita.png", bbox_inches = 'tight')