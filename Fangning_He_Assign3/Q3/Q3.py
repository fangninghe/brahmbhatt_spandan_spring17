import pandas as pd

#read file
file = pd.read_csv("Data/cricket_matches.csv")
df = pd.DataFrame(file)
df.head()

#select key columns
df_winner = df[['winner','home','innings1','innings1_runs','innings2','innings2_runs']]
df_winner.head()


#select winners and host
df_winner = df_winner.loc[df_winner['winner'] == df_winner['home']]
df_winner.head()

#group winners by home
df_winner = df_winner.groupby('home')

#calculate the sum score winning in innings1
df_innings1 = pd.DataFrame(df_winner.apply(lambda x: x[x['winner'] == x['innings1']]['innings1_runs'].sum()))
df_innings1.head()


#calculate the sum score winning in innings1
df_innings2 = pd.DataFrame(df_winner.apply(lambda x: x[x['winner'] == x['innings2']]['innings2_runs'].sum()))
df_innings2.head()

##calculate the total score winning in innings1
df_total = df_innings1.add(df_innings2, fill_value=0)
df_total.head()


#calulate the numbers of winning rounds of the winners
df_winner_round = df_winner.size().reset_index(name='Winnig_Round')
df_winner_round.head()

#merge two DataFrames
df_result = pd.merge(df_winner_round,df_total,left_on='home', right_index=True)
df_result.head()

#add result column
df_result['Score'] = df_result[0]/df_result['Winnig_Round']
df_result = df_result.sort_values('Score',ascending=False)
df_result.head()

#select final columns
df_result = df_result[['home','Score']]
df_result.head()

result.to_csv('output/Q3.csv',index=False)
