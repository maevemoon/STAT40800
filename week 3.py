import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import numpy.random as npr


# series 
my_series_2 = Series([6, 9, 2, 5],index=['a', 'd', 'b', 'c']) # index optional
# print(my_series_2)
# print(my_series_2 < 5)

my_series_3 = Series([1,2,3,4,5],index=['e', 'a', 'd', 'c','f'])
# print(my_series_2**my_series_3) # adding two together

# exercise 2
def multiples_five(max):
    series = Series(range(1, max+1), index=range(1, max+1)) * 5
    answer = series < max
    print(series[answer])

max = 24
print(multiples_five(max))

# data frames
dict_1 = {'a': np.arange(5),'b': npr.rand(5),'c': npr.randint(0,10,size=(5))}
df_1 = DataFrame(dict_1)
print(df_1)

iphone_dict = {'Name': ['iPhone', 'iPhone 3G', 'iPhone 3GS', 'iPhone 4', 'iPhone 4S', 'iPhone 5', 'iPhone 5C', 'iPhone 5S'],
    'Memory_MB': [128, 128, 256, 512, 512, 1024, 1024, 1024],
    'Weight_g': [135, 133, 135, 137, 140, 112, 132, 112],
    'Camera_MP': [2, 2, 3, 5, 8, 8, 8, 8],
    'Year': [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2013] }
iphone_df = DataFrame(iphone_dict,index=iphone_dict['Name'],columns=['Memory_MB','Weight_g','Camera_MP','Year'])
print(iphone_df)

# print(iphone_df.iloc[0])
# print(iphone_df.loc['iPhone 5C'])
print(iphone_df.iloc[2:4,:2]) # rows 2->4 (exclusive), first two columns

# iphone_df.Camera_MP[4] = 6 # changing camera mp to say 6 in 4th row

# pass by reference
df_2 = DataFrame({'x': [0,1,2,3],'y': [4,5,6,7],'z': [8,9,10,11]},index=('a','b','c','d'))
print(df_2)

sample = df_2.x # extracting part of data frame also changes the data frame - add .copy() after to not do it
print(df_2)
sample[0:2] = 10
print(sample)
print(df_2) 

# exercise 5
dict1 = {'Name': ['Aaron', 'Barry', 'Catherine', 'Darren', 'Edel', 'Francis', 'George', 'Helen', 'Ian'], 
         'Age': [23,36,27,19,41,38,57,17,28], 
         'Height': [1.7,2.1,1.8,1.9,1.7,2.0,1.8,1.6,1.7],
         'Weight': [64,99,68,85,102,84,87,90,78]}
df1 = DataFrame(dict1,index=dict1['Name'], columns=['Age', 'Height', 'Weight'])
print(df1.iloc[3,1]) # darren's height

# question 1
# can use np.eye() and np.diag()
matrix = np.zeros((5,5))
i,j = np.indices(matrix.shape)
matrix[i==j] = -2.
matrix[i==j-1] = 1.
matrix[i==j+1] = 1.
print(matrix)

# question 2 
def matrix_multiplication(n):
    X = np.array(range(1,2*n**2+1,2)).reshape(n,n)
    Y = np.array(range(2*n**2,0,-2)).reshape(n,n)
    result = X.dot(Y)
    return result

# question 3
df = DataFrame({'x':[1,2,3,4],'y':[5,6,7,8],'z':[9,10,11,12]},index=['a','b','c','d'])
print(df)
print(df.loc['b','z'])
print(df.iloc[0,1])
# print(df.iloc['a','x'])
# print(df.loc[2,1])
# print(df.iloc[df.z>2])
# print(df.loc[df['a']>2])
print(df.loc[df.x>2])
# print(df.loc['x','b'])

# question 5
Europe = DataFrame({'Area':[44.5,183.5,301.3,41.2,312.7,498.5],
'Capital':['Aarhus','Paris','Rome','Amsterdam','Warsaw','Barcelona'],
'Population':[5.9,68,58.8,17.8,517.2,48]},
index=['Denmark','France','Italy','Netherlands','Poland','Spain'])

print(Europe)
Europe.iloc[0,1] = 'Copenhagen'
Europe.iloc[5,1] = 'Madrid'
Europe.iloc[4,2] = 36.7
Europe.iloc[1,0] = 551.7
print(Europe)

# could also do this
# Europe.Capital[5] = 'Madrid'
# Europe.Population[4] = 36.7
# Europe.Area[1] = 551.7