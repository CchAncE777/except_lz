import pandas as pd

file_1 = 'var3.csv'
file_2 = 'var_stolb_3.csv'
file_pd_1= pd.read_csv(file_1)
file_pd_2 = pd.read_csv(file_2)
colums_1 = file_pd_1.columns
colums_2 = file_pd_2.columns
odinakovie_ctolbci = colums_1.intersection(colums_2)

print(odinakovie_ctolbci)

for colums in odinakovie_ctolbci:
    if file_pd_1[colums].dtype != file_pd_2[colums].dtype:
        print(f"Столбец '{colums}': df1={file_pd_1[colums].dtype}, df2={file_pd_2[colums].dtype}")


