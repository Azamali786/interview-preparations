# This file will contain learning resources, notes and other stack realted informations #


- In pandas table is called dataframe
- pandas supports integration with many file formats or data structures out of the box (csv, excel, sql, json, parquet ...)
- importing data from each of these data sources is provided by function with prefix read_* 
- like read_csv, read_sql, read_json etc
- Similarly to_*  method is used to store data like to_csv, to_sql, to_json
- 



# Pandas Interview Questions #

    ##  Beginner Level ##

        1- What is Pandas?
        2- What are the main data structures in Pandas?
        3- How to create a Series from a list?
        4- How to create a DataFrame from a dictionary?
        5- Difference between a Series and a DataFrame?
        6- How to read a CSV file into a DataFrame?
        7- How to write a DataFrame to a CSV file?
        8- How to display the first 5 rows of a DataFrame?
        9- How to display the last 5 rows of a DataFrame?
        10- How to get the number of rows and columns in a DataFrame?
        11- How to list column names in a DataFrame?
        12- How to select one column from a DataFrame?
        13- How to select multiple columns from a DataFrame?
        14- What is the difference between .loc[] and .iloc[]?
        15- How to slice rows using .iloc[]?
        16- How to filter rows based on column values?
        17- How to find the number of missing values in each column?
        18- How to fill missing values with a specific value?
        19- How to drop rows with missing data?
        20- How to rename columns in a DataFrame?
        21- How to change the datatype of a column?
        22- How to create a new column from existing columns?
        23- How to delete a column from a DataFrame?
        24- How to reset the index of a DataFrame?
        25- How to set a specific column as the index?
        26- How to sort a DataFrame by a column in ascending/descending order?
        27- How to check if a DataFrame is empty?
        28- How to find unique values in a column?
        29- How to count the number of unique values in a column?
        30- How to check for duplicate rows?

    ## Intermediate level question ##
        31. How to remove duplicate rows from a DataFrame?
        32. How to replace values in a column?
        33. How does .apply() differ from .map()?
        34. How to apply a custom function to a column?
        35. How to group data by a column and apply aggregation?
        36. How to calculate mean, median, and mode of a column?
        37. How to perform multiple aggregations (sum, mean) at once?
        38. How to merge two DataFrames horizontally (inner join)?
        39. How to perform a left join with Pandas?
        40. How to perform an outer join with Pandas?
        41. How to concatenate two DataFrames vertically?
        42. How to concatenate two DataFrames horizontally?
        43. What is axis=0 vs axis=1?
        44. What is broadcasting in Pandas?
        45. How to pivot a table?
        46. How to create a pivot table with multiple aggregation functions?
        47. Difference between .pivot() and .melt()?
        48. How to melt a DataFrame into a long format?
        49. What are MultiIndexes in Pandas?
        50. How to sort a MultiIndexed DataFrame?
        51. How to stack and unstack a DataFrame?
        52. How to sample random rows from a DataFrame?
        53. How to shuffle a DataFrame randomly?
        54. How to create dummy variables from a categorical column?
        55. How to detect and handle outliers in a DataFrame?
        56. How to use .query() to filter rows?
        57. How to use .eval() to compute expressions?
        58. How to convert a column to datetime?
        59. How to extract the year, month, and day from a datetime column?
        60. How to filter data for a specific date range?
        61. How to perform cumulative sum on a column?
        62. How to perform rolling averages?
        63. How to forward-fill missing data?
        64. How to backward-fill missing data?
        65. How to interpolate missing values?
        66. How to rank entries in a DataFrame?
        67. What is chaining indexing? Why should it be avoided?
        68. How to optimize memory usage when loading big datasets?
        69. How to use Categorical datatypes to save memory?
        70. How to read only selected columns from a CSV?

        ## Advance Level Questions ##
            71. How to chunk a large CSV file while reading it?

            72. How to process large datasets without loading them fully into memory?

            73. What is vectorization in Pandas and why is it important?

            74. How to use .transform() in a groupby operation?

            75. Difference between .apply() and .transform() after groupby?

            76. How to write custom aggregation functions for groupby?

            77. How does .rolling() work in Pandas?

            78. How to apply expanding window calculations?

            79. What is window function and how is it useful?

            80. How to create lag features for time series data?

            81. How to calculate moving average with Pandas?

            82. How to shift a column up or down by N periods?

            83. How to join datasets on multiple columns?

            84. How to merge datasets with different column names?

            85. How to use .merge_asof() for time-aligned joins?

            86. How to perform cross join (cartesian product) in Pandas?

            87. How to chain multiple operations using method chaining?

            88. How to create a custom accessor for a DataFrame?

            89. How to serialize a DataFrame to JSON?

            90. How to save and load a DataFrame using Pickle?

            91. How does Pandas handle NaN values internally?

            92. How to deal with inconsistent column names (e.g., trailing spaces)?

            93. How to detect text encoding issues while reading files?

            94. What is memory_map option while reading CSV?

            95. What are extension arrays in Pandas? Example?

            96. How to parallelize a Pandas operation?

            97. Difference between Pandas and Dask?

            98. When would you prefer Dask over Pandas?

            99. How would you design a data pipeline using Pandas?

            100. What are some best practices for working with large datasets in Pandas?


        ##  Summary ##
        30 Beginner (basic usage, indexing, cleaning)
        40 Intermediate (joins, pivots, missing data handling, optimization)
        30 Advanced (performance, real-world problems, design concepts)


