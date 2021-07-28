import pandas as pd
import numpy as np
full_data = pd.read_excel("Data_Agregat_Covid19_Jakarta.xlsx",
                          sheet_name="Data Jakarta", usecols="A,K:M,O")
data_nakes = pd.read_excel("Data_Agregat_Covid19_Jakarta.xlsx",
                           sheet_name="Data Jakarta", usecols="K")
data_pos_day = pd.read_excel("Data_Agregat_Covid19_Jakarta.xlsx",
                             sheet_name="Data Jakarta", usecols="L")
data_pos_aktif = pd.read_excel("Data_Agregat_Covid19_Jakarta.xlsx",
                               sheet_name="Data Jakarta", usecols="M")
data_otg = pd.read_excel("Data_Agregat_Covid19_Jakarta.xlsx",
                         sheet_name="Data Jakarta", usecols="O")
print(full_data)

# problem case 1
# mean
print("\n Berikut hasil rata rata data : \n")
print(data_nakes.mean())
print(data_pos_day.mean())
print(data_pos_aktif.mean())
print(data_otg.mean())
# median
print("\n Berikut hasil data median : \n")
print(data_nakes.median())
print(data_pos_day.median())
print(data_pos_aktif.median())
print(data_otg.median())
# standar deviasi
print("\n Berikut hasil standar deviasi data : \n")
print(data_nakes.std())
print(data_pos_day.std())
print(data_pos_aktif.std())
print(data_otg.std())
# maximum value each column
print("\n Berikut hasil nilai data maximum  : \n")
print(data_nakes.max())
print(data_pos_day.max())
print(data_pos_aktif.max())
print(data_otg.max())
# minimum value each column
print("\n Berikut hasil nilai data minimum  : \n")
print(data_nakes.min())
print(data_pos_day.min())
print(data_pos_aktif.min())
print(data_otg.min())


print(full_data.describe())

# z value 95%
z_val = 2.96
outliers = []
# needed data
data_mean = [data_nakes["Tenaga Kesehatan Terinfeksi"].mean()]
data_std = [data_nakes["Tenaga Kesehatan Terinfeksi"].std()]
print(data_mean)

for y in data_mean:
    z_score = (y - data_mean)/data_std
    if np.abs(z_score) > z_val:
        outliers.append(y)
print(outliers)

# 2
data_mean = [data_nakes["Positif Harian"].mean()]
data_std = [data_nakes["Positif Harian"].std()]
print(data_mean)

for y in data_mean:
    z_score = (y - data_mean)/data_std
    if np.abs(z_score) > z_val:
        outliers.append(y)
print(outliers)
