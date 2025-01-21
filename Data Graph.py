from EDA import all_years_SAT, avg_SAT_score, percentile_75, percentile_95, numeric_df
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns

# SAT Scatter Plot
# plt.scatter(all_years_SAT['Year'], all_years_SAT['SAT Total'], marker='o',
#             edgecolors='#505050', facecolors='none', s=100, label='Data Points')
# plt.plot(avg_SAT_score['Year'], avg_SAT_score['SAT Total'], label='Average Trend Line', color='#ffcb03', linewidth=2)
# plt.plot(percentile_75['Year'], percentile_75['SAT Total'], label='75% Percentile Trend Line', color='#c80a1b', linewidth=2)
# plt.plot(percentile_95['Year'], percentile_95['SAT Total'], label='95% Percentile Trend Line', color='#58b848', linewidth=2)
#
# plt.xlabel('Year')
# plt.ylabel('SAT Total')
# plt.title('SAT Total Scores Over Years')
# plt.legend()
# plt.show()

#SAT Correlation
corr_matrix = numeric_df.corr()
sat_column = 'SAT Total'
column_correlations = corr_matrix.loc[sat_column]
mask = (column_correlations == 1) | (column_correlations > .7) #| (column_correlations > 0.7)
filtered_correlation_matrix = corr_matrix.loc[mask, mask]
filtered_correlation_matrix = corr_matrix.loc[:, mask].loc[mask, :]
plt.figure(figsize=(8, 6))
sns.heatmap(filtered_correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()