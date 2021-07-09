import pandas as pd
"""
#input data
data = [1,2,3,4]
series1 = pd.Series(data)
print(series1)

#change index series object
type (series1)
series2=pd.Series(data,index=['a','b','c','d'])
print(series2)

#create dataframe
data = [1,2,3,4,5]
df=pd.DataFrame(data)
print(df)

#create dataframe with dictionary
"""
diction = {'fruits': ['apples', 'banana', 'mangoes'], 'count': [10, 20, 15]}
df1 = pd.DataFrame(diction)
print(df1)

"""
series3=pd.Series([6,12],index=['a','b'])
df2=pd.DataFrame(series3)
print(df2)


# numpy df
import numpy as np
numpyarray = np.array([[50000,60000],['john','james']])
df4= pd.DataFrame({'name':numpyarray[1],'salary':numpyarray[0]})
print(df4)

#merge join
    #data1
player =['player1','player2','player3']
point=[8,9,6]
title=['game1','game2','game3']
df5=pd.DataFrame({'player':player,'point':point,'title':title})
print(df5)
    #data2
player2 =['player1','player5','player6']
power2=['punch','kick','elbow']
title2=['game1','game5','game6']
df6=pd.DataFrame({'player':player2,'power':power2,'title':title2})
print(df6)

#inner merge
    #menyatukan yang sama saja parameter akn ada 2 tergantung on (on hanya akan ada 1 yang merupakan dicari samanya)dan
df5.merge(df6,on='title',how ='inner')
    #DEFAULT INNER akan dicari sama nya dan otomatis cmn 1 on nya

df5.merge(df6)


#left merge
    #yang di kiri disatukan sama kanan utama yang kiri  jadi yang kanan kosong
df5.merge(df6,on='player',how ='left')

#right merge
    #yang di kanan disatukan sama kiri utama yang kiri jadi yang kiri akan banya kosong
df5.merge(df6,on='player',how ='right')

#outer merge
    #yang tidaksama lawan inner
df5.merge(df6,on='player',how ='outer')
"""
# join
player3 = ['player1', 'player5', 'player6']
power3 = ['punch', 'kick', 'elbow']
title3 = ['game1', 'game5', 'game6']
df7 = pd.DataFrame({'player': player3, 'power': power3,
                    'title': title3}, index=['l1', 'l2', 'l3'])
print(df7)

player3 = ['player1', 'player5', 'player6']
power3 = ['punch', 'kick', 'elbow']
title3 = ['game1', 'game5', 'game6']
df8 = pd.DataFrame({'player': player3, 'power': power3,
                    'title': title3}, index=['l2', 'l3', 'l4'])
print(df8)

# inner join>yang sama aja
df7.join(df8, how='inner')

# left join>reference left
df7.join(df8, how='left')
# right join >reference right
df7.join(df8, how='right')
# outer join>all
df7.join(df8, how='inner')


# concatinate

pd.concat(df7, df8)


# importing dataset
"""
cars=pd.read_csv("bala")
print(cars)

#check the type
typpe(cars)
#check first  5 
cars.head()

#check data sesuai x pertama
cars.head(x)

#check data sesuai x terakhir
cars.tail(x)

#check bentuk dari df aka dimensi

cars.shape

#summary of data on cmputer desc
cars.info(null_counts=True)

#mean
cars.mean()
#standar deviasi
cars.std()

#maximum value each column
cars.max()
#minimum value each column
cars.min()
#count value each column (null not counted)
cars.count()
#descriptive statistics summary such max min std etc. (in percentage data)
cars.describe()


#cleaning data
    #rename column
cars=cars.rename(columns={"Unnamed: 1":"model"})
print(cars)
    #fill null on (qsec) by(fillna) with value of (mean)
cars.qsec=cars.qsec.fillna(cars.qsec.mean())
print(cars)
    #drop unwanted column (columns=[column name]) hapus kolom ke bawah
    
cars = cars.drop(columns=['S.No'])
print(cars)

    #correlation matrix on angka  parameter nya column
df10=cars[['mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].corr()
print(df10)









"""
