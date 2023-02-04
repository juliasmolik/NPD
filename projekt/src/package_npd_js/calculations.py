import pandas as pd
import os

def read_data(csv_file):
    """
    Function used to load a csv file that contains merged data.
    
    :param csv_file: a csv file that contains merged data
    """
    
    df = pd.read_csv(csv_file)
    
    return df
    

def co2_per_capita(csv_file):
    """
    Function used to calculate per capita CO2 emissions. It saves 
    the calculated data to a csv file. 
    
    :param csv_file: a csv file that contains merged data
    """
    
    path = '../../results/tables/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    co2_per_capita = []
    
    df = read_data(csv_file)
    # for each row (country) calculate CO2 emissions per capita
    for index, row in df.iterrows():
        try:
            co2_per_capita.append(row["CO2 Total"]/row["Population"])
        # or if some of the data is absent in the input csv file, set this value to blank 
        except:
            co2_per_capita.append("")
    
    df["CO2 per capita"] = co2_per_capita    
    df = df.sort_values(['Year', 'Country Name'], ascending = [True, True])
    
    new_df = pd.DataFrame()
    
    # for each year in the data selecting 5 countries that achieved the highest values
    for year in sorted(list(set(df["Year"]))):
        sub_df = df[df["Year"] == year][["Year", "Country Name", "Country Code", "CO2 Total", "CO2 per capita"]]
        sub_df = sub_df.sort_values(["CO2 per capita"], ascending = [False])
        # as instructed - 5 countries with the highest value
        new_df = pd.concat([new_df, sub_df.head(5)])
    
    new_df = new_df.sort_values(['Year', "CO2 per capita"], ascending = [True, False]).reset_index(drop=True)
    new_df.to_csv(path+"co2_per_capita.csv", index=False)
    
    return new_df


def gdp_per_capita(csv_file):
    """
    Function used to calculate GDP per capita. It saves 
    the calculated data to a csv file. 
    
    :param csv_file: a csv file that contains merged data
    """
    
    path = '../../results/tables/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    gdp_per_capita = []
    
    df = read_data(csv_file)
    
    # for each row (country) calculate GDP per capita
    for index, row in df.iterrows():
        try:
            gdp_per_capita.append(row["GDP"]/row["Population"])
        # or if some of the data is absent in the input csv file, set this value to blank 
        except:
            gdp_per_capita.append("")
    
    df["GDP per capita"] = gdp_per_capita    
    df = df.sort_values(['Year', 'Country Name'], ascending = [True, True])
    
    new_df = pd.DataFrame()
    
    # for each year in the data selecting 5 countries that achieved the highest values
    for year in sorted(list(set(df["Year"]))):
        sub_df = df[df["Year"] == year][["Year", "Country Name", "Country Code", "GDP", "GDP per capita"]]
        sub_df = sub_df.sort_values(["GDP per capita"], ascending = [False])
        # as instructed - 5 countries with the highest value
        new_df = pd.concat([new_df, sub_df.head(5)])
    
    new_df = new_df.sort_values(['Year', "GDP per capita"], ascending = [True, False]).reset_index(drop=True)
    new_df.to_csv(path+"gdp_per_capita.csv", index=False)
    return new_df

def change_of_co2_emission(csv_file):
    """
    Function used to calculate changes in CO2 emissions per capita. 
    It saves the calculated data to a csv file. 
    
    :param csv_file: a csv file that contains merged data
    """
    
    path = '../../results/tables/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    change_of_co2_emission = []
    
    df = read_data(csv_file)
    
    years = list(set(df["Year"]))
    # if 10 years cannot be distinguished in the data - setting the default time interval (smallest and largest value from years, repectively)
    if max(years) - min(years) < 10:
        start_year = min(years)
        end_year = max(years)
        print("No data from the last 10 years. Setting the interval of {}-{}".format(start_year, end_year))
    # otherwise the time period is 10 years
    else:
        start_year = max(years)-10
        end_year = max(years)
    
    # calculation of the change in CO2 emissions for each country
    for country in sorted(list(set(df["Country Name"]))):
        # sub-dataframe that contains information about the analyzed country over the preset time period
        sub_df = df[(df["Country Name"] == country) & ((df["Year"] >= start_year)&(df["Year"] <= end_year))].sort_values(["Year"], ascending = [True])
        
        # CO2 emissions per capita in the start and end years, respectively
        per_capita_initial = sub_df.iloc[0]["CO2 Total"]/sub_df.iloc[0]["Population"]
        per_capita_final = sub_df.iloc[-1]["CO2 Total"]/sub_df.iloc[-1]["Population"]
        
        # creating a new dataframe with all the data for each country
        change_of_co2_emission.append([start_year, end_year,
                                       sub_df.iloc[0]["Country Name"], sub_df.iloc[0]["Country Code"],
                                       sub_df.iloc[0]["Population"], sub_df.iloc[-1]["Population"],
                                       sub_df.iloc[0]["CO2 Total"], sub_df.iloc[-1]["CO2 Total"],
                                       per_capita_initial, per_capita_final, per_capita_final-per_capita_initial])

    df_new = pd.DataFrame(change_of_co2_emission, columns = ["Start year", "End year", "Country Name", "Country Code", "Initial population", "Final population",
                                                             "Initial CO2 Total", "Final CO2 Total", "Initial CO2 per capita", "Final CO2 per capita", "Change of CO2 emission"])
    
    df_new = df_new.sort_values(['Change of CO2 emission', 'Country Name'], ascending = [True, False])
    df_new = df_new.dropna()
    df_final = pd.DataFrame()
    # selecting 5 countries with the largest increase and decrease in CO2 emissions per capita 
    df_final = pd.concat([df_new.head(5), df_new.tail(5)])

    df_final.to_csv(path+"change_of_co2_emission.csv", index=False)
    
    return df_final