# databaker_usage

## Why is databaker useful?
Databaker can easily read data from files like csv and xls where packages like pandas cannot.
Following this guide and the examples makes reading the data much easier than creating functions from scratch.
Using databaker avoids common mistakes that happen when manually converting data from an unreadable csv to readable.
We also want to discourage mnual steps, they are hard to tests, lead to human error and are not repeatable.

## When should you use databaker
Mention how this should not be a long term solution.
Ideally the data should be recieved in a readable manner.
This is a short term solution.
Use databker when the data cannot be directly read by packages like pandas.
Only use databaker to read the data and convert to a pandas dataframe.
Do not use databakers data cleaning features, best to stick with common packages like pandas.
Do not use databaker jupyter notebook features, we discourage jupyter notebooks for analysis.

## Examples
There are two examples provided in the example_uses folder.

## What Databaker functions are useful?
The useful_functions page highlights the key databaker functions.
You can also use the examples to see the suggested functions
