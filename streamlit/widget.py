import numpy as np
import pandas as pd
import streamlit as st

st.title('Simple Text Input')

name=st.text_input('Enter your name')

age=st.slider('Select your age :',0,100,25)

st.write(f"your age is {age}")


options=['pyhton','java','c++','javascript']
choice=st.selectbox('Choose your favourite language:',options)
st.write(f"You selected {choice}.")


if name:
    st.write(f'hello {name}')



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=1))


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option