import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import numpy as np

file_paths = {r'/Users/thewang/Downloads/NYC High School Quality Data Set/2014_2015_hs_sqr_results_2016_04_08.xlsx': '2014/15',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/2015_2016_hs_sqr_results_2017_01_05.xlsx': '2015/16',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/2016-17_hs_sqr.xlsx': '2016/17',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/201718_hs_sqr_results.xlsx': '2017/18',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/201819_hs_sqr_results.xlsx': '2018/19',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/202021-hs-sqr-results.xlsx': '2020/21',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/202122-hs-sqr-results.xlsx': '2021/22',
              r'/Users/thewang/Downloads/NYC High School Quality Data Set/202223-hs-sqr-results.xlsx': '2022/23'
}

pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)  # Auto-detect the width
pd.set_option('display.max_colwidth', None)  # No limit on column width
pd.set_option('future.no_silent_downcasting', True)
# The header skips the number of rows the next row will be your headers and if you are trying to use only certain columns
#df = pd.read_excel(file_paths, header=3, usecols="D:CV")  # Syntax (file,header,usecols) which help analyze the excel at a certain position
# This up here can only read one sheet at a time
master_data_struc = {}  # This initiates so I can have all the data centralized and without creating new excel sheets

for file, year in file_paths.items():
    loading_excel = pd.ExcelFile(file)
    year_data = {}
    for sheet_name in loading_excel.sheet_names:
        checking_cols = pd.read_excel(file, sheet_name=sheet_name, header=3, nrows=10)
        cols = checking_cols.dropna(axis=1, how='all').columns
        usecols = [str(col) for col in cols]  # Ensure usecols is a list of strings
        #print(f"Columns to use for {sheet_name}: {usecols}")

        try:
            sheetdata = pd.read_excel(loading_excel, sheet_name=sheet_name, header=3, usecols=usecols)
            print(sheetdata)
            year_data[sheet_name] = sheetdata
        except ValueError as e:
            print(f"Error reading {sheet_name}: {e}")

    master_data_struc[year] = year_data

all_file_sheets = set()
for file, year in file_paths.items():   # This is to print all the sheet names in all of the excel sheets
    loading_excel = pd.ExcelFile(file)
    sheetname = loading_excel.sheet_names
    all_file_sheets.update(sheetname)
print(all_file_sheets)  # List of sheets for all excel sheets

def convert_sheet_to_numeric_or_keep(df):       # this is to clean the data a little so I can use it better
    def convert_numeric_or_keep(col):
        col = col.replace({'N<15': 0, 'N<5': 0, 'N/A': 0, '': 0})
        col = col.replace('%', '', regex=True)
        col = col.replace(r'^\s*$', '0', regex=True)
        numeric_col = pd.to_numeric(col, errors='coerce')
        return np.where(numeric_col.notna(), numeric_col, col)
    return df.apply(lambda col: convert_numeric_or_keep(col))

#print(master_data_struc.keys())
data_2020 = convert_sheet_to_numeric_or_keep(master_data_struc['2020/21']["Summary"])    #Ill be looking for a better way to get this streamlined so I dont need to creat a line each time
data_2021 = convert_sheet_to_numeric_or_keep(master_data_struc['2021/22']["Summary"])
data_2022 = convert_sheet_to_numeric_or_keep(master_data_struc['2022/23']["Summary"])
data_2020_Student = convert_sheet_to_numeric_or_keep(master_data_struc['2020/21']["Student Achievement"])
data_2021_Student = convert_sheet_to_numeric_or_keep(master_data_struc['2021/22']["Student Achievement"])
data_2022_Student = convert_sheet_to_numeric_or_keep(master_data_struc['2022/23']["Student Achievement"])
data_2014_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2014/15']["Additional Info"])
data_2015_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2015/16']["Additional Info"])
data_2016_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2016/17']["Additional Info"])
data_2017_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2017/18']["Additional Info"])
data_2018_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2018/19']["Additional Info"])
#data_2019_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2019/20']["Additional Info"])
data_2020_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2020/21']["Additional Info"])
data_2021_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2021/22']["Additional Info"])
data_2022_Additional_Info = convert_sheet_to_numeric_or_keep(master_data_struc['2022/23']["Additional Info"])
data_2020_Framework = convert_sheet_to_numeric_or_keep(master_data_struc['2020/21']["Framework"])
data_2021_Framework = convert_sheet_to_numeric_or_keep(master_data_struc['2021/22']["Framework"])
data_2022_Framework = convert_sheet_to_numeric_or_keep(master_data_struc['2022/23']["Framework"])

