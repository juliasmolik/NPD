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

def create_country_name(string):
    """
    Function used to create a country name uniformly. In names, "&" 
    often occurs alternately with "and". The function removes these 
    differences and creates names with "and" only. In addition, the 
    function causes that in the case of a country name with several 
    words, each word will start with a capital letter.
    
    :param string: country name as string 
    """

    # every word in the name beginning with a capital letter 
    tmp_string = string.title()
    name_parts = tmp_string.split(" ")
    # forcing "and" to be the only one that begins with a lowercase letter 
    country_name = " ".join([x if x != "And" else x.lower() for x in name_parts])
    if "&" in country_name:
        country_name = country_name.replace("&", "and")
    return country_name

def find_similar_countries(all_countries, list_of_countries1, list_of_countries2):
    """
    Function used to search for similar country names in other lists. For a given 
    list, it checks each country in it - it looks for the single most similar name 
    in the other list (similarity = cutoff = 0.75). It returns three lists: one is 
    a list of countries that appear in both lists (same or similar names) and two 
    lists that contain countries that appear only in one of the lists. 
    
    :param all_countries: list of common country names
    param list_of_countries1: list of countries appearing only in the first list 
    param list_of countries2: list of countries appearing only in the second list 
    """
    
    # for each country in the first list
    for country1 in list_of_countries1:
        # one most similar country name from the second list 
        close_matches = difflib.get_close_matches(country1, list_of_countries2, n=1, cutoff=0.75)
        # if a similar name appears in the second list
        if close_matches:
            # if the country1 is not already in the list of all countries, add it
            if country1 not in all_countries:
                all_countries.append(country1)
            # remove the analyzed country and the similar country from the lists
            list_of_countries1.remove(country1)
            list_of_countries2.remove(close_matches[0])
    
    return all_countries, list_of_countries1, list_of_countries2

def find_simmilar_countries_exceptions(all_countries, list_of_countries1, list_of_countries2):
    """
    Function used to search for exceptions in countries that have not been found before.
    It returns three lists: one is a list of countries that appear in both lists (same 
    or similar names) and two lists that contain countries that appear only in one of the lists. 
    """

    dictionary = {"Yemen, Rep.":"Yemen", "Iran, Islamic Rep.": "Islamic Republic Of Iran",
                  "Czechia": "Czech Republic", "Egypt, Arab Rep.":"Egypt", "Moldova": "Republic Of Moldova",
                  "Congo, Dem. Rep.": "Democratic Republic Of The Congo (Formerly Zaire)", "Congo, Rep.": "Congo",
                  "United States":"United States Of America", "France":"France (Including Monaco)", "Korea, Rep.": "Republic Of Korea",
                  "Korea, Dem. People'S Rep.": "Democratic People S Republic Of Korea", "Cameroon": "Republic Of Cameroon",
                  "Italy":"Italy (Including San Marino)", "Bolivia":"Plurinational State Of Bolivia", "Slovak Republic":"Slovakia",
                  "China":"China (Mainland)", "Hong Kong Sar, China":"Hong Kong Special Adminstrative Region Of China", 
                  "Macao Sar, China":"Macau Special Adminstrative Region Of China", "Bahamas, The":"Bahamas", 
                  "South Sudan":"Republic Of South Sudan", "Gambia, The":"Gambia"}

    # for each country exception 
    for country in dictionary:
        # if the exception has not yet been added
        if dictionary[country] not in all_countries:
            all_countries.append(dictionary[country])
        # remove exceptions from the list of unique countries for each file
        if country in list_of_countries1:
            list_of_countries1.remove(country)
        if dictionary[country] in list_of_countries2:
            list_of_countries2.remove(dictionary[country])
        
    return all_countries, list_of_countries1, list_of_countries2
    

def get_countries(gdp_data, population_data, co2_data):
    """
    Function used to find countries that appear in all files. Some countries correspond 
    to each other in different files, but have different names. The function returns sorted 
    names of all countries which correspond to each other and which appear in all files.
    
    :param gdp_data: csv file with GDP data
    :param population_data: csv file with population data
    :param co2_data: csv file with CO2 emissions data
    """
    
    filtered_gdp, filtered_population, filtered_co2 = filter_data(gdp_data, population_data, co2_data)
    
    # countries that appear in the co2 file
    co2_countries = [create_country_name(x.lower()) for x in list(set(filtered_co2["Country"]))]
    
    # countries that appear in the population/gdp file (the same countries)
    population_countries = [create_country_name(x) for x in list(set(filtered_population["Country Name"]))]
    
    all_countries = []
    
    # searching for common countries in the files 
    for country in co2_countries:
        if country in population_countries:
            if " " not in country:
                all_countries.append(country)
            else:
                all_countries.append(create_country_name(country))
    
    # countries only in the co2 file
    only_co2_countries = [create_country_name(x) for x in co2_countries if x not in population_countries]   
    # countries only in the population/gdp file
    only_population_countries = [create_country_name(x) for x in population_countries if x not in co2_countries]  

    # searching for similar names in the other list    
    all_countries, only_co2_countries, only_population_countries = find_similar_countries(all_countries, only_co2_countries, only_population_countries)
    all_countries, only_population_countries, only_co2_countries = find_similar_countries(all_countries, only_population_countries, only_co2_countries)
    
    # adding exceptions 
    all_countries, only_population_countries, only_co2_countries = find_simmilar_countries_exceptions(all_countries, only_population_countries, only_co2_countries)
    all_countries, only_co2_countries, only_population_countries = find_simmilar_countries_exceptions(all_countries, only_co2_countries, only_population_countries)
    print("{} countries to analyze. Ommiting the total of {} countries from all the files".format(len(all_countries), len(only_co2_countries)+len(only_population_countries)))
    
    all_countries_sorted = sorted(all_countries)
    
    return all_countries_sorted