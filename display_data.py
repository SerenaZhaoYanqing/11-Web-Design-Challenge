import pandas as pd

#reading csv of our raw data 
df=pd.read_csv('Resources/Display Data.csv')

#converting file into html
data_table=df.to_html('data_source.html')
print(data_table)

