import pandas as pd

#read file
file = pd.read_csv("Data/employee_compensation.csv")
df = pd.DataFrame(file)
df.head()

#select the meaningful columns
df_compenstaion = df[['Organization Group','Department','Total Compensation']]
df_compenstaion.head()

#caculate the mean of total compensation
df_compenstaion = df_compenstaion.groupby(['Organization Group','Department']).mean()
df_compenstaion.head()


#sort by total compensation within groups
df_compenstaion = df_compenstaion['Total Compensation'].groupby(level=0, group_keys=False)
df_compenstaion = pd.DataFrame(df_compenstaion.nlargest(20))
df_compenstaion.head()

df_compenstaion.to_csv('output/Q2_Part_1.csv')
