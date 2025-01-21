import pandas as pd
import numpy as np

# File paths and corresponding years
file_paths = {
    '/Users/thewang/Downloads/NYC High School Quality Data Set/2014_2015_hs_sqr_results_2016_04_08.xlsx': '2014/15',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/2015_2016_hs_sqr_results_2017_01_05.xlsx': '2015/16',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/2016-17_hs_sqr.xlsx': '2016/17',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/201718_hs_sqr_results.xlsx': '2017/18',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/201819_hs_sqr_results.xlsx': '2018/19',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/2019-20_School_Quality_Guide_High_School_Revision_.xlsx': '2019/20',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/202021-hs-sqr-results.xlsx': '2020/21',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/202122-hs-sqr-results.xlsx': '2021/22',
    '/Users/thewang/Downloads/NYC High School Quality Data Set/202223-hs-sqr-results.xlsx': '2022/23'
}

# Display options for DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('future.no_silent_downcasting', True)

# Constants for cleaning
UNWANTED_COLUMNS = {
    "Summary": ['School Type', 'Percent Female', 'Percent Male', 'Student Percent - Asian', 'Student Percent - Black',
                'Student Percent - Hispanic', 'Student Percent - Native American',
                'Student Percent - Native Hawaiian or Pacific Islander', 'Student Percent - White'],
    "Student Achievement": ['School Type', 'N count - 10+ Credits in 1st Year - All Students',
                            'Metric Value - 10+ Credits in 1st Year - All Students',
                            'N count - 10+ Credits in 2nd Year - All Students',
                            'Metric Value - 10+ Credits in 2nd Year - All Students'],
    "Framework": ['School Type', 'Metric Value - Percentage of Students with 90%+ Attendance',
                  'Quality Review - Dates Of Review'],
    "Additional Info": ['School Type', "N Count - Average Student Attendance",
                        "Metric Value - Average Student Attendance",
                        "N Count - Percentage of Students with 90%+ Attendance - Asian",
                        "Metric Value - Percentage of Students with 90%+ Attendance - Asian"]
}


# Function to clean and convert DataFrame
def convert_sheet_to_numeric_or_keep(df):
    def convert_numeric_or_keep(col):
        col = col.replace({'N<15': 0, 'N<5': 0, 'N/A': 0, '': 0})
        col = col.replace('%', '', regex=True)
        col = col.replace(r'^\s*$', '0', regex=True)
        numeric_col = pd.to_numeric(col, errors='coerce').fillna(value=col)
        return numeric_col
    return df.apply(lambda col: convert_numeric_or_keep(col))


# Master structure for all years and sheets
master_data = {}

# Load and clean all Excel files
for file, year in file_paths.items():
    loading_excel = pd.ExcelFile(file)
    master_data[year] = {}
    for sheet_name in loading_excel.sheet_names:
        try:
            # Determine columns dynamically
            preview = pd.read_excel(file, sheet_name=sheet_name, header=3, nrows=10)
            usecols = preview.dropna(axis=1, how='all').columns.tolist()

            # Load data
            data = pd.read_excel(file, sheet_name=sheet_name, header=3, usecols=usecols)
            data = convert_sheet_to_numeric_or_keep(data)

            # Drop unwanted columns
            if sheet_name in UNWANTED_COLUMNS:
                data = data.drop(columns=UNWANTED_COLUMNS[sheet_name], errors='ignore')

            master_data[year][sheet_name] = data
        except Exception as e:
            print(f"Error loading {sheet_name} from {year}: {e}")


# Accessing specific data
def get_sheet_data(year, sheet_name):
    return master_data.get(year, {}).get(sheet_name)


