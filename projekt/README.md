# Tools Supporting Data Analysis in Python: Final Project
A project to study the relationship between countries' income (GDP - gross domestic product), population numbers and CO2 emissions and visualize these results with various plots.

## Author
Julia Smolik

## About
This program was developed as the final project on the subject Tools Supporting Data Analysis in Python at the Faculty of Mathematics, Informatics and Mechanics, University of Warsaw under the labs tutelage of [Jarosław Paszek, PhD](https://github.com/j-paszek). It is a program that allows the user to merge the data by country and year found in all the [GDP](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD), [population](https://data.worldbank.org/indicator/SP.POP.TOTL) and [CO2](https://datahub.io/core/co2-fossil-by-nation) data csv files, and then visualize them with various plots. The only argument the user has to provide is the paths to the csv files with the data. The rest of the arguments are optional and relate to data filtering and visualization.

## Getting started

The program comes as a package that can be installed with the pip command. The user must be in the directory with the downloaded package and type in the console 

```
$ pip3 install [package_name]
```
where 
```
[package_name] 
```
is the name of the downloaded project package.

Installing this package allows the user to install all the necessary modules to run the program and get all the results. The program includes scripts to pre-process the data, select the years and countries present in all the files, merge them by country and year, and filter the merged data to the range of years of interest to the user. 

## Tutorial
### How to call the program

To call the program, start the terminal, go to the directory where the main script is located and type the command:

```
python3 main.py -g [gdp_data_csv_file] -p [population_data_csv_file] -e [emission_data_csv_file] -s [starting_year] -k [ending_year] -v
```
where 
```
[gdp_data_csv_file], [population_data_csv_file], [emission_data_csv_file] 
```
are paths to csv files with data on GDP, population and CO2 emissions, respectively.
```
[starting_year], [ending_year]
```
are integers that allow the data to be filtered to a specific range of years.
```
-v 
```
parameter allows the user to visualize the obtained results with various plots. 

## Project overview

### Input
* [GDP data](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)
* [Population data](https://data.worldbank.org/indicator/SP.POP.TOTL)
* [CO2 emissions data](https://datahub.io/core/co2-fossil-by-nation)

### Modules used in the project
* Main part of the project [main.py](https://github.com/juliasmolik/NPD/blob/main/projekt/scripts/main.py)
* Data preparation [prepare_data.py](https://github.com/juliasmolik/NPD/blob/main/projekt/scripts/prepare_data.py)
* Calculations [calculations.py](https://github.com/juliasmolik/NPD/blob/main/projekt/scripts/calculations.py)
* Data visualization [visualize.py](https://github.com/juliasmolik/NPD/blob/main/projekt/scripts/visualize.py)
* Tests [tests.py](https://github.com/juliasmolik/NPD/blob/main/projekt/tests/test.py)

## Output
* Table merged by country and year with data on the country, its population, GDP and CO2 emissions in each year 
* Table merged by country and year with data on the country, its population, GDP and CO2 emissions in each year, filtered to a range of years specified by the user
* Table of five countries that emit the most CO2 per capita in each year
* Table of five countries with the highest per capita income in each year
* Table of five countries each that have reduced and increased CO2 emissions the most over the past 10 years (from data)
* Visualization of filtered data using various plots
* Profiler results - pstats file and graph

## Documentation

* [PDF version]()
* [Online version](https://students.mimuw.edu.pl/~js406162/npd/index.html)