print(len(data_2020_Additional_Info.columns))
unwanted_data_columns1 = ['School Type', 'Percent Female', 'Percent Male', 'Student Percent - Asian',
                          'Student Percent - Black', 'Student Percent - Hispanic', 'Student Percent - Native American',
                          'Student Percent - Native Hawaiian or Pacific Islander', 'Student Percent - White'
                          ]
unwanted_data_columns2 = [
    'School Type',
    'N count - 10+ Credits in 1st Year - All Students',
    'Metric Value - 10+ Credits in 1st Year - All Students',
    'N count - 10+ Credits in 2nd Year - All Students',
    'Metric Value - 10+ Credits in 2nd Year - All Students',
    'N count - 10+ Credits in 3rd Year - All Students',
    'Metric Value - 10+ Credits in 3rd Year - All Students',
    "N count - 10+ Credits in 3rd Year - School's Lowest Third",
    "Metric Value - 10+ Credits in 3rd Year - School's Lowest Third",
    'N count - Percentage of Students with 90%+ Attendance',
    'Metric Value - Percentage of Students with 90%+ Attendance'
]
unwanted_data_columns3 = ['School Type', 'Metric Value - Percentage of Students with 90%+ Attendance',
                          'Quality Review - Dates Of Review']
unwanted_data_columns4 = ['School Type', "N Count - Average Student Attendance",
                          "Metric Value - Average Student Attendance",
                          "N Count - Average Student Attendance - In-person days",
                          "Metric Value - Average Student Attendance - In-person days",
                          "N Count - Average Student Attendance - Remote days",
                          "Metric Value - Average Student Attendance - Remote days",
                          "N Count - Percentage of Students with 90%+ Attendance - Asian",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Asian",
                          "N Count - Percentage of Students with 90%+ Attendance - Black",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Black",
                          "N Count - Percentage of Students with 90%+ Attendance - Hispanic",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Hispanic",
                          "N Count - Percentage of Students with 90%+ Attendance - Native American",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Native American",
                          "N Count - Percentage of Students with 90%+ Attendance - Multiracial",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Multiracial",
                          "N Count - Percentage of Students with 90%+ Attendance - Native Hawaiian or Pacific Islander",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Native Hawaiian or Pacific Islander",
                          "N Count - Percentage of Students with 90%+ Attendance - White",
                          "Metric Value - Percentage of Students with 90%+ Attendance - White",
                          "N Count - Percentage of Students with 90%+ Attendance - Female",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Female",
                          "N Count - Percentage of Students with 90%+ Attendance - Male",
                          "Metric Value - Percentage of Students with 90%+ Attendance - Male"]

data_2020 = data_2020.drop(unwanted_data_columns1, axis=1)
data_2021 = data_2021.drop(unwanted_data_columns1, axis=1)
data_2022 = data_2022.drop(unwanted_data_columns1, axis=1)

data_2020_Student = data_2020_Student.drop(unwanted_data_columns2, axis=1, errors='ignore')
data_2021_Student = data_2021_Student.drop(unwanted_data_columns2, axis=1, errors='ignore')
data_2022_Student = data_2022_Student.drop(unwanted_data_columns2, axis=1, errors='ignore')

data_2020_Framework = data_2020_Framework.drop(unwanted_data_columns3, axis=1, errors='ignore')
data_2021_Framework = data_2021_Framework.drop(unwanted_data_columns3, axis=1, errors='ignore')
data_2022_Framework = data_2022_Framework.drop(unwanted_data_columns3, axis=1, errors='ignore')

data_2020_Additional_Info = data_2020_Additional_Info.drop(unwanted_data_columns4, axis=1, errors='ignore')
data_2021_Additional_Info = data_2021_Additional_Info.drop(unwanted_data_columns4, axis=1, errors='ignore')
data_2022_Additional_Info = data_2022_Additional_Info.drop(unwanted_data_columns4, axis=1, errors='ignore')

#print(len(data_2020_Additional_Info.columns))



