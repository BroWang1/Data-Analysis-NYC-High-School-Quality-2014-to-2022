from EDA import data_2020, data_2021, data_2022, data_2020_Student, data_2021_Student, data_2022_Student, data_2020_Framework, data_2021_Framework, data_2022_Framework, data_2014_Additional_Info, data_2015_Additional_Info, data_2016_Additional_Info, data_2017_Additional_Info, data_2018_Additional_Info, data_2019_Additional_Info, data_2020_Additional_Info, data_2021_Additional_Info, data_2022_Additional_Info
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import numpy as np


def process_year_data(data, year, sat_math_score, sat_writing_score, new_column_name='SAT Total'):
    data[new_column_name] = data[sat_math_score] + data[sat_writing_score]  # total sat score
    data[new_column_name] = pd.to_numeric(data[new_column_name], errors='coerce')   # now we make sure that it is numeric
    # Remove rows with SAT Total equal to 0 or missing
    data = data[data[new_column_name] != 0]
    # Add year column
    data = data.copy()
    data.loc[:, 'Year'] = year
    return data

# List of years and corresponding column names for SAT math and writing scores
years_data = [
    (2014, 'Average Score SAT Math', 'Average Score SAT Writing', 'SAT Total'),
    (2015, 'Average Score SAT Math', 'Average Score SAT Writing', 'SAT Total'),
    (2016, 'Metric Value - Average Score SAT Math', 'Metric Value - Average Score SAT Reading and Writing', 'SAT Total'),
    (2017, 'Metric Value - Average score of students in the current cohort who took the SAT Math exam',
     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
     'SAT Total'),
    (2018, 'Metric Value - Average score of students in the current cohort who took the SAT Math exam',
     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
     'SAT Total'),
    (2019, 'val_mean_score_sat_math_all', 'val_mean_score_sat_writ_all', 'SAT Total'),
    (2020, 'Metric Value - Average score of students in the current cohort who took the SAT Math exam',
     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
     'SAT Total'),
    (2021, 'Metric Value - Average score of students in the current cohort who took the SAT Math exam',
     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
     'SAT Total'),
    (2022, 'Metric Value - Average score of students in the current cohort who took the SAT Math exam',
     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
     'SAT Total')
]

# Loading the data dynamically (assuming the data variables are already loaded as before)
all_years_data = []
for year, sat_math_col, sat_writing_col, new_column_name in years_data:
    data = globals().get(f"data_{year}_Additional_Info")
    if data is not None:
        processed_data = process_year_data(data, year, sat_math_col, sat_writing_col, new_column_name)
        all_years_data.append(processed_data)

# Combine all the processed data into one DataFrame
all_years_SAT = pd.concat(all_years_data, ignore_index=True).sort_values(by='Year')
#This is to check out of all the school in the past 8 years what is the ranking
# sorted_df = all_years_SAT.sort_values(by='SAT Total', ascending=False)
# print(sorted_df[['School Name', 'SAT Total', 'Year']].head(10))

#top 10 per year sat scores
top_5_per_year = all_years_SAT.groupby('Year', group_keys=False).apply(
    lambda x: x.sort_values(by='SAT Total', ascending=False).head(5)
)
print(top_5_per_year[['School Name', 'SAT Total', 'Year']])

bottom_5_per_year = all_years_SAT.groupby('Year', group_keys=False).apply(
    lambda x: x.dropna(subset=['SAT Total']).sort_values(by='SAT Total', ascending=False).tail(5)
)
print(bottom_5_per_year[['School Name', 'SAT Total', 'Year']])

