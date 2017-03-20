

import numpy as np
import pandas as pd


#Create a vector from 4 to 100 by 4  
#Create a vector from 0.8 to 40 by 0.8

vector1 = np.arange(4, 101, 4)
vector2 = np.arange(0.8, 40.8, 0.8)


#Create a matrix with the previous vector; make it have 5 columns
myMatrix = np.array(vector2).reshape(len(vector2)/5,5)


#Load zip_codes and Oklahoma dataset into a dataframe
zipCodes = pd.read_csv('zip_codes.csv')
Oklahoma = pd.read_csv('C:\Users\MBG\Documents\R\Oklahoma.csv')


#Display information about new dataframe
zipCodes.info()

Oklahoma.info()


#Find the mean of HSTotal in Oklahoma
Oklahoma['HSTotal'].mean()



#Find the schools in Oklahoma with below-average HS attendance that are not na
OK2= Oklahoma[(Oklahoma['HSTotal'] < Oklahoma['HSTotal'].mean()) & (Oklahoma['HSTotal'].isnull()==0)]
OK2.head()



#Find mean attendance across all grades and add into the dataframe
Oklahoma['ClassAvgSize'] = Oklahoma[['Grade7', 'Grade8', 'Grade9', 'Grade10', 'Grade11', 'Grade12']].mean(axis = 1)


#Display the first 25 rows of the dataframe
Oklahoma.head(25)



#Construct a dataset of only high schools in Oklahoma
OKHS = Oklahoma[Oklahoma['School'].apply(lambda school: 'HS' in school.split() or 'ES-HS' in school.split())]
OKHS.head()


#Create a dataframe of Oklahoma zip codes
OKZips = zipCodes[zipCodes['state'] == 'OK']
OKZips.head()


#Change the names of the cities to uppercase and store in MailCity
OKZips['MailCity'] = OKZips['primary_city'].apply(lambda city: city.upper())



# Merge the zip code data with the high school data
OKZipsAndHS =  pd.merge(OKHS,OKZips,how = 'inner', on = 'MailCity')



#Display the first 25 rows of the new dataset
OKZipsAndHS.head(25)



# Write the resultant dataset to CSV
OKZipsAndHS.to_csv('OKZipsAndHS.csv', index = False)

