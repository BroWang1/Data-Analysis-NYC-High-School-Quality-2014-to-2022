import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
                            # The header skips the number of rows the next row will be your headers and if you are trying to use only certain columns
df = pd.read_excel(r'/Users/thewang/Downloads/202223-hs-sqr-results.xlsx', header=3, usecols="D:CV")  # Syntax (file,header,usecols) which help analyze the excel at a certain position
print(df.columns)
