import numpy as np
import pandas as pd
import streamlit as st


##tittle of app
st.title('Hello streamlit')

#dislay a simple text
st.write('This is a simple text')

#creating a simple data frame
df =pd.DataFrame({
    'ffirst column':[1,2,3,4,5],
    'second':[2,4,6,8,10]
})
#display the df
st.write("HEre is the dataframe")
st.write(df)


#create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)
