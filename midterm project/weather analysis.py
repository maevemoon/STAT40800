import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather = pd.read_csv('weather_1819.csv',skiprows=11) # skipping the legend of the data file

# TABLE 1. RECORD VALUES FOR WEATHER MEASUREMENTS IN AIRPORT WEATHER STATIONS AROUND IRELAND
r = {'Measurement': [], 'Record': [], 'Station': [], 'Date': []}
records = pd.DataFrame(r,index=r['Measurement'],columns=['Record', 'Station', 'Date'])

f = "{} {} {}" # shortening code, this is the format of the date (dd mm yyyy)

maxtp = weather['maxtp'] # shortening code
mintp = weather['mintp']
rain = weather['rain']
wdsp = weather['wdsp']
hg = weather['hg']
sun = weather['sun']

max_tp = weather['maxtp'].idxmax()
min_tp = weather['mintp'].idxmin()
max_rain = weather['rain'].idxmax()
max_wdsp = weather['wdsp'].idxmax()
max_hg = weather['hg'].idxmax()
max_sun = weather['sun'].idxmax()

records.loc['Max Temperature (C)'] = [maxtp.max(),weather.loc[max_maxtp,'station'],f.format(weather.loc[max_tp,'day'],weather.loc[max_tp,'month'],weather.loc[max_tp,'year'])]
records.loc['Min Temperature (C)'] = [mintp.min(),weather.loc[min_tp,'station'],f.format(weather.loc[min_tp,'day'],weather.loc[min_tp,'month'],weather.loc[min_tp,'year'])]
records.loc['Precipitation Amount (mm)'] = [rain.max(),weather.loc[max_rain,'station'],f.format(weather.loc[max_rain,'day'],weather.loc[max_rain,'month'],weather.loc[max_rain,'year'])]
records.loc['Wind Speed (kn)'] = [wdsp.max(),weather.loc[max_wdsp,'station'],f.format(weather.loc[max_wdsp,'day'],weather.loc[max_wdsp,'month'],weather.loc[max_wdsp,'year'])]
records.loc['Highest Gust (kn)'] = [hg.max(),weather.loc[max_hg,'station'],f.format(weather.loc[max_hg,'day'],weather.loc[max_hg,'month'],weather.loc[max_hg,'year'])]
records.loc['Sunshine Duration (hrs)'] = [sun.max(),weather.loc[max_sun,'station'],f.format(weather.loc[max_sun,'day'],weather.loc[max_sun,'month'],weather.loc[max_sun,'year'])]

print("Record values for 2018 & 2019 weather measurements in airport weather stations around Ireland.\n\n",records)

# OUTPUT:
# Record values for 2018 & 2019 weather measurements in airport weather stations around Ireland.

#                             Record          Station         Date
# Max Temperature (C)          32.0  Shannon Airport  28 jun 2018
# Min Temperature (C)          -7.0     Cork Airport   1 mar 2018
# Precipitation Amount (mm)    54.6     Cork Airport  15 apr 2019
# Wind Speed (kn)              28.5   Dublin Airport   2 mar 2018
# Highest Gust (kn)            84.0    Knock Airport   2 jan 2018
# Sunshine Duration (hrs)      15.9   Dublin Airport  28 jun 2018


# TABLE 2. NUMERICAL SUMMARY OF WEATHER MEASUREMENTS IN AIRPORT WEATHER STATIONS AROUND IRELAND
s = {'Measurement': [], 'Mean': [], 'Median': [], 'Standard Deviation': [], 'Minimum': [], 'Maximum': []} # dict for df
summary = pd.DataFrame(s,index=s['Measurement'],columns=['Mean', 'Median', 'Std Deviation', 'Min', 'Max']) # df from dict

summary.loc['Max Temperature (C)'] = [maxtp.mean(),maxtp.median(),maxtp.std(),maxtp.min(),maxtp.max()] # adding separately for organisation; easy to change
summary.loc['Min Temperature (C)'] = [mintp.mean(),mintp.median(),mintp.std(),mintp.min(),mintp.max()]
summary.loc['Precipitation Amount (mm)'] = [rain.mean(),rain.median(),rain.std(),rain.min(),rain.max()]
summary.loc['Wind Speed (kn)'] = [wdsp.mean(),wdsp.std(),wdsp.median(),wdsp.min(),wdsp.max()]
summary.loc['Highest Gust (kn)'] = [hg.mean(),hg.median(),hg.std(),hg.min(),hg.max()]
summary.loc['Sunshine Duration (hrs)'] = [sun.mean(),sun.median(),sun.std(),sun.min(),sun.max()] 

print("\n\nNumerical summary for various 2018 & 2019 weather measurements in airport weather stations around Ireland.\n\n",summary)

