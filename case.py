
import pandas as pd

df = pd.read_csv('StudentsPerformance .csv')
df.info()
mean_math = df['math score'].mean()
print(mean_math)