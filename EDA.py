import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
        numeric_col = pd.to_numeric(col, errors='coerce')
        return np.where(numeric_col.notna(), numeric_col, col)

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

all_data_Framework
