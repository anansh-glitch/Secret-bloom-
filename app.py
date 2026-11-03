
import streamlit as st

st.set_page_config(
    page_title="Secret Bloom",
    page_icon="🌸"
)

st.markdown("""
<style>

.stApp {
    background-image: url(
        "https://raw.githubusercontent.com/YOUR-USERNAME/secret-bloom/main/background.png"
    );
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

h1 {
    color: #B56583;
    text-align: center;
}

p {
    color: #806477;
}

.stButton button {
    background-color: #E8AFC3;
    color: white;
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 Secret Bloom")

st.write("### A little bouquet, a little secret 💗")

st.write(
    "Create a beautiful digital bouquet "
    "for your special one!"
)

name = st.text_input("Who is this bouquet for?")

if name:
    st.success(f"This bouquet is for {name} 🌷")
