import pandas as pd
#read file
file = pd.read_csv("Data/employee_compensation.csv")
df = pd.DataFrame(file)
df.head()


#filter Calendar data
df_calendar = df.loc[df['Year Type'] == 'Calendar']
df_calendar.head()

#select key columns
df_mean = df_calendar[['Job Family','Employee Identifier','Salaries','Overtime','Total Benefits','Total Compensation']]
df_mean = df_mean.groupby(['Job Family','Employee Identifier']).mean()
df_mean.head()

#select employee overtime is greater than 5% of the Salaries
df_mean = df_mean.loc[df_mean['Overtime'] > (df_mean['Salaries']*0.05)]
df_mean.head()

#group by job Family
df_mean = df_mean.groupby(level=[0]).mean()
df_mean.head()

#caculate Percent_Total_Benefit and sort
df_mean['Percent_Total_Benefit'] = df_mean['Total Benefits']/df_mean['Total Compensation']*100
df_mean = df_mean.sort_values('Percent_Total_Benefit',ascending=False)
df_mean.head()

#select key columns
df_benefit_compensation = df_mean[['Total Benefits','Total Compensation','Percent_Total_Benefit']]
df_benefit_compensation.head()


df_benefit_compensation.to_csv('output/Q2_Part_2.csv')