avg_SAT_score = all_years_SAT.groupby('Year')['SAT Total'].mean().reset_index()     # Average SAT
percentile_75 = all_years_SAT.groupby('Year')['SAT Total'].quantile(0.75).reset_index()  # 75th percentile SAT
print(percentile_75)
plt.scatter(all_years_SAT['Year'], all_years_SAT['SAT Total'], label='Data Points', color='blue')
plt.plot(avg_SAT_score['Year'], avg_SAT_score['SAT Total'], label='Average Trend Line', color='orange', linewidth=2)
plt.plot(percentile_75['Year'], percentile_75['SAT Total'], label='75% Percentile Trend Line', color='red', linewidth=2)
plt.xlabel('Year')
plt.ylabel('SAT Total')
plt.title('SAT Total Scores Over Years')
plt.legend()
plt.show()
# How I orginally did it
# data_2014_Additional_Info['SAT Total'] = data_2014_Additional_Info['Average Score SAT Math'] + data_2014_Additional_Info['Average Score SAT Writing']
# data_2015_Additional_Info['SAT Total'] = data_2015_Additional_Info['Average Score SAT Math'] + data_2015_Additional_Info['Average Score SAT Writing']
# data_2016_Additional_Info['SAT Total'] = data_2016_Additional_Info['Metric Value - Average Score SAT Math'] + data_2016_Additional_Info['Metric Value - Average Score SAT Reading and Writing']
# data_2017_Additional_Info['SAT Total'] = data_2017_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2017_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
# data_2018_Additional_Info['SAT Total'] = data_2018_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2018_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
# data_2019_Additional_Info['SAT Total'] = data_2019_Additional_Info['val_mean_score_sat_math_all'] + data_2019_Additional_Info['val_mean_score_sat_writ_all']
# data_2020_Additional_Info['SAT Total'] = data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
# data_2021_Additional_Info['SAT Total'] = data_2021_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2021_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
# data_2022_Additional_Info['SAT Total'] = data_2022_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] + data_2022_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam']
#
# data_2014_Additional_Info['SAT Total'] = pd.to_numeric(data_2014_Additional_Info['SAT Total'], errors='coerce')
# data_2015_Additional_Info['SAT Total'] = pd.to_numeric(data_2015_Additional_Info['SAT Total'], errors='coerce')
# data_2016_Additional_Info['SAT Total'] = pd.to_numeric(data_2016_Additional_Info['SAT Total'], errors='coerce')
# data_2017_Additional_Info['SAT Total'] = pd.to_numeric(data_2017_Additional_Info['SAT Total'], errors='coerce')
# data_2018_Additional_Info['SAT Total'] = pd.to_numeric(data_2018_Additional_Info['SAT Total'], errors='coerce')
# data_2019_Additional_Info['SAT Total'] = pd.to_numeric(data_2019_Additional_Info['SAT Total'], errors='coerce')
#
# data_2014_Additional_Info = data_2014_Additional_Info[data_2014_Additional_Info['SAT Total'] != 0]
# data_2015_Additional_Info = data_2015_Additional_Info[data_2015_Additional_Info['SAT Total'] != 0]
# data_2016_Additional_Info = data_2016_Additional_Info[data_2016_Additional_Info['SAT Total'] != 0]
# data_2017_Additional_Info = data_2017_Additional_Info[data_2017_Additional_Info['SAT Total'] != 0]
# data_2018_Additional_Info = data_2018_Additional_Info[data_2018_Additional_Info['SAT Total'] != 0]
# data_2019_Additional_Info = data_2019_Additional_Info[data_2019_Additional_Info['SAT Total'] != 0]
# data_2020_Additional_Info = data_2020_Additional_Info[data_2020_Additional_Info['SAT Total'] != 0]
# data_2021_Additional_Info = data_2021_Additional_Info[data_2021_Additional_Info['SAT Total'] != 0]
# data_2022_Additional_Info = data_2022_Additional_Info[data_2022_Additional_Info['SAT Total'] != 0]
#
# data_2014_Additional_Info = data_2014_Additional_Info.copy()
# data_2015_Additional_Info = data_2015_Additional_Info.copy()
# data_2016_Additional_Info = data_2016_Additional_Info.copy()
# data_2017_Additional_Info = data_2017_Additional_Info.copy()
# data_2018_Additional_Info = data_2018_Additional_Info.copy()
# data_2019_Additional_Info = data_2019_Additional_Info.copy()
# data_2020_Additional_Info = data_2020_Additional_Info.copy()
# data_2021_Additional_Info = data_2021_Additional_Info.copy()
# data_2022_Additional_Info = data_2022_Additional_Info.copy()
#
# data_2014_Additional_Info.loc[:, 'Year'] = 2014
# data_2015_Additional_Info.loc[:, 'Year'] = 2015
# data_2016_Additional_Info.loc[:, 'Year'] = 2016
# data_2017_Additional_Info.loc[:, 'Year'] = 2017
# data_2018_Additional_Info.loc[:, 'Year'] = 2018
# data_2019_Additional_Info.loc[:, 'Year'] = 2019
# data_2020_Additional_Info.loc[:, 'Year'] = 2020
# data_2021_Additional_Info.loc[:, 'Year'] = 2021
# data_2022_Additional_Info.loc[:, 'Year'] = 2022
#
#
# all_years_SAT = pd.concat([data_2014_Additional_Info, data_2015_Additional_Info, data_2016_Additional_Info, data_2017_Additional_Info, data_2018_Additional_Info,data_2019_Additional_Info, data_2020_Additional_Info, data_2021_Additional_Info, data_2022_Additional_Info], ignore_index=True)
# all_years_SAT = all_years_SAT.sort_values(by='Year')
# avg_SAT_score = all_years_SAT.groupby('Year')['SAT Total'].mean().reset_index()
# plt.scatter(all_years_SAT['Year'], all_years_SAT['SAT Total'], label='Data Points', color='blue')
# plt.plot(avg_SAT_score['Year'], avg_SAT_score['SAT Total'], label='Average Trend Line', color='orange', linewidth=2)
# plt.xlabel('Year')
# plt.ylabel('SAT Total')
# plt.title('SAT Total Scores Over Years')
# plt.legend()
# plt.show()