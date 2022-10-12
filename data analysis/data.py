import pandas as pd 
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt 
import altair as alt


a = [ 1,2,3,4,5,6,7,8]
n = np.array(a)

nd=n.reshape((2,4))

dic= {
    'name':'Nuke',
    'age':23,
    'city':'pune',
}

data=pd.read_csv('athlete_events.csv')

## st.dataframe(data)



data2 = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

plt.scatter(data2['a'],data2['b'])
plt.title('Scatter')
st.pyplot()

st.line_chart(data2)

st.area_chart(data2)
st.bar_chart(data2)

