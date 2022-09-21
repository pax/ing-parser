import time, sys, os
import pandas as pd

infile = 'data/ING Curent RO83INGB0000999903963904 01.01.2019-31.12.2020 Tranzactii_11-05-2022_15-47-35.xlsx'
outfile = 'data/sample2.csv'

df = pd.read_excel(infile)
df.to_csv(outfile)
print("done")

