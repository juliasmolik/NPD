import pandas as pd
import difflib, os

def read_gdp_data(gdp_data):
    """
    Function used to load GDP data. Returns a dataframe 
    that reflects the data in the csv file.
    
    :param gdp_data: csv file with GDP data
    """
    
    # omit lines that do not contain relevant data
    df = pd.read_csv(gdp_data, skiprows=4)
    # removing columns with unnecessary data
    df = df.drop(['Indicator Name', 'Indicator Code'], axis=1)
    # removing columns that are all empty 
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df.drop(empty_cols, axis=1, inplace=True)
    
    return df

def read_population_data(population_data):
    """
    Function used to load population data. Returns a dataframe 
    that reflects the data in the csv file.
    
    :param population_data: csv file with population data
    """
    
    #omit lines that do not contain relevant data
    df = pd.read_csv(population_data, skiprows=4)
    #removing columns with unnecessary data
    df = df.drop(['Indicator Name', 'Indicator Code'], axis=1) 
    # removing columns that are all empty 
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df.drop(empty_cols, axis=1, inplace=True)
    
    return df

def read_co2_data(co2_data):
    """
    Function used to load CO2 emissions data. Returns a dataframe 
    that reflects the data in the csv file.
    
    :param co2_data: csv file with CO2 emissions data
    """
    
    df = pd.read_csv(co2_data)
    
    return df

def filter_data(gdp_data, population_data, co2_data):
    """
    Function used to filter data. It checks which years occur 
    in all data files and removes from individual dataframes those 
    years that are not common in all the files. It returns three 
    dataframes (one for each type of data) in which the years are 
    the same.
    
    :param gdp_data: csv file with GDP data
    :param population_data: csv file with population data
    :param co2_data: csv file with CO2 emissions data
    """
    
    # reading data from files
    df_gdp = read_gdp_data(gdp_data)
    df_population = read_population_data(population_data)
    df_co2 = read_co2_data(co2_data)
    
    # extracting years from data files
    years_gdp = [int(x) for x in list(set(df_gdp.columns[2:]))] # [2:], since the first two columns are the name and abbreviation of the country 
    years_population = [int(x) for x in list(set(df_population.columns[2:]))] # [2:], since the first two columns are the name and abbreviation of the country
    years_co2 = [int(x) for x in list(set(df_co2["Year"]))]
    
    # years that occur in all files
    set1 = set(years_gdp).intersection(set(years_population))
    result_years = sorted(list(set1.intersection(set(years_co2))))
    
    # GDP data filtering
    for column in df_gdp.columns[2:]:
        # removing columns (years) that do not occur together for all files
        if int(column) > max(result_years) or int(column) < min(result_years):
            df_gdp = df_gdp.drop(column, axis=1)
            
    # population data filtering
    for column in df_population.columns[2:]:
        # removing columns (years) that do not occur together for all files
        if int(column) > max(result_years) or int(column) < min(result_years):
            df_population = df_population.drop(column, axis=1)
    
    # CO2 data filtering
    # removing rows (years) that do not occur together for all files
    df_co2 = df_co2.drop(df_co2[(df_co2["Year"] < min(result_years)) | (df_co2["Year"] > max(result_years))].index)
    
    return df_gdp, df_population, df_co2

