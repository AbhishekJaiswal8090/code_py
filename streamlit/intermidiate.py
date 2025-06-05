import streamlit as st

st.title('Abhishek Project')

if st.button('Select'):
    pass

add_cont=st.checkbox('Add content')
if add_cont:
    st.write('content added to the book')

tea_type= st.radio('Pick your book base:',['About Author', 'Chapters','Summary','Conclusion','Final view'])    
st.write(f"Selected base {tea_type}")

type_of=st.selectbox("Choose Type of book:",['Love','War','Pysychology'])
st.write(f"Your selected kind of book is {type_of}")


level_of=st.slider('Ratings',0 ,5,2)
st.write(f"Your rating is {level_of}")

num_books=st.number_input('How much books',min_value=1, max_value=10,step=1)
st.write(f'Your input is {num_books}')


name=st.text_input("Enter your name")
if name:
    st.write(f'welcome {name} your book is on way')

dob=st.date_input("Select your date of birth")
st.write(f"Your dob is {dob}")