# Data Analysis NYC High School Quality EDA
___
# Overview
This dataset is sourced from the New York City Department of Education (DOE) and provides valuable insights into the performance of students and the quality of high schools in NYC. The data spans several academic years, from 2014 to 2022, and contains information on various factors such as student achievement, school environment, and additional educational metrics. This dataset allows for in-depth analysis of school performance and can be used to gain insights into trends over time, regional differences, and factors that impact student success.
___
# Data Processing
This repository contains code for processing and cleaning the raw Excel data. It includes functions for:  
Loading Data: Importing data from multiple Excel files (one for each academic year).  
Data Cleaning: Removing unwanted columns, handling missing values, and converting data types for analysis (e.g., converting scores to numeric values).  
Merging Data: Combining various data points (like SAT scores and demographic information) for further analysis.  
Aggregation: Summarizing data for key performance metrics (e.g., average SAT scores, top-performing schools).  
___
# Results
![Scatter plot w/ lines - 2014 to 2022](images/scattertl.png)
Notable Insight:
- 12.1% Increase in 2016 due to restructuring the SAT test  
- From 2016 to 2022 we have dropped 5.39% or 51 points  
- Right-skewed distribution since the 75th Percentile is close to the mean  

![Heatmap](images/heatmap.png)
Notable Insight:




# Data Source

https://infohub.nyced.org/reports/students-and-schools/school-quality/school-quality-reports-and-resources/school-quality-report-citywide-data

There are the excel files as well in the repository just in case you can't find it on the website.
