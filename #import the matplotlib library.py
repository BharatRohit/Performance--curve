#import the matplotlib library
import pandas as pd
from matplotlib import pyplot as plt
columns = ["Flow_ls", "Head_m"]
df = pd.read_csv("CSV.csv", usecols=columns)
print("contents in csv file:", df)
plt.plot(df.Flow_ls, df.Head_m)
plt.show()