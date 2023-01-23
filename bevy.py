import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
columns = ["Flow_ls", "Head_m"]
df = pd.read_csv("CSV.csv", usecols=columns)
print("contents in csv file:", df)
plt.plot(df.Flow_ls, df.Head_m)

# option = st.selectbox('Select pump model',(x1,x2,x3)) 

st.area_chart()
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
