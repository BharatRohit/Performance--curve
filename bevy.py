import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('CSV.csv')
x = df['FLOW']
y = df['HEAD']

plt.plt(x,y)
plt.fill_between(x,y, color="lightblue", alpha=0.5)

plt.show()
