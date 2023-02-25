import streamlit as st
import requests
from streamlit_lottie import st_lottie

# LottieFile is an animation that scales without any pixelization

lottie_cards_url = "https://assets6.lottiefiles.com/packages/lf20_LkyI64BhN0.json"

#use of all of the width of the screen (standard would center the content)
#emojis cheat sheet : https://www.webfx.com/tools/emoji-cheat-sheet/


st.set_page_config(page_title = "E124BG's Webpage", page_icon = ":tophat:", layout = "wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:# we get response code 200 in case of successful get
        return None
    return r.json()

# Use local CSS

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
            
            
# ---- LOAD ASSETS ----

lottie_animation = load_lottie_url(lottie_cards_url)
    

# ---- HEADER SECTION ----

with st.container():# a multi element container
    left_column, right_column = st.columns(2)# split into 2 columns
    with left_column:
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

    with right_column:
        st_lottie(lottie_animation, height= 300, key= "animation")
        
with st.container():#for contact service I use formsubmit https://formsubmit.co/
    st.write("---")
    st.header("Get In Touche With Me!")
    st.write("##")
    
    
    contact_form = """
    <form action="https://formsubmit.co/eliottbonte@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

# ---- HEROKU USAGE ---
# for hosting, heroku is used, see documentation : https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku/