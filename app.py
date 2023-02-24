import streamlit as st

#use of all of the width of the screen (standard would center the content)
#emojis cheat sheet : https://www.webfx.com/tools/emoji-cheat-sheet/


st.set_page_config(page_title = "E124BG's Webpage", page_icon = ":tophat:", layout = "wide")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Eliott :wave:")
st.subheader("A Master in Computer Science student from Uni Lu :flag-lu:")

st.write("I am passionate about software engineering, optimization and the applications of AI.")
st.write(
    """
    Some of my current projects :  
    - Deus ex Machina, an AI and ART project http://deus-x-machina.org/
    - Rust by the book, a collection of short rust programs to learn rust step by step https://github.com/E124BG/rust-by-the-book
    - A study of chatgpt and its usage in Luxembourg (link yet to come)
    """)
st.write("Contacts : [Linkedin](www.linkedin.com/in/eliott-bonte-534a76207)")

# LottieFile is an animation that scales without any pixelization

