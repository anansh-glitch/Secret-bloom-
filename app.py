import streamlit as st

st.set_page_config(
    page_title="Secret Bloom",
    page_icon="🌸"
)

st.title("Secret Bloom 🌸")
st.write("A little bouquet, a little secret.")

st.subheader("Welcome to Secret Bloom 💗")

st.write("Create a beautiful digital bouquet for someone special!")

name = st.text_input("Who is this bouquet for?")

if name:
    st.write("This bouquet is made with love for", name, "🌷")
