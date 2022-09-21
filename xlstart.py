import time, sys, os
import pandas as pd
df = pd.read_excel('data/sample.xls')
df.to_csv('data/sample.csv')
print("done")

