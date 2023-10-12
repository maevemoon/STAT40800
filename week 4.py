import numpy as np
import pandas as pd

path = 'week 4 data/'

# treating strings and ints differently in data
data = []
for line in open(path+'sample4.txt'):
    items = line.rstrip('\n').split(' ')
    curr_items = []
    for j in items:
        if j.isalpha()==True: # is a string
            curr_items.append(j) 
        else:
            curr_items.append(int(j))
    data.append(curr_items)
print(data)

# making dictionaries from data
data = {}
for line in open(path+'sample5.txt'):
    items = line.rstrip('\n').split(' ')
    data[items[0]] = int(items[1]) # term1 : term2
print(data)

# exercise 2
data = {}
for line in open(path+'sample6.txt'):
    items = line.rstrip('\n').split(' ')
    data[items[0]] = [eval(i) for i in items[1:]] # int() doesn't work here when there are multiple entries, so eval()
print(data)

# numpy vs pandas (delimiter -> sep)
npdata = np.loadtxt(path+'array.txt',delimiter=',') 
pddata = pd.read_csv(path+'sample_dat.dat',sep='\t') # \t = tab

# exercise 5
covid = pd.read_excel(path + 'covid-cases.xlsx', skiprows=[0,1,2], index_col='date') #skiprows so we can get index column
print(covid.tail(10))

# assessed exercises
# question 2
# text and numbers in separate lists
text = []
numbers = []
for line in open('AE1_data.txt'):
    items = line.rstrip('\n').split(' ')
    for j in items:
        if j.isalpha()==True: 
            text.append(j) 
        else:
            numbers.append(int(j))
print(text)
print(numbers)
