from EDA import data_2020, data_2021, data_2022, data_2020_Student, data_2021_Student, data_2022_Student, data_2020_Framework, data_2021_Framework, data_2022_Framework, data_2014_Additional_Info, data_2015_Additional_Info, data_2016_Additional_Info, data_2017_Additional_Info, data_2018_Additional_Info, data_2019_Additional_Info, data_2020_Additional_Info, data_2021_Additional_Info, data_2022_Additional_Info
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import numpy as np

# I need to also find a better way to deal with this too
data_2014_Additional_Info['SAT Total'] = data_2014_Additional_Info['Average Score SAT Math'] + data_2014_Additional_Info['Average Score SAT Writing']
data_2015_Additional_Info['SAT Total'] = data_2015_Additional_Info['Average Score SAT Math'] + data_2015_Additional_Info['Average Score SAT Writing']
data_2016_Additional_Info['SAT Total'] = data_2016_Additional_Info['Metric Value - Average Score SAT Math'] + data_2016_Additional_Info['Metric Value - Average Score SAT Reading and Writing']
data_2017_Additional_Info['SAT Total'] = data_2017_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2017_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
data_2018_Additional_Info['SAT Total'] = data_2018_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2018_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
data_2019_Additional_Info['SAT Total'] = data_2019_Additional_Info['val_mean_score_sat_math_all'] + data_2019_Additional_Info['val_mean_score_sat_writ_all']
data_2020_Additional_Info['SAT Total'] = data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
data_2021_Additional_Info['SAT Total'] = data_2021_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2021_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
data_2022_Additional_Info['SAT Total'] = data_2022_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2022_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']

data_2014_Additional_Info['SAT Total'] = pd.to_numeric(data_2014_Additional_Info['SAT Total'], errors='coerce')
data_2015_Additional_Info['SAT Total'] = pd.to_numeric(data_2015_Additional_Info['SAT Total'], errors='coerce')
data_2016_Additional_Info['SAT Total'] = pd.to_numeric(data_2016_Additional_Info['SAT Total'], errors='coerce')
data_2017_Additional_Info['SAT Total'] = pd.to_numeric(data_2017_Additional_Info['SAT Total'], errors='coerce')
data_2018_Additional_Info['SAT Total'] = pd.to_numeric(data_2018_Additional_Info['SAT Total'], errors='coerce')
data_2019_Additional_Info['SAT Total'] = pd.to_numeric(data_2019_Additional_Info['SAT Total'], errors='coerce')

data_2014_Additional_Info = data_2014_Additional_Info[data_2014_Additional_Info['SAT Total'] != 0]
data_2015_Additional_Info = data_2015_Additional_Info[data_2015_Additional_Info['SAT Total'] != 0]
data_2016_Additional_Info = data_2016_Additional_Info[data_2016_Additional_Info['SAT Total'] != 0]
data_2017_Additional_Info = data_2017_Additional_Info[data_2017_Additional_Info['SAT Total'] != 0]
data_2018_Additional_Info = data_2018_Additional_Info[data_2018_Additional_Info['SAT Total'] != 0]
data_2019_Additional_Info = data_2019_Additional_Info[data_2019_Additional_Info['SAT Total'] != 0]
data_2020_Additional_Info = data_2020_Additional_Info[data_2020_Additional_Info['SAT Total'] != 0]
data_2021_Additional_Info = data_2021_Additional_Info[data_2021_Additional_Info['SAT Total'] != 0]
data_2022_Additional_Info = data_2022_Additional_Info[data_2022_Additional_Info['SAT Total'] != 0]

data_2014_Additional_Info = data_2014_Additional_Info.copy()
data_2015_Additional_Info = data_2015_Additional_Info.copy()
data_2016_Additional_Info = data_2016_Additional_Info.copy()
data_2017_Additional_Info = data_2017_Additional_Info.copy()
data_2018_Additional_Info = data_2018_Additional_Info.copy()
data_2019_Additional_Info = data_2019_Additional_Info.copy()
data_2020_Additional_Info = data_2020_Additional_Info.copy()
data_2021_Additional_Info = data_2021_Additional_Info.copy()
data_2022_Additional_Info = data_2022_Additional_Info.copy()

data_2014_Additional_Info.loc[:, 'Year'] = 2014
data_2015_Additional_Info.loc[:, 'Year'] = 2015
data_2016_Additional_Info.loc[:, 'Year'] = 2016
data_2017_Additional_Info.loc[:, 'Year'] = 2017
data_2018_Additional_Info.loc[:, 'Year'] = 2018
data_2019_Additional_Info.loc[:, 'Year'] = 2019
data_2020_Additional_Info.loc[:, 'Year'] = 2020
data_2021_Additional_Info.loc[:, 'Year'] = 2021
data_2022_Additional_Info.loc[:, 'Year'] = 2022


all_years_SAT = pd.concat([data_2014_Additional_Info, data_2015_Additional_Info, data_2016_Additional_Info, data_2017_Additional_Info, data_2018_Additional_Info,data_2019_Additional_Info, data_2020_Additional_Info, data_2021_Additional_Info, data_2022_Additional_Info], ignore_index=True)
all_years_SAT = all_years_SAT.sort_values(by='Year')
avg_SAT_score = all_years_SAT.groupby('Year')['SAT Total'].mean().reset_index()
plt.scatter(all_years_SAT['Year'], all_years_SAT['SAT Total'], label='Data Points', color='blue')
plt.plot(avg_SAT_score['Year'], avg_SAT_score['SAT Total'], label='Average Trend Line', color='orange', linewidth=2)
plt.xlabel('Year')
plt.ylabel('SAT Total')
plt.title('SAT Total Scores Over Years')
plt.legend()
plt.show()