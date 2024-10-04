import streamlit as st
import ai
import printai1

# Set up the sidebar navigation
st.sidebar.title("Navigation")

# Define the different pages
pages = ["ClassMent Home", "ClassMent Explorer Lab", "About Us", "Contact"]

# Create the navigation menu in the sidebar
selection = st.sidebar.radio("Go to", pages)

# Display content based on the selection
if selection == "ClassMent Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the Streamlit app.")


elif selection == "ClassMent Explorer Lab":
    st.title("Welcome to ClassMent Explorer Lab")

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

elif selection == "About Us":
    st.title("About Us")
    st.write("This page contains information about the application.")
elif selection == "Contact":
    st.title("Contact Us")
    st.write("This page contains contact information.")





