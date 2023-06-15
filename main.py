from pathlib import Path

import streamlit as st 
from PIL import Image


# ------PATH SETTINGS -----------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / 'assests'/'Felix Kuria Resume.pdf'
profile_pic = current_dir / 'assests'/'profile-pic.png'
css_file = current_dir / 'styles'/'main.css'


# --------- GENERAL SETTINGS ---------

PAGE_TITLE = 'Digital CV | Felix Kuria'
NAME = 'Felix Kuria'
PAGE_ICON = ":wave:"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = 'felixkuria12@gmail.com'

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/felix-kuria/",
    "GitHub": "https://github.com/kush2022",
    "WhatsApp": "+254710702286"
}

PROJECTS = {

}


# -------Code---

st.set_page_config(
    page_icon=PAGE_ICON,
    page_title=PAGE_TITLE,
    layout='centered'
)


# ----- LOADING CSS --- 

def load_css(file_path):
    with open(file_path) as f:
        css = f.read()
        return f"<style>{css}</style>"
css = load_css(css_file)
st.markdown(css, unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#----- HERO SECTION ----------
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=200)


with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(":email:", EMAIL)


# ------- SOCIAL LINKS -------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (plaform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{plaform}]({link})")


# ----EXPERIENCE & QUALIFICATIONS--------
st.empty()
st.subheader('Experience & Qualification')
st.write(
    """
    - Designed and developed scalable and efficient software solutions using programming languages such as Python, Java, and C++.
    - Integrated software applications with external systems and APIs to enhance functionality and data exchange.
    - Presented findings and recommendations to stakeholders and provided data-driven insights for process improvements.
    - Collaborated with cross-functional teams to define key performance indicators (KPIs) and create dashboards for monitoring business metrics.
    """
)

# ---SKILLS ----------
st.empty()
st.subheader("Hard Skills")
st.write(
    """
    - Data analysis and interpretation
    - Data visualization
    - SQL and database management
    - Data cleansing and preprocessing
    - Software development methodologies (Agile, Scrum)
    - Web development frameworks (e.g., Django, Flask)

    """
)


# -----WORK HISTORY ---------
st.empty()
st.subheader("Work Experience")
st.divider()

# job1
st.write("Back-end Developer | **BlackBox Flight Data Limited**")
st.write("2022-2023")
st.write(
    """
- ● Collaborated with a team to create a web application with the use
of the Django framework
- ● My responsibilities included working on the database design and
implementation using both SQL and NoSQL databases
- ● In order to maintain version control and work alongside my
teammates, I utilized Git
- ● Additionally, I actively participated in code reviews and testing to
guarantee the application's high quality.
- ● Managed efficient SQL queries and data transport.
- ● Troubleshooted and tested software and debugged to clean up code
and improve efficiency.
    """
)

# job2
st.empty()
st.divider()
st.write("Teaching Assistance | **St.Joseph's High School**")
st.write("2018-2019")
st.write(
    """
- ● Tutored struggling students individually and in small groups to
reinforce learning concepts.
- ● Supported classroom activities, tutoring, and reviewing work.
- ● Assisted teachers with classroom management and document
coordination to maintain a positive learning environment.
    """
)