data_2020 = get_sheet_data('2020/21', 'Summary')
data_2021 = get_sheet_data('2021/22', 'Summary')
data_2022 = get_sheet_data('2022/23', 'Summary')
data_2020_Student = get_sheet_data('2020/21', "Student Achievement")
data_2021_Student = get_sheet_data('2021/22', "Student Achievement")
data_2022_Student = get_sheet_data('2022/23', "Student Achievement")
data_2014_Additional_Info = get_sheet_data('2014/15', "Additional Info")
data_2015_Additional_Info = get_sheet_data('2015/16', "Additional Info")
data_2016_Additional_Info = get_sheet_data('2016/17', "Additional Info")
data_2017_Additional_Info = get_sheet_data('2017/18', "Additional Info")
data_2018_Additional_Info = get_sheet_data('2018/19', "Additional Info")
data_2019_Additional_Info = get_sheet_data('2019/20', "Additional Info")
data_2020_Additional_Info = get_sheet_data('2020/21', "Additional Info")
data_2021_Additional_Info = get_sheet_data('2021/22', "Additional Info")
data_2022_Additional_Info = get_sheet_data('2022/23', "Additional Info")
data_2020_Framework = get_sheet_data('2020/21', "Framework")
data_2021_Framework = get_sheet_data('2021/22', "Framework")
data_2022_Framework = get_sheet_data('2022/23', "Framework")


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
all_years_SAT = (
    pd
    .concat(all_years_data, ignore_index=True)
    .sort_values(by='Year')
)
#print(all_years_SAT[all_years_SAT['Year'] == 2021].head(15))
#print(all_years_SAT.dtypes)
#This is to check out of all the school in the past 8 years what is the ranking
# sorted_df = all_years_SAT.sort_values(by='SAT Total', ascending=False)
# print(sorted_df[['School Name', 'SAT Total', 'Year']].head(10))

#top 10 per year sat scores
top_5_per_year = (
    all_years_SAT                                                       # DataFrame
    .groupby('Year', group_keys=False)                              # Grouping by the Year
    .apply(lambda x: x.sort_values(by='SAT Total', ascending=False))    # Since in a Group using apply to sort
    .head(5)                                                            # This is to get the top 5 from the sorted
)
#print(top_5_per_year[['School Name', 'SAT Total', 'Year']])

bottom_5_per_year = (
    all_years_SAT.groupby('Year', group_keys=False)
    .apply(lambda x: x.dropna(subset=['SAT Total'])
    .sort_values(by='SAT Total', ascending=False))
    .tail(5)
)
#print(bottom_5_per_year[['School Name', 'SAT Total', 'Year']])

avg_SAT_score = all_years_SAT.groupby('Year')['SAT Total'].mean().reset_index()     # Average SAT
#avg_SAT_score['percent_increase'] = avg_SAT_score['SAT Total'].pct_change()
#print(avg_SAT_score)
percentile_75 = all_years_SAT.groupby('Year')['SAT Total'].quantile(0.75).reset_index()  # 75th percentile SAT
percentile_95 = all_years_SAT.groupby('Year')['SAT Total'].quantile(0.95).reset_index()  # 75th percentile SAT

# I was trying to get data for what happens to students after graduation but the data is unusable
# keyword = 'Postsecondary'
# postsecondary_columns = [col for col in data_2022_Additional_Info.columns if keyword in col]
# print(data_2022_Additional_Info[postsecondary_columns].describe())
# null_zero = data_2022_Additional_Info[postsecondary_columns].isnull()|data_2022_Additional_Info[postsecondary_columns] == 0
# print(null_zero.sum())
#
# postsecondary_columns = [col for col in data_2021_Additional_Info.columns if keyword in col]
# print(data_2021_Additional_Info[postsecondary_columns].describe())
# null_zero = data_2021_Additional_Info[postsecondary_columns].isnull()|data_2021_Additional_Info[postsecondary_columns] == 0
# print(null_zero.sum())


