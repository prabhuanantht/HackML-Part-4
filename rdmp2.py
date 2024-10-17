import streamlit as st
import ai
import printai1

st.title("Career Roadmap Generator")

if 'roadmap_content' not in st.session_state:
    st.session_state.roadmap_content = ""

dom = st.selectbox("Enter the domain: ", ["Computer Science", "Others"],None)

if dom == "Computer Science":
    roadmap = st.selectbox("Choose a roadmap", ["Front-End Developer", "Backend Developer", "Data Analyst", "AI and Data Scientist", "Machine Learning Engineer", "Python Developer", "Cloud Engineer", "Others"], None)

    if roadmap=="Others":
        printai1.other()

    elif(roadmap) :
        csv = ai.generate_ai_for_headings(roadmap)
        extract_csv = ai.extract_useful_content(csv)
        printai1.display_keywords_as_buttons(extract_csv)


elif(dom=="Others"):
    printai1.other()





