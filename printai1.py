import ai
import streamlit as st

def print_below(text):
    response = ai.generate_ai_for_topics(text)
    st.session_state.roadmap_content = ai.extract_useful_content(response)
    # return st.session_state.roadmap_content
    return st.markdown(st.session_state.roadmap_content)

def other():
    dom = st.text_input("Enter the field")
    if 'prev_dom' not in st.session_state:
        st.session_state.prev_dom = ""

    if dom != st.session_state.prev_dom:
        st.session_state.roadmap_content = ""  # Clear previous content if domain changed
        st.session_state.prev_dom = dom  # Update the previous domain

    # Now make the AI call only if there's new content
    if dom and not st.session_state.roadmap_content:
        with st.spinner("Generating a detailed learning plan..."):
            response = ai.generate_ai(dom)
            st.session_state.roadmap_content = ai.extract_useful_content(response)

        # return st.session_state.roadmap_content
        st.markdown(st.session_state.roadmap_content)

def display_keywords_as_buttons(csv_text):
    if "keywords" not in st.session_state:
        st.session_state.keywords = [keyword.strip() for keyword in csv_text.split(',')]

    keywords = st.session_state.keywords
    buttons_per_row = 2  # Define number of buttons per row

    # Create buttons in a grid layout
    for i in range(0, len(keywords), buttons_per_row):
        cols = st.columns(buttons_per_row)  # Create columns for each row
        for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
            if j < len(cols):  # Ensure j doesn't exceed the number of columns
                unique_key = f"button_{i+j}_{keyword}"
                with cols[j]:
                    if st.button(keyword, key=unique_key):
                        st.session_state.selected_button = keyword

    # If a button is selected, generate AI content for that keyword
    if 'selected_button' in st.session_state:
        return print_below(st.session_state.selected_button)

def append_csv_to_list(csv_text):
    values = [value.strip() for value in csv_text.split(',')]
    result_list = []
    for value in values:
        cleaned_value = value.strip()  # Remove any extra whitespace
        if cleaned_value:  # Append only if not an empty string
            result_list.append(cleaned_value)
            st.markdown(result_list)
    # return result_list