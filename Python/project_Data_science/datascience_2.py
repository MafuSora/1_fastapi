import pandas as pd

#input data
data = [1,2,3,4]
seriess = pd.Series(data)
print(seriess)
#data type
print(type(seriess))
#change index
seriess = pd.Series(data, index=['a','b','c','d'])
print(seriess)


#Dataframe
#Penggunan list
list = [1,2,3,4]
dflist = pd.DataFrame(list)
print(dflist)

#pengunaan dict
dict= {'value' : [100,200,300],'name' : ["james","money","johan"]}
dfdict = pd.DataFrame(dict)
print(dfdict)
#penggunaan series
seriesss = pd.Series([6,12],index = ['a','b'])
dfseriesss= pd.DataFrame(seriesss)
print(dfseriesss)
#numpy
import numpy as np
numpyarray = np.array([[5000,6000],['jonathan','joestaar']])
dfnumpay = pd.DataFrame({'nama': numpyarray[1],'gaji': numpyarray[0]},index = [1,2])
print (dfnumpay)

#data example
name = 'sukijan','sukiman','sukikan'
nilai = 80, 90 , 100
matkul = 'fister', 'mat teknik', 'rangkaian digital'

dfnilai = pd.DataFrame({'nama': name , 'nilai' : nilai, 'mata kuliah' : matkul})

name = 'sukijan','sukinanda','sukirman'
olahraga = 'gulat', 'sumo' , 'judo'
keahlian = 'fister', 'mat teknik', 'rangkaian digital'

dfkeahlian = pd.DataFrame({'nama': name , 'hobi' : olahraga, 'mata kuliah' : matkul})
#merge bberarti untuk menyatukan berdasarkan ..PERSAMAAN DATA!!!!
#inner untuk data yang
print(dfnilai.merge(dfkeahlian,on='nama' , how='inner'))
print(dfnilai.merge(dfkeahlian))
print(dfnilai.merge(dfkeahlian,on='mata kuliah' , how='inner'))
#outter
print(dfnilai.merge(dfkeahlian,on='nama' , how='outer'))
print(dfnilai.merge(dfkeahlian,on='mata kuliah' , how='outer'))

