# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# columns = ["Flow_ls", "Head_m"]
# df = pd.read_csv("CSV.csv", usecols=columns)
# print("contents in csv file:", df)
# plt.plot(df.Flow_ls, df.Head_m)
# plt.show()
import streamlit as st
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