# OUTPUT:
# Numerical summary for various 2018 & 2019 weather measurements in airport weather stations around Ireland.

#                                  Mean     Median  Std Deviation  Min   Max
# Max Temperature (C)        13.283150  12.800000       5.146289 -1.8  32.0
# Min Temperature (C)         6.432977   6.400000       4.368755 -7.0  18.9
# Precipitation Amount (mm)   3.063583   0.700000       5.053881  0.0  54.6
# Wind Speed (kn)             9.481475   3.820605       8.900000  2.3  28.5
# Highest Gust (kn)          25.443871  24.000000       9.278313  7.0  84.0
# Sunshine Duration (hrs)     3.783797   2.600000       3.850012  0.0  15.9


sns.set_style('whitegrid',{'grid.color':'.7','grid.linestyle':':'}) # readable background so the individual monthly measurements are easy to read

# FIGURE 1. GRAPHICAL SUMMARIES OF WEATHER MEASUREMENTS IN AIRPORT WEATHER STATIONS AROUND IRELAND
weather_melted = weather.melt(['day','month','year','station','rain','wdsp','hg','sun'],var_name="temperature",value_name="tp") # melting minimum + maximum temperatures so they can be plotted together

plt.figure()
maxtp = sns.relplot(data=weather_melted,x='month',y='tp',col='station',hue='station',style='temperature',kind='line',errorbar='sd') # plotting standard deviation instead of 95% ci to compare with numerical summary
rain = sns.relplot(data=weather,x='month',y='rain',col='station',hue='station',kind='line',errorbar='sd')
wdsp = sns.relplot(data=weather,x='month',y='wdsp',col='station',hue='station',kind='line',errorbar='sd')
hg = sns.relplot(data=weather,x='month',y='hg',col='station',hue='station',kind='line',errorbar='sd')
sun = sns.relplot(data=weather,x='month',y='sun',col='station',hue='station',kind='line',errorbar='sd')

# supporting titles
maxtp.fig.subplots_adjust(top=.85) # so the title does not intercept the individual graph titles
maxtp.fig.suptitle('Monthly Maximum/Minimum Temperature in Airport Weather Stations around Ireland',size=15,weight='bold')
rain.fig.subplots_adjust(top=.85)
rain.fig.suptitle('Monthly Precipitation in Airport Weather Stations around Ireland',size=15,weight='bold')
wdsp.fig.subplots_adjust(top=.85)
wdsp.fig.suptitle('Monthly Wind Speed in Airport Weather Stations around Ireland',size=15,weight='bold')
hg.fig.subplots_adjust(top=.85)
hg.fig.suptitle('Monthly Highest Gust in Airport Weather Stations around Ireland',size=15,weight='bold')
sun.fig.subplots_adjust(top=.85)
sun.fig.suptitle('Monthly Sunshine Hours in Airport Weather Stations around Ireland',size=15,weight='bold')

# axis labels
maxtp.set_axis_labels('Month','Temperature Temperature (C)',size=10,weight='bold')
rain.set_axis_labels('Month','Precipitation Amount (mm)',size=10,weight='bold')
wdsp.set_axis_labels('Month','Wind Speed (kn)',size=10,weight='bold')
hg.set_axis_labels('Month','Highest Gust (kn)',size=10,weight='bold')
sun.set_axis_labels('Month','Sunshine Hours (hrs)',size=10,weight='bold')


# FIGURE 2. GRAPHICAL SUMMARY OF MEAN WIND SPEED VS. HIGHEST GUST IN AIRPORT WEATHER STATIONS AROUND IRELAND
plt.figure()
wdsp_hg = sns.relplot(data=weather,x='wdsp',y='hg',hue='month',style='station',col='year')

wdsp_hg.fig.subplots_adjust(top=.85)
wdsp_hg.fig.suptitle('Mean Wind Speed vs. Highest Gust in Airport Weather Stations around Ireland',size=13,weight='bold')

wdsp_hg.set_axis_labels('Wind Speed (kn)', 'Highest Gust (kn)',size=10,weight='bold')


# FIGURE 3. GRAPHICAL SUMMARY OF TEMPERATURE RANGE VS. SUNSHINE HOURS IN AIRPORT WEATHER STATIONS AROUND IRELAND
weather['tprange'] = weather['maxtp'] - weather['mintp']

plt.figure()
tprange_sun = sns.relplot(data=weather,x='tprange',y='sun',hue='month',style='station',col='year')

tprange_sun.fig.subplots_adjust(top=.85)
tprange_sun.fig.suptitle('Daily Temperature Range vs. Hours of Sunlight in Airport Weather Stations around Ireland',size=13,weight='bold')

tprange_sun.set_axis_labels('Temperature Range (C)', 'Sunlight Hours (hrs)',size=10,weight='bold')