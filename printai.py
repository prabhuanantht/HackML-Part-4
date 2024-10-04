# import ai
# import streamlit as st


# def print_below(text):
    
#     response = ai.generate_ai_for_topics(text)
#     st.session_state.roadmap_content = ai.extract_useful_content(response)
#     # st.markdown(st.session_state.roadmap_content)
#     # st.success(st.session_state.roadmap_content)
#     return st.session_state.roadmap_content


# def other():
#     dom = st.text_input("Enter the field")
#     if 'prev_dom' not in st.session_state:
#         st.session_state.prev_dom = ""

#     if dom != st.session_state.prev_dom:
#         st.session_state.roadmap_content = ""  # Clear previous content if domain changed
#         st.session_state.prev_dom = dom  # Update the previous domain

#     # Now make the AI call only if there's new content
#     if dom and not st.session_state.roadmap_content:
#         with st.spinner("Generating a detailed learning plan..."):
#             response = ai.generate_ai(dom)
#             st.session_state.roadmap_content = ai.extract_useful_content(response)

#         # Display the generated roadmap content
#         # st.markdown(st.session_state.roadmap_content)
#         return st.session_state.roadmap_content

#          # if(ip):
#             #     if not st.session_state.roadmap_content:
#             #         response = ai.generate_ai(ip)
#             #         st.session_state.roadmap_content = ai.extract_useful_content(response)
#             #     roadmap_content = st.session_state.roadmap_content
#             #     st.markdown(roadmap_content, unsafe_allow_html=True)
#             #     # st.success(roadmap_content)
#             #     # for step in roadmap_content:
#             #     #     st.checkbox(step)



# # def display_keywords_as_buttons(csv_text):
# #     # Split the CSV text into a list of keywords
# #     if "keywords" not in st.session_state:
# #         keywords = [keyword.strip() for keyword in csv_text.split(',')]
# #         st.session_state.keywords = keywords
    
# #     # Define the number of buttons per row
# #     buttons_per_row = 2  # You can change this number based on your preference
    
# #     # Create rows and organize buttons in a grid
# #     for i in range(0, len(keywords), buttons_per_row):
# #         cols = st.columns(buttons_per_row)  # Create columns for each row
# #         for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
# #             # Use a column for each button, with a unique key
# #             with cols[j]:
# #                 if st.button(keyword, key=f"button_{i+j}"):
# #                     st.session_state.selected_button = keyword
# #                     # str = print_below(keyword)
# #                     # return str
# #     if 'selected_button' in st.session_state:
# #         return print_below(st.session_state.selected_button)          

# # def display_keywords_as_buttons(csv_text):
# #     # Split the CSV text into a list of keywords
# #     if "keywords" not in st.session_state:
# #         st.session_state.keywords = [keyword.strip() for keyword in csv_text.split(',')]

# #     keywords = st.session_state.keywords
# #     buttons_per_row = 2  # Define number of buttons per row

# #     # Create buttons in a grid layout
# #     for i in range(0, len(keywords), buttons_per_row):
# #         cols = st.columns(buttons_per_row)  # Create columns for each row
# #         for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
# #             # Use a column for each button
# #             with cols[j]:
# #                 if st.button(keyword, key=f"button_{i+j}"):
# #                     st.session_state.selected_button = keyword

# #     # If a button is selected, generate AI content for that keyword
# #     if 'selected_button' in st.session_state:
# #         return print_below(st.session_state.selected_button)





#     # # Create columns for the buttons
#     # num_columns = (len(keywords) + buttons_per_row - 1) // buttons_per_row  # Calculate number of columns needed
#     # columns = st.columns(num_columns)

#     # # Display buttons in a grid layout
#     # for index, keyword in enumerate(keywords):
#     #     col_index = index % buttons_per_row  # Determine the column index
#     #     with columns[col_index]:
#     #         if st.button(keyword, key=f"button_{index}"):
#     #             print_below(keyword)




# # def display_keywords_as_buttons(csv_text):
# #     # Split the CSV text into a list of keywords
# #     if "keywords" not in st.session_state:
# #         st.session_state.keywords = [keyword.strip() for keyword in csv_text.split(',')]

# #     keywords = st.session_state.keywords
# #     buttons_per_row = 2  # Define the number of buttons per row

# #     # Create buttons in a grid layout
# #     for i in range(0, len(keywords), buttons_per_row):
# #         cols = st.columns(buttons_per_row)  # Create columns for each row
# #         for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
# #             # Use a unique key by combining the button index with a prefix
# #             unique_key = f"button_{i+j}_{st.session_state.selected_roadmap}"  # Add roadmap context
# #             with cols[j]:
# #                 if st.button(keyword, key=unique_key):
# #                     st.session_state.selected_button = keyword

# #     # If a button is selected, generate AI content for that keyword
# #     if 'selected_button' in st.session_state:
# #         return print_below(st.session_state.selected_button)


# def display_keywords_as_buttons(csv_text):
#     # Split the CSV text into a list of keywords
#     if "keywords" not in st.session_state:
#         st.session_state.keywords = [keyword.strip() for keyword in csv_text.split(',')]

#     keywords = st.session_state.keywords
#     buttons_per_row = 2  # Define number of buttons per row

#     # Create buttons in a grid layout
#     for i in range(0, len(keywords), buttons_per_row):
#         cols = st.columns(buttons_per_row)  # Create columns for each row
#         for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
#             if j < len(cols):  # Ensure j doesn't exceed the number of columns
#                 unique_key = f"button_{i+j}_{keyword}"
#                 with cols[j]:
#                     if st.button(keyword, key=unique_key):
#                         st.session_state.selected_button = keyword

#     # If a button is selected, generate AI content for that keyword
#     if 'selected_button' in st.session_state:
#         return print_below(st.session_state.selected_button)
    








    






# # def display_keywords_as_buttons(csv_text):
# #     # Split the CSV text into a list of keywords
# #     if "keywords" not in st.session_state:
# #         st.session_state.keywords = [keyword.strip() for keyword in csv_text.split(',')]

# #     keywords = st.session_state.keywords
# #     buttons_per_row = 2  # Define number of buttons per row

# #     # Create buttons in a grid layout
# #     for i in range(0, len(keywords), buttons_per_row):
# #         cols = st.columns(buttons_per_row)  # Create columns for each row
# #         for j, keyword in enumerate(keywords[i:i + buttons_per_row]):
# #             # Generate a unique key for each button using the index and keyword
# #             unique_key = f"button_{i+j}_{keyword}"
# #             with cols[j]:
# #                 if st.button(keyword, key=unique_key):
# #                     st.session_state.selected_button = keyword

# #     # If a button is selected, generate AI content for that keyword
# #     if 'selected_button' in st.session_state:
# #         return print_below(st.session_state.selected_button)




# def append_csv_to_list(csv_text):
# # Split the CSV text into a list based on commas
    
#     values = [value.strip() for value in csv_text.split(',')]
#     # Create an empty list to hold the cleaned values
#     result_list = []
    
#     # Append cleaned values to the list
#     for value in values:
#         cleaned_value = value.strip()  # Remove any extra whitespace
#         if cleaned_value:  # Append only if not an empty string
#             result_list.append(cleaned_value)
    
#     return result_list










































import ai
import streamlit as st

def print_below(text):
    response = ai.generate_ai_for_topics(text)
    st.session_state.roadmap_content = ai.extract_useful_content(response)
    return st.session_state.roadmap_content

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

        return st.session_state.roadmap_content

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

    return result_list