total_SAT_score = all_years_SAT[all_years_SAT['Year'] == 2022][['DBN', 'SAT Total']].reset_index(drop=True)
# print(total_SAT_score[['DBN', 'SAT Total']])
# print(total_SAT_score.dtypes)
merged_2022 = pd.merge(data_2022, data_2022_Student, on="DBN", how="inner")
merged_2022 = pd.merge(merged_2022, data_2022_Additional_Info, on="DBN", how="inner")
merged_2022 = pd.merge(merged_2022, total_SAT_score, on="DBN", how="inner")
df_combined = merged_2022.copy()
# if len(total_SAT_score) == len(df_combined):
#     df_combined['SAT Total'] = total_SAT_score
# else:
#     # Handle the case where lengths don't match
#     print(f"Length mismatch: {len(df_combined)} != {len(total_SAT_score)}")
# df_combined['SAT Total'] = total_SAT_score
rem_keyword = ['Asian', 'Black', 'Hispanic', 'White', 'Pacific Islander', 'Native American', 'Comparison Group',
               'N count', 'Female', 'Male', 'Multiracial', 'N Count', 'Metric Rating', 'Comparison Group',
               'SAT Math', 'SAT Reading']
df_combined = df_combined.drop([col for col in df_combined.columns if any(k in col for k in rem_keyword)], axis=1)
numeric_df = df_combined.select_dtypes(include=['number'])
numeric_df.columns = (
    numeric_df.columns
    .str.replace('Metric Value - ', '', regex=False)  # Remove specific substring
    .str.replace('Metric Score - ', '', regex=False)
    .str.replace('Average', 'Avg.', regex=False)
    .str.replace('Percentage ', '% ', regex=False)
    .str.replace('Percentage of students ', '% Students ', regex=False)
    .str.replace('Percent ', '% ', regex=False)
    .str.replace('of ', '', regex=False)
    .str.replace('in ', '', regex=False)
    .str.replace('for ', '', regex=False)
    .str.replace('with ', '', regex=False)
    .str.replace('High School ', 'H.S. ', regex=False)
    .str.replace('Graduation ', 'Grad.', regex=False)
    .str.replace('who took the ', '', regex=False)
    .str.replace('in the current cohort who took the ', '', regex=False)
    .str.replace('English', 'Eng.', regex=False)
    .str.replace('Postsecondary Enrollment', 'Postsec. Enrollment', regex=False)
    .str.replace('recommended', 'rec.', regex=False)
    .str.replace('Out Students at ', '', regex=False)
    .str.replace('the current cohort ', '', regex=False)
    .str.replace('the current year who ', '', regex=False)
    .str.replace('are college ready ', '', regex=False)
    .str.replace('Lowest Third Citywide', 'L 3rd CW', regex=False)
    .str.replace('Students Who', '', regex=False)
    .str.replace('and', '&', regex=False)
    .str.replace('months', 'M', regex=False)
    .str.replace('Months', 'M', regex=False)
    .str.replace('year', 'Y', regex=False)
    .str.replace('Algebra', 'Alg', regex=False)
    .str.replace('Chemistry', 'Chem', regex=False)
    .str.replace('scored ', '', regex=False)
)
numeric_df = numeric_df.rename(columns={
    'SAT Total_x': 'SAT Total',
    '% students rec. general ed settings Special Ed Teacher Support Services (SETSS)': '% students rec. SETSS',
    '% students rec. Integrated Co-Teaching (ICT) services' : '% students rec. ICT',
    '% students who took a Languages Other Than Eng. Regents scored 65+': '% students Other Languages Regents scored 65+',
    'Movement Students IEPs to Less Restrictive Environments': 'Less Restrictive Environments',
    '% students Eng. Regents exam & (scored 70+)': '% students Eng. Regents (scored 70+)',
    '% students Geometry Regents exam & (scored 70+)': '% students Geometry Regents (scored 70+)',
    '% students Alg I Regents exam & (scored 70+)': '% students Alg I Regents (scored 70+)',
})
numeric_df = numeric_df.drop('SAT Total_y', axis=1)
for col in numeric_df.columns:
    print(col)
