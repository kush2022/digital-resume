import streamlit as st 
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests


# -----PATH SETTINGS----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic = current_dir /"assests"/"profile-pic.png"
css_file = current_dir / 'styles'/'style.css'
coding = "https://assets10.lottiefiles.com/packages/lf20_mXdqmT1SH2.json"
data_analysis = "https://assets5.lottiefiles.com/packages/lf20_49rdyysj.json"
email= "https://assets9.lottiefiles.com/packages/lf20_asqchqyq.json"
resume_file = current_dir/'assets'/'felix-resume.pdf'


# -------- PAGE CONFIG -------------

st.set_page_config(
    page_title="Felix Kuria",
    page_icon=":tada:",
    layout="wide"
)
# --------- LOADING ASSETS----------
@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

coding = load_lottieurl(coding)
data_analysis = load_lottieurl(data_analysis)
email = load_lottieurl(email)


# -----CSS FILE ------
@st.cache_data
def load_css(file_path):
    with open(file_path) as f:
        css = f.read()
        return f"<style>{css}</style>"
css = load_css(css_file)
st.markdown(css, unsafe_allow_html=True)

# -----RESUME DOWNLOAD ---
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()


# ----------VARIABLES
DESCRIPTION = """ 
Welcome to my portfolio! I am a highly skilled 
and versatile professional with a strong background in 
backend development and data analysis. With expertise in 
both fields, I bring a unique blend of technical prowess and 
analytical acumen to solve complex problems 
and drive impactful results.
"""

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/felix-kuria/",
    "GitHub": "https://github.com/kush2022",
    "WhatsApp": "https://wa.me/message/TOOBYKO2VINOH1",
}




#-------HERO SECTION -----
col1, col2 = st.columns((1,2), gap='small')
profile_pic = Image.open(profile_pic)
with col1:
    st.image(profile_pic, width=270)


with col2:
    st.subheader("Hi, I am Felix Kuria :wave:")
    st.markdown("## Back-end Developer | Data Analyst")
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(':email:', 'felixkuria12@gmail.com')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --------WHAT I DO ----------
with st.container():
    st.divider()

    left_column, right_column = st.columns(2, gap='small')
    with left_column:
        st.title("What I Do")
        st.markdown("#### *Back-end Development*")
        st.write(
            """
            - Design and develop scalable backend solutions using Python, Django, and FastAPI.
            - Create secure and efficient APIs to power web and mobile applications.
            - Optimize database performance, ensuring data integrity and high availability.
            - Implement authentication and authorization systems to protect sensitive data.
            - Collaborate with frontend developers to seamlessly integrate backend functionality.
            - Database design & management (PostgreSQL, MySQL, MongoDB)
            - DevOps (Docker, Slack, Git, GitHub)

            """
        )

        with right_column:
            st_lottie(coding, height=300)

with st.container():
    st.divider()

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("#### *Data Analysis*")
        st.write(
            """
            - Clean, transform, and analyze complex datasets to uncover valuable insights.
            - Apply statistical analysis techniques to identify patterns and trends.
            - Utilize machine learning algorithms for predictive modeling and decision-making.
            - Visualize data using charts, graphs, and interactive dashboards for effective communication.
            - Provide actionable recommendations based on data-driven insights.
            """
        )

    with right_column:
        st_lottie(data_analysis, height=250)



# ------- CONTACT FORM -----
with st.container():
    st.divider()
    st.header("Get In Touch With Me! ")
    st.empty()
    contact_form = """
    <form action="https://formsubmit.co/felixkuria12@gmail.com" method="POST">
     <input type="hidden" name="_capture" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here..." required></textarea>
     <button type="submit">Send</button>    
    </form>
    """
    left_column, right_column = st.columns(2)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with left_column:
        st_lottie(email, height=250)