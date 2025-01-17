from EDA import all_years_SAT, avg_SAT_score, percentile_75, numeric_df
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import numpy as np

#SAT Scatter Plot
# plt.scatter(all_years_SAT['Year'], all_years_SAT['SAT Total'], label='Data Points', color='blue')
# plt.plot(avg_SAT_score['Year'], avg_SAT_score['SAT Total'], label='Average Trend Line', color='orange', linewidth=2)
# plt.plot(percentile_75['Year'], percentile_75['SAT Total'], label='75% Percentile Trend Line', color='red', linewidth=2)
# plt.xlabel('Year')
# plt.ylabel('SAT Total')
# plt.title('SAT Total Scores Over Years')
# plt.legend()
# plt.show()

#SAT Correlation
corr_matrix = numeric_df.corr()
sat_column = 'SAT Total_y'
column_correlations = corr_matrix.loc[sat_column]
mask = (column_correlations < -0.5) | (column_correlations > 0.5)
filtered_correlation_matrix = corr_matrix.loc[mask, mask]
filtered_correlation_matrix = corr_matrix.loc[:, mask].loc[mask, :]
plt.figure(figsize=(8, 6))
sns.heatmap(filtered_correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()