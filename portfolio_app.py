import streamlit as st
import pandas as pd
from pathlib import Path
import base64

st.set_page_config(page_title="My Portfolio", layout="wide")

DATA_PATH = Path("contact_messages.csv")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Resume", "Contact"])

if page == "Home":
    st.title("👋 Welcome to My Portfolio")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("profile.jpg", width=200)  

    with col2:
        st.subheader("Hi, I'm Raja Muhammad Arbab")
        st.markdown("""
        - 🎓 **IT Student** passionate about Python and building real-world applications.
        - 💻 Skilled in Python, Streamlit, OpenCV, NumPy, and Tkinter.
        - 🚀 Exploring AI, Automation, Machine Learning and Web App Development.
        """)

    st.markdown("---")
    st.markdown("### 🚀 Core Skills")
    st.markdown("""
    - **Languages**: Python, HTML, CSS
    - **Libraries/Tools**: NumPy, Pandas, OpenCV, Streamlit
    - **Frameworks**: Tkinter
    - **Tools**:GitHub, VS Code
    """)
    
    st.markdown("---")
    st.markdown("## 🎖️ Certificates & Testimonials")

    certificates = [
    {
        "title": "Advanced Python Programming",
        "issuer": "NAVTTC",
        "year": "2024",
        "desc": "Completed a certified Python course covering OOP, GUI, and more."
    },
   
]

    for cert in certificates:
        with st.container():
            st.markdown(f"### 🏅 {cert['title']}")
            st.markdown(f"**Issuer**: {cert['issuer']} ({cert['year']})")
            st.markdown(cert["desc"])
            st.markdown("---")

    st.markdown("## 🌐 Connect with Me")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin)](https://linkedin.com/in/raja-muhammad-arbab-91a062372/)")

    with col2:
        st.markdown("[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github)](https://github.com/RajaMuhammadArbab)")

    with col3:
        st.markdown( "[![X](https://img.shields.io/badge/-X-000000?logo=twitter)](https://x.com/@arbab_thakur)")

    

elif page == "Projects":
    st.title("📁 Projects")
    project_data = [
        {
            "title": "AI Resume Screening System",
            "desc": "An AI-based Resume Screening System that ranks resumes based on their relevance to a job description using NLP techniques like TF-IDF and BERT. Helps automate candidate shortlisting for recruiters with a simple and effective Python-based interface..",
            "tech": "Python, Streamlit, scikit-learn",
            "github": "https://github.com/RajaMuhammadArbab/Ai_based_Resume_Screening_System",
            
        },
        {
            "title": "Attendance Management System",
            "desc": "A smart Attendance Management System for universities with face recognition, fingerprint, and QR code support. Includes separate apps for students and teachers, real-time stats, offline mode, and secure role-based access. Built with Python and biometric/NLP tools.",
            "tech": "OpenCV, Tkinter, SQLite",
            "github": "https://github.com/RajaMuhammadArbab/Attendance_managment_system",
            
        },
        {
            "title": "2D Maze Game ",
            "desc": "A Python-based 2D Maze Game with randomly generated mazes, player navigation, and goal detection. Features obstacles, unique session IDs, and an interactive UI. Designed for logic building, fun gameplay, and educational purposes.",
            "tech": "Python, Pygame, Random, DFS Algorithm",
            "github": "https://github.com/RajaMuhammadArbab/2D_Maze_Game",
            
        },
        {
            "title": "Temperature Converter ",
            "desc": "A simple Python-based Temperature Converter that allows users to convert between Celsius, Fahrenheit, and Kelvin. Features a user-friendly interface built with Tkinter, making it easy to perform quick and accurate temperature ",           
            "tech": "Python, Conditional Logic, Arithmetic",
            "github": "https://github.com/RajaMuhammadArbab/Temperature_converter",
        },    
        {
            "title": "Sudoku gui game",
            "desc": "A Python-based Sudoku Solver with a graphical user interface. Users can input puzzles manually or load them from files, and the system solves them instantly using a backtracking algorithm. Built with Tkinter for an interactive and user-friendly experience.",
            "tech": "Python, Tkinter, NumPy, Backtracking Algorithm",
            "github": "https://github.com/RajaMuhammadArbab/Sudoku_gui_game",
        },  
        {
          "title":"Currency_Converter_Project",
          "desc":"A real-time Currency Converter built with Python and Tkinter. Fetches live exchange rates and allows users to convert between various global currencies instantly through a clean and interactive GUI. Useful for travelers, businesses, and finance enthusiasts",
          "tech":"Python, Tkinter, Requests (for API), Exchange Rate API",
          "github":"https://github.com/RajaMuhammadArbab/Currency_Converter_Project", 
                    
        }, 
        {
          "title":"Emotion Music Player",
          "desc":"An AI-powered music player that detects user emotions using facial expressions and plays songs to match the mood. Combines OpenCV, deep learning, and a music library for a personalized listening experience. Built with Python and emotion recognition models.",
          "tech":"Python, OpenCV, Deep Learning (CNN), Tkinter, Emotion Recognition, Pygame (for audio)",
          "github":"https://github.com/RajaMuhammadArbab/Raja-emotion_music_player", 
                    
        },
        {
          "title":"Guess Number Game",
          "desc":"A fun and interactive Python game where players try to guess a randomly generated number within a limited range. Features difficulty levels, score tracking, and a leaderboard system. Great for beginners to learn logic, loops, and user input handling",
          "tech":"Python, Random, File I/O, Conditional Logic, Loops, CLI",
          "github":"https://github.com/RajaMuhammadArbab/Guess_number_game", 
                    
        }, 
        {
          "title":"File Organizer",
          "desc":"A Python-based File Organizer with a user-friendly GUI that automatically sorts and moves files into folders based on type, extension, or custom rules. Built using Tkinter for easy desktop use, helping users keep their directories clean and organized.",
          "tech":"Python, Tkinter, OS Module, Shutil Module, File Handling",
          "github":"https://github.com/RajaMuhammadArbab/file_organizer_gui", 
                    
        }, 
        {
          "title":"Dictionary App",
          "desc":"A Python-powered Dictionary App that allows users to search word meanings, synonyms, antonyms, and pronunciations. Features a clean GUI built with Tkinter and fetches definitions using an online API for real-time results. Useful for students and language learners",
          "tech":"Python, Tkinter, Requests, Dictionary API, JSON",
          "github":"https://github.com/RajaMuhammadArbab/DictionaryApp", 
                    
        }, 
        {
          "title":"Contact Manager",
          "desc":"A Python-based Contact Manager with a user-friendly GUI to add, search, update, and delete contact details. Built using Tkinter and SQLite for smooth data storage and management. Ideal for organizing personal or professional contact lists efficiently",
          "tech":"Python, Tkinter, SQLite, SQL, GUI Design",
          "github":"https://github.com/RajaMuhammadArbab/Contact_manager", 
                    
        }, 
        {
          "title":"English Urdu Dictionary",
          "desc":"A bilingual English-Urdu Dictionary app built with Python and Tkinter. Allows users to search words and get accurate Urdu translations and meanings. Ideal for students, translators, and language learners seeking quick and easy vocabulary assistance",
          "tech":"Python, Tkinter, SQLite, Urdu Translation Dataset, GUI Design",
          "github":"https://github.com/RajaMuhammadArbab/English-Urdu-Dictionary", 
                    
        }
    ]

    for p in project_data:
        with st.container():
            cols = st.columns([5, 3])
            with cols[0]:
                st.subheader(p["title"])
                st.write(p["desc"])
                st.markdown(f"**Tech Used**: {p['tech']}")
                st.markdown(f"[GitHub]({p['github']})")
        st.markdown("---")


elif page == "Resume":
    st.title("📄 My Resume")
    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
        st.download_button(label="📥 Download Resume",
                           data=PDFbyte,
                           file_name="resume.pdf",
                           mime='application/octet-stream')

    st.markdown("---")
    st.markdown("### 📑 Resume Preview")
    resume_viewer = '''
    <iframe src="resume.pdf" width="100%" height="600px" type="application/pdf"></iframe>
    '''
    st.markdown(resume_viewer, unsafe_allow_html=True)

       


elif page == "Contact":
    st.title("📬 Contact Me")
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")

        if submit:
            msg_data = pd.DataFrame([[name, email, message]], columns=["Name", "Email", "Message"])
            if DATA_PATH.exists():
                old_data = pd.read_csv(DATA_PATH)
                msg_data = pd.concat([old_data, msg_data], ignore_index=True)
            msg_data.to_csv(DATA_PATH, index=False)
            st.success("✅ Thank you! Your message has been received.")


