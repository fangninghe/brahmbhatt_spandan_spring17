import pandas as pd

#read data
file = pd.read_csv("Data/vehicle_collisions.csv")
df = pd.DataFrame(file)
df.head()


#convert to date format
df['DATE'] = pd.to_datetime(df['DATE'])
df.head()


#extract month from date
df['MONTH'] = df['DATE'].dt.month
df.head()
#pick up 2016 data
mark = (df['DATE'] >= '2016-01-01') & (df['DATE'] <= '2016-12-31')
df_2016 = df.loc[mark]
df_2016.head()


#caculate total accidents
df_2016_total = df_2016.groupby('MONTH').size().reset_index(name='NYC')
df_2016_total


#caculate car accidents in Manhattan
df_2016_MANHATTAN = df_2016.groupby(["MONTH", "BOROUGH"]).size().reset_index(name="MANHATTAN")
df_2016_MANHATTAN = df_2016_MANHATTAN.loc[df_2016_MANHATTAN['BOROUGH'] == 'MANHATTAN']
df_2016_MANHATTAN



#merge two dataframe and delete borough column
df_final = pd.merge(df_2016_MANHATTAN, df_2016_total, left_on='MONTH', right_on='MONTH')
df_final.drop('BOROUGH', axis=1, inplace=True)
df_final

#add percentage column
df_final['PENCENTAGE'] = df_final['MANHATTAN']/df_final['NYC']
df_final


#change month column
df_final['MONTH'] = ['Jan', 'Fen', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df_final

df_final.to_csv("output/Q1_Part_1.csv",index=False)
