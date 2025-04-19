import streamlit as st

def clicked():
    st.write("The button was clicked")

st.write("## Hello World")
movie: str = st.text_input("What is your favourite movie: ")
st.write(f"Your favourite Movie is: {movie}")
is_clicked = st.button("Click Me", on_click=clicked)