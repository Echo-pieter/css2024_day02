# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:46:47 2024

@author: terre
"""

import pandas as pd

file = pd.read_csv('iris.csv')



# you can also reads files from the web (like github)

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# create a list containing the column headings
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

#df_web = pd.read_csv(url, header=None, names=column_names)


# we can also import text files we must only specify the correct delimeter (if it does not use commas)
file_txt = pd.read_csv("Geospatial Data.txt", sep=';')


# we can import an excel file (specify the specific sheet if there is more than one)
file_excel = pd.read_excel('residentdoctors.xlsx')


# we can import a json file using pandas
file_json = pd.read_json("student_data.json")



# the file below already has indexing. It must be removed since pandas adds a default index column
# the index_col can be used to set a column inside of the data frame equal to the index

df = pd.read_csv("country_data_index.csv", index_col=0)




# investigate the excel file
#print(file_excel.info())



# transforming the data


# the excel file has words and letters combined in one of the columns
# we can transform the column


# the (/d+) below is a regular expression for a number

# the command below only extracts the numerical values from the data frame
file_excel['LOWER_AGE']=file_excel['AGEDIST'].str.extract('(\d+)-')

# file_excel['UPPER_AGE']=file_excel['AGEDIST'].str.extract('-(\d+)')


# the new column a.k.a LOWER_AGE is still a string since it was extracted from a string

#print(file_excel.info())


# we need to convert the new column to an integer

file_excel['LOWER_AGE'] = file_excel['LOWER_AGE'].astype(int)


# print(file_excel.info())








# importing the time series data (experimenting with dates)
# (get rid of the index column)
file_time_series = pd.read_csv('time_series_data.csv', index_col=0)

'''
Working with dates

UK: 10-01-2024

US: 01-10-2024
'''

# pandas interprets a dash or any other character as string
#print(file_time_series.info())

# we must convert the string to the date and time format

file_time_series['Date'] = pd.to_datetime(file_time_series['Date'], format="%Y-%m-%d")


# extrac the year month and date and save it in diffeerent columns
file_time_series['Year'] = file_time_series['Date'].dt.year
file_time_series['Month'] = file_time_series['Date'].dt.month
file_time_series['Day'] = file_time_series['Date'].dt.day



# fixing the patient dates data

# remove the index column
file_patient_data = pd.read_csv("patient_data_dates.csv", index_col=0)



# remove the row with nan value in Date column
file_patient_data.drop(index=26, inplace=True)


# convert the date from string to DateTimeformat
file_patient_data['Date'] = pd.to_datetime(file_patient_data['Date'])



# replace the nan's inside of the Calorie column (we replace empty values with the average value)
avg_cal = file_patient_data['Calories'].mean()

file_patient_data['Calories'].fillna(avg_cal, inplace=True)


# we must remove the nan values
file_patient_data.dropna(inplace=True)

# reset the index column after dropping some rows
file_patient_data = file_patient_data.reset_index(drop=True)


# we must fix the outlier (the original value was 450)

file_patient_data.loc[7, 'Duration'] = 45

# alternative
# file_patient_data['Duration'] = file_patient_data['Duration'].replace([450],45)











# data transformations (grouping data)




file_iris = pd.read_csv('iris.csv')


# extract the headers and save them inside of a list
file_iris_headers = file_iris.columns.tolist()


# we want to add a column called sepal length squared
file_iris['sepal_length_sq'] = file_iris['sepal_length']**2

# alternative way using lamda functions to find the square
file_iris['sepal_length_sq2'] = file_iris['sepal_length'].apply(lambda x: x**2)



# grouping

# group based on the class column
grouped = file_iris.groupby('class')

# using aggregate functions on the group
mean_square_values = grouped['sepal_length_sq'].mean()

#print(mean_square_values)

summed_values = grouped['sepal_length'].sum()


# the class column of the iris dataframe has redundant information
# one can remove the word 'iris' 
# the word 'iris' is replaced with empty

file_iris['class'] = file_iris['class'].str.replace("Iris-","")











# combining data (merge)



df1 = pd.read_csv('person_split1.csv')

df2 = pd.read_csv('person_split2.csv')






# we want to combine df1 and df2 

df_combo = pd.concat([df1, df2], ignore_index=True)


##################################################################

# working with files with different header names, but relation between headers

# going to merge them based on a common relation

df_education = pd.read_csv('person_education.csv')

df_work = pd.read_csv('person_work.csv')


# do an inner join on the two dataframes to combine them based on realtionship

df_merge = pd.merge(df_education, df_work, on='id')






# filtering


# we want to filter the data based on sepal_length greater than 5
greater_than_5 = file_iris[file_iris['sepal_length'] > 5]


# only see data for virginica class
virginica_class = file_iris[file_iris['class'] == 'virginica']





















# after extracting and transforming the data it is necessary to load (save) the results
# we want to export the results

# sve to working directory
file_iris.to_csv("pulsar.csv")

# save to output directory
file_iris.to_csv('output/pulsar.csv')


