import pandas as pd

#read file
file = pd.read_csv("../Data/vehicle_collisions.csv")
df = pd.DataFrame(file)
df.head()


#grab car numbers
df_car_involve = df[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
df_car_involve.head()


#delete null Borough rows
df_car_involve = df_car_involve[pd.notnull(df_car_involve['BOROUGH'])]
df_car_involve.head()



#count cars in an accident
df_car_involve['car_count'] = df_car_involve.apply(lambda x: x.count()-1, axis=1)
df_car_involve.head()


#grab index and columns of result
df_car_involve = df_car_involve.groupby(["BOROUGH","car_count"]).size().reset_index(name="number")
df_car_involve.head()


#reshape dataframe
df_car_involve = df_car_involve.pivot_table(index='BOROUGH', columns='car_count', values='number')
df_car_involve


#grap final result for csv file
df_car_involve['more'] = df_car_involve[0] + df_car_involve[4] + df_car_involve[5]
df_car_involve = df_car_involve[[1,2,3,'more']]
df_car_involve


df_car_involve.to_csv("Q1_Part_2.csv",header=["ONE_VEHICLE_INVOLVED","TWO_VEHICLES_INVOLVED","THREE_VEHICLES_INVOLVED","MORE_VEHICLES_INVOVLED"])
