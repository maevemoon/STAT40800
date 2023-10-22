import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
# https://matplotlib.org/stable/users/explain/colors/colormaps.html#classes-of-colormaps 

path = 'week 5 data/'
diamonds = pd.read_csv(path+'diamonds2.csv')

# exercise 1
plt.figure()
# plt.plot color and marker can be together eg. 'c^'
# color - listed names / greyscale intensities from 0-1 / hex
plt.scatter(diamonds.carat,diamonds.x,color='c',marker='^',label='x')
plt.scatter(diamonds.carat,diamonds.y,color='m',marker='o',label='y')
plt.scatter(diamonds.carat,diamonds.z,color='green',marker='s',label='y')
plt.ylabel('Length',fontsize=15)
plt.xlabel('Carat',fontsize=15)
plt.title('Scatter plot of diamond dimension vs carat',fontsize=15,weight='bold')
plt.legend(loc='lower right',fontsize=17)
plt.axis([0,3,0,10])
plt.yticks(np.linspace(0,10,5)) # first number, last number, total ticks
plt.grid(visible=True, which='major',color='0.6', linestyle=':')
plt.savefig('week 5 data/example plot.png')

# plt.figure - start
# plt.subplot - another figure in same window

# assessed exercises
tips = sns.load_dataset('tips')
print(tips)
print(tips['sex'].value_counts()['Female']) # counting occurences of specific thing in dataframe

tip_precentage = (tips.iloc[:,1] / tips.iloc[:,0]) * 100
tips['tip_precentage'] = tip_precentage # adding column to dataframe
print(tips)

sns.relplot(data=tips,x='tip_precentage',y='total_bill',hue='time')
plt.savefig('week 5 data/tips.png')

plt.figure()
sns.displot(kind='hist',data=tips,x='tip_precentage',y='tip',hue='sex')
plt.savefig('week 5 data/tips2.png')