# #df = df.rename(columns = {'name on sheets': 'name wanted',...etc)  #this is to rename so it can be easier to read
# #df.duplicated()    #this is to find if there are any duplicated in the dataset
#
# print(list(data_2020_Additional_Info.columns))
# # print(data_2020_Additional_Info.isnull().sum())   # This is to find the number of missing data in each column
# # print(data_2020_Additional_Info.describe())
# data_2020_Additional_Info = data_2020_Additional_Info.apply(pd.to_numeric, errors='coerce')
#
# # Now calculate the correlation
# # sns.heatmap(data_2020_Additional_Info.corr(), annot=True)
# # plt.rcParams['figure.figsize'] = (10, 10)
# # plt.show(block=True)
# remove_word = ['Asian', 'Black', 'Hispanic', 'Native American', 'Multiracial', 'Native Hawaiian', 'Pacific Islander',
#              'White', 'Latinx', 'Female', 'Male']
# remove_col = [col for col in data_2020.columns if not any(word in col for word in remove_word)]
# #print(remove_race)
#
# # metrics = ['Metric']
# # metrics_value = [col for col in remove_col if any(word in col for word in metrics)]
# # print(metrics_value)
#
# data_2020 = data_2020[remove_col].select_dtypes(include=['number'])
# print(data_2020)
# sns.heatmap(data_2020.corr(), annot=True)
# #plt.rcParams['figure.figsize'] = (10, 10)
# plt.show(block=True)
# # metrics_2020_Student = [col for col in data_2020_Student.columns if any(word in col for word in metrics)]
# #
# # # Select the relevant columns from the DataFrame
# # metrics_df_2020_Student = data_2020_Student[metrics_2020_Student]
# #
# # # Apply numeric conversion to the DataFrame
# # metrics_df_2020_Student = convert_sheet_to_numeric_or_keep(metrics_df_2020_Student)
# #
# # # Calculate and print the correlation matrix
# # print(metrics_df_2020_Student.corr())
# # plt.figure(figsize=(10, 10))
# # sns.heatmap(metrics_df_2020_Student.corr(), annot=True, cmap="coolwarm")
# # plt.title("Correlation Heatmap for Metrics 2020 Student")
# # plt.show()
# #
# # print(data_2020_Student.dtypes)
# # print(data_2020_Additional_Info.dtypes)
# # # Convert DBN columns to string type to ensure compatibility
# # data_2020_Student['DBN'] = data_2020_Student['DBN'].astype(str)
# # data_2020_Additional_Info['DBN'] = data_2020_Additional_Info['DBN'].astype(str)
# #
# # # Merge the two sheets on a common column
# # merged_data = pd.merge(data_2020_Student, data_2020_Additional_Info, on='DBN', how='inner')
# #
# # # Select the columns you want to correlate
# # columns_to_correlate = [
# #     'N count - 4-Year High School Persistence Rate',
# #     'Metric Value - 4-Year High School Persistence Rate',
# #     'N count - 6-Year High School Persistence Rate',
# #     'Metric Value - 6-Year High School Persistence Rate',
# #     'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam',
# #     'Metric Value - Average score of students in the current cohort who took the SAT Math exam'
# # ]
# #
# # # Ensure numeric conversion
# # merged_data[columns_to_correlate] = merged_data[columns_to_correlate].apply(pd.to_numeric, errors='coerce')
# #
# # # Check for columns that have too many NaN values
# # nan_counts = merged_data[columns_to_correlate].isna().sum()
# # print("NaN counts per column:")
# # print(nan_counts)
# #
# # # Option 1: Drop rows with NaN values in the selected columns
# # cleaned_data = merged_data[columns_to_correlate].dropna()
# #
# # # Option 2: Fill NaN values with the mean of each column (if you prefer not to drop rows)
# # #cleaned_data = merged_data[columns_to_correlate].fillna(merged_data[columns_to_correlate].mean())
# #
# # # Calculate the correlation matrix
# # correlation_matrix = cleaned_data.corr()
# #
# # # Print the correlation matrix
# # print(correlation_matrix)
# #
# # # Visualize the correlation matrix using a heatmap
# # plt.figure(figsize=(10, 8))
# # sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
# # plt.title("Correlation Heatmap")
# # plt.show()

