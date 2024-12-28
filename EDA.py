import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_paths = {r'/Users/thewang/Downloads/202021-hs-sqr-results.xlsx': '2020/21', r'/Users/thewang/Downloads/202122-hs-sqr-results.xlsx': '2021/22', r'/Users/thewang/Downloads/202223-hs-sqr-results.xlsx': '2022/23'}
pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)  # Auto-detect the width
pd.set_option('display.max_colwidth', None)  # No limit on column width

# The header skips the number of rows the next row will be your headers and if you are trying to use only certain columns
#df = pd.read_excel(file_paths, header=3, usecols="D:CV")  # Syntax (file,header,usecols) which help analyze the excel at a certain position
# This up here can only read one sheet at a time
master_data_struc = {}  # This initiates so I can have all the data centralized and without creating new excel sheets

for file, year in file_paths.items():   # accesing files and years from each file path
    loading_excel = pd.ExcelFile(file)  # This is so you can read multiple files and sheets
    year_data = {}  # In general initializing allows different type of data to be stored to be manipulated without being deleted
    for sheet_name in loading_excel.sheet_names:
        checking_cols = pd.read_excel(file, sheet_name=sheet_name, header=3, nrows=10)     # This is to get all the columns that arent empty
        cols = checking_cols.dropna(axis=1, how='all').columns
        usecols = cols.tolist()     # Put this into a lost so no errors
        sheetdata = pd.read_excel(loading_excel, sheet_name=sheet_name, header=3, usecols=usecols)
        year_data[sheet_name] = sheetdata   # stores the df of the files
    master_data_struc[year] = year_data


all_file_sheets = set()
for file, year in file_paths.items():   # This is to print all the sheet names in all of the excel sheets
    loading_excel = pd.ExcelFile(file)
    sheetname = loading_excel.sheet_names
    all_file_sheets.update(sheetname)


print(all_file_sheets)  # List of sheets for all excel sheets

data_2020 = master_data_struc['2020/21']["Summary"].head()
data_2021 = master_data_struc['2021/22']["Summary"].head()
data_2022 = master_data_struc['2022/23']["Summary"].head()
data_2020_Student = master_data_struc['2020/21']["Student Achievement"].head()
data_2021_Student = master_data_struc['2021/22']["Student Achievement"].head()
data_2022_Student = master_data_struc['2022/23']["Student Achievement"].head()
data_2020_Additional_Info = master_data_struc['2020/21']["Additional Info"].head()
data_2021_Additional_Info = master_data_struc['2021/22']["Additional Info"].head()
data_2022_Additional_Info = master_data_struc['2022/23']["Additional Info"].head()
data_2020_Framework = master_data_struc['2020/21']["Framework"].head()
data_2021_Framework = master_data_struc['2021/22']["Framework"].head()
data_2022_Framework = master_data_struc['2022/23']["Framework"].head()

#print(list(data_2020_Additional_Info.columns))

data_2020_Additional_Info.loc[:, 'Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam'] = pd.to_numeric(
    data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam'],
    errors='coerce'
)


data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'] = pd.to_numeric(data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'], errors='coerce')
data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam'] = pd.to_numeric(data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam'], errors='coerce')

print(data_2020_Additional_Info.dtypes)
print(data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Reading and Writing exam'].describe())
print(data_2020_Additional_Info['Metric Value - Average score of students in the current cohort who took the SAT Math exam'].describe())