# Scenario Based Questions #

    ### Beginner Level ###

        1. You have a dataset with missing values in multiple columns. How will you fill missing numeric values with the column mean and categorical values with the mode?

        2. You are given a column of strings with mixed cases. How would you standardize them to lowercase?

        3. Your DataFrame contains duplicate rows. How will you drop only the exact duplicates but keep the first occurrence?

        4. How would you select rows where column 'Age' is between 20 and 30?

        5. A column contains price values like "$400", "$250". How would you convert them into integers?

        6. You want to sort a DataFrame by two columns: 'Country' ascending and 'Sales' descending. How?

        7. If a DataFrame has an index with gaps (e.g., 0, 2, 4), how would you reset it back to 0, 1, 2, ...?

        8. A column contains dates in string format. How do you convert it to datetime objects?

        9. How would you filter all rows where the 'Name' column starts with "A"?

        10. You want to select all rows where a column has NULL values. How?

        11. You want to create a new column 'Revenue' by multiplying 'Quantity' and 'Price'. How?

        12. How would you count how many times each unique value appears in a column?

        13. You are given two DataFrames. How would you perform an inner join on a common column?

        14. You have a huge DataFrame. How would you view just the column types and memory usage?

        15. How would you remove rows where 'Salary' is less than 10000?

        16. How to randomly sample 5% of the rows of a DataFrame?

        17. You have a column 'Category' with 50 unique values. How would you find the top 5 most frequent ones?

        18. A DataFrame has column names with spaces. How would you rename them with underscores instead?

        19. Given a datetime column, how would you extract only the month?

        20. How would you change negative values in a column to 0?

        21. A DataFrame has duplicate column names. How would you identify and fix it?

        22. You are given a column of emails. How would you extract only the domain (e.g., gmail.com)?

        23. How would you create a pivot table showing average 'Sales' for each 'Region'?

        24. How to find correlation between numeric columns of a DataFrame?

        25. You want to apply a custom function only to one column. How?

        26. How would you detect outliers using Z-score method?

        27. You want to concatenate two DataFrames vertically. How?

        28. How would you forward-fill missing values only for specific columns?

        29. You want to calculate a cumulative sum for a 'Sales' column. How?

        30. You want to add a new row to a DataFrame. How?

    ### Intermediate Level ###

        31. How would you detect which columns have more than 30% missing values?

        32. You need to merge two datasets where one has duplicate keys. Which join will you use?

        33. You have a DataFrame with dates. How would you find all rows in the last 7 days?

        34. A DataFrame contains text with unwanted leading/trailing spaces. How would you clean it?

        35. You want to group data by 'Region' and 'Category' and find the total sales. How?

        36. How to replace all occurrences of a string "N/A" with np.nan?

        37. You need to filter rows based on a complex condition involving multiple columns. How?

        38. How to split a column 'Name' into 'First Name' and 'Last Name'?

        39. You are asked to find the day of the week for each transaction date. How?

        40. How would you detect duplicated values based on specific columns only (not all)?

        41. You need to create dummy variables from a categorical feature. How?

        42. How to optimize DataFrame size when loading 100 million rows?

        43. You have a JSON file with nested objects. How would you read it into a flat DataFrame?

        44. You want to create a lag feature by shifting 'Sales' by 1 day. How?

        45. You are given two DataFrames with the same columns. How to concatenate them while keeping only unique rows?

        46. You need to generate a summary report showing mean, median, min, max for all columns. How?

        47. How would you select all numeric columns only?

        48. How would you select all columns that have object (string) datatype?

        49. A dataset has some corrupted rows that have too many NULLs. How would you find and drop them?

        50. You want to bucket 'Age' into groups (e.g., 0-18, 19-35, etc.). How?

        51. How would you create a rolling average of the last 7 rows?

        52. You want to extract text between parentheses in a column. How?

        53. Given a DataFrame, how would you find which columns are completely empty?

        54. How to find the most common value in each column?

        55. How would you export a DataFrame to an Excel file with multiple sheets?

        56. You have a dataset with typos like "Fmale" instead of "Female". How would you fix it?

        57. How to create a new column that shows 'High' if Sales > 10000 and 'Low' otherwise?

        58. How would you remove rows where two specific columns are both NULL?

        59. You want to pivot data where columns are values of 'Category' and entries are counts. How?

        60. How would you append a row without using .append() (which is deprecated)?

        61. How would you perform a groupby but keep the same shape as original (broadcasted result)?

        62. You want to assign a sequential ID within each group of a GroupBy object. How?

        63. How would you calculate the difference between consecutive rows?

        64. How to rank customers based on their total purchases?

        65. How would you find which columns have a constant value?

        66. How would you calculate the percentage of missing values per column?

        67. You need to replace extreme outliers with the 95th percentile. How?

        68. How would you calculate year-over-year growth rates?

        69. How would you transpose a huge DataFrame efficiently?

        70. You want to save a DataFrame to Parquet format instead of CSV. Why and how?

    ### Advance Level Questions ###

        71. You have two time series datasets that need to be joined based on nearest timestamps. How?

        72. You want to create an expanding sum instead of rolling. How?

        73. How to filter rows where a string column contains a specific pattern using regex?

        74. You need to optimize a DataFrame to consume 70% less memory. What steps?

        75. How would you map multiple values to a single value using dictionary mapping?

        76. How would you efficiently filter a dataset with millions of rows based on a list of values?

        77. How would you fill missing values with the median grouped by another column?

        78. How would you remove special characters from every string column in the DataFrame?

        79. You want to create a DataFrame from multiple smaller CSV files in a folder. How?

        80. How to unpivot a table where multiple columns are actually value categories?

        81. How to count number of times each customer made a purchase month over month?

        82. You have a multi-index DataFrame. How would you flatten it back to normal?

        83. You want to explode a list inside a column to multiple rows. How?

        84. How would you detect and handle skewed distributions in a feature?

        85. How would you split a DataFrame into train-test datasets without scikit-learn?

        86. How to find the second-highest salary per department using Pandas?

        87. How to handle text columns with mixed languages or encodings?

        88. How would you use .agg() to apply different functions to different columns?

        89. How would you reverse the order of rows in a DataFrame?

        90. How would you normalize numeric columns to a 0-1 range?

        91. You have a huge dataset but only want to calculate group-level aggregates without loading full data. How?

        92. How to use memory mapping to load huge CSV faster?

        93. How would you convert hierarchical JSON to flat columns while reading it?

        94. How to parallelize .apply() using swifter or Dask?

        95. How to cache intermediate results to avoid repeated heavy computations?

        96. You want to create a custom Pandas accessor @pd.api.extensions.register_dataframe_accessor. How?

        97. You need to build an ETL pipeline with Pandas transformations. How would you structure it?

        98. How to serialize a DataFrame into a compressed format for faster reading later?

        99. How to handle dirty datetime formats like "2024-04-05" and "5/4/2024" together?

        100. You are asked to profile and benchmark Pandas code performance. What tools and how?


    ## Summary ##
        30 Basic (Common real-world tasks)
        40 Intermediate (Groupby, joins, missing data, memory optimization)
        30 Advanced (Big data handling, time series, ETL patterns)




