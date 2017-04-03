import pandas as pd

#read file
file = pd.read_csv("Data/movies_awards.csv")
df = pd.DataFrame(file)
df.head()

#select key columns
df_awards = df[['Title','Awards']]
df_awards.head()

#delete now awards columns
df_awards = df_awards[pd.notnull(df_awards['Awards'])]
df_awards.head()

#select other columns
name_won_l = []
name_nominated_l = []

for row in df_awards['Awards']:
    regex1 = re.search(r'Won (\d+) (.*?)\.',row)
    regex2 = re.search(r'Nominated for (\d+) (.*?)\.',row)
    name_won = ''
    name_nominated = ''
    if regex1:
        name_won = regex1.group(2) + '_won'
        name_won_l.append(name_won)
    if regex2:
        name_nominated = regex2.group(2) + '_nominated'
        name_nominated_l.append(name_nominated)

print(set(name_won_l))
print(set(name_nominated_l))

#complete dataframe
col_list = ['Awards_won','Awards_nominatied','Golden Globe_won','Golden Globe_nominated','BAFTA Film Award_nominated','Oscar_nominated','Oscar_won','Primetime Emmy_nominated','Primetime Emmy_won']
df_awards_result = pd.concat([df_awards,pd.DataFrame(columns=col_list)]).fillna(0)
df_awards_result.head()
#give reasonable order to columns
df_awards_result = df_awards_result[['Title','Awards','Awards_won','Awards_nominatied','Oscar_nominated','Oscar_won','Golden Globe_won','Golden Globe_nominated','Primetime Emmy_nominated','Primetime Emmy_won','BAFTA Film Award_nominated']]
df_awards_result.head()
#reindex
df_awards_result = df_awards_result.reset_index(drop=True)
df_awards_result.head()

#add value to dataframe
a = 0
for row in df_awards['Awards']:
    regex1 = re.search(r'(\d+) win',row)
    regex2 = re.search(r'(\d+) nomination',row)
    regex3 = re.search(r'Won (\d+) (.*?)\.',row)
    regex4 = re.search(r'Nominated for (\d+) (.*?)\.',row)
    if regex1:
        df_awards_result.set_value(a, 'Awards_won', regex1.group(1))
    if regex2:
        df_awards_result.set_value(a, 'Awards_nominatied', regex2.group(1))
    if regex3:
        if 'Golden Globe' in regex3.group(2):
            df_awards_result.set_value(a, 'Golden Globe_won', regex3.group(1))
        if 'Oscar' in regex3.group(2):
            df_awards_result.set_value(a, 'Oscar_won', regex3.group(1))
        if 'Primetime Emmy' in regex3.group(2):
            df_awards_result.set_value(a, 'Primetime Emmy_won', regex3.group(1))
    if regex4:
        if 'Golden Globe' in regex4.group(2):
            df_awards_result.set_value(a, 'Golden Globe_nominated', regex4.group(1))
        if 'Oscar' in regex4.group(2):
            df_awards_result.set_value(a, 'Oscar_nominated', regex4.group(1))
        if 'Primetime Emmy' in regex4.group(2):
            df_awards_result.set_value(a, 'Primetime Emmy_nominated', regex4.group(1))
        if 'BAFTA Film Award' in regex4.group(2):
            df_awards_result.set_value(a, 'BAFTA Film Award_nominated', regex4.group(1))
    a = a + 1

df_awards_result.head()

#sum Awards_won and Awards_nomination
df_awards_result['Awards_won'] = df_awards_result['Awards_won'] + df_awards_result['Golden Globe_won'] + df_awards_result['Oscar_won'] + df_awards_result['Primetime Emmy_won']
df_awards_result['Awards_nominatied'] = df_awards_result['Awards_nominatied'] + df_awards_result['Golden Globe_nominated'] + df_awards_result['Oscar_nominated'] + df_awards_result['Primetime Emmy_nominated'] + df_awards_result['BAFTA Film Award_nominated']

df_awards_result.head()

df_awards_result.to_csv('output/Q4.csv',index=False)
