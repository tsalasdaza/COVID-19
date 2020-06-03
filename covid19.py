import pandas as pd
import numpy as np

load_confirmed_global = pd.read_csv('/Users/tomassalasdaza/Programing/covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
print(load_confirmed_global.head())

load_confirmed_us = pd.read_csv('/Users/tomassalasdaza/Programing/covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_us.csv')
print(load_confirmed_us.head())

load_death_global = pd.read_csv('/Users/tomassalasdaza/Programing/covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
print(load_death_global.head())

load_death_us = pd.read_csv('/Users/tomassalasdaza/Programing/covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_us.csv')
print(load_death_us.head())

load_recovered_global = pd.read_csv('/Users/tomassalasdaza/Programing/covid-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
print(load_recovered_global.head())
