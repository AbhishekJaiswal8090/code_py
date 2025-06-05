import streamlit as st

st.title('Hello Brotha')
st.subheader('Abhishek')
st.text('Welcome to your first interactive app')
st.write('Choose your favourite of chai')

#It is a slider
books=st.selectbox('Your fav book',['Rich dad poor dad','Atomic habbits','48 Powerful laws','Ikigai'])

st.write(f"You choose {books} as your favourite book")

st.success(f'Your Book has been selected {books}')