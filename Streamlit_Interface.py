#st.experemental_rerun() - устарело в 1.27, у меня сейчас 1.26 (08.01.2024), вместо этого
#используется st.rerun(). обе эти функции, чтобы кнопка работала с одного клика а не с дефолтных двух.
import streamlit as st
from Parser.ParcerCore import parse_matches_and_save
# Remove Streamlit developer notes:
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
# Function to validate the match ID
def is_valid_id(match_id):
    return match_id.isdigit() and len(match_id) == 10

# Function to change page
def change_page(target_page):
    if st.session_state.current_page != target_page:
        st.session_state.current_page = target_page

# Navigation menu
def navigation_menu():
    st.sidebar.title("Navigation")
    if st.sidebar.button("Project Stage"):
        change_page('main')
        st.experimental_rerun()

    if st.sidebar.button("Request Stage"):
        change_page('request_stage')
        st.experimental_rerun()

    if st.sidebar.button("Analytics Stage"):
        change_page('analytics_stage')
        st.experimental_rerun()

# Main app function
def main():
    st.title("PROSTATA")
    # markdown to remove developer notes:
    st.markdown(hide_st_style, unsafe_allow_html=True)
    # Initialize session state variables
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'main'
    if 'match_ids' not in st.session_state:
        st.session_state.match_ids = []
    if 'menu_active' not in st.session_state:
        st.session_state.menu_active = False

    # Main Page
    if st.session_state.current_page == 'main':
        st.subheader("Project Stage")

        with st.form(key='match_id_form', clear_on_submit=True):

            match_id = st.text_input("Enter Match ID (10 digits):")
            submit_button = st.form_submit_button(label='Enter')

        if submit_button:
            if is_valid_id(match_id):
                st.session_state.match_ids.append(match_id)
                st.success("ID added. Enter another or click Save.")

            else:
                st.error("ID is in incorrect form! It contains only 10 numbers!")




        if st.session_state.match_ids:
            st.write("Stored IDs:")
            for stored_id in st.session_state.match_ids:
                st.write(stored_id)

            if st.button('Save IDs'):
                st.session_state.menu_active = True
                parse_matches_and_save(st.session_state.match_ids, output_file= "test_matches.csv")
                change_page('request_stage')
                st.experimental_rerun()

            if st.button('Reset IDs'):
                st.session_state.match_ids = []
                st.experimental_rerun()

    # Display navigation menu if active
    if st.session_state.menu_active:
        navigation_menu()

    # Request Stage Page
    if st.session_state.current_page == 'request_stage':
        st.subheader("Request Stage")
        st.write("This is the Request Stage page.")

    # Analytics Stage Page
    if st.session_state.current_page == 'analytics_stage':
        st.subheader("Analytics Stage")
        st.write("This is the Analytics Stage page.")

if __name__ == "__main__":
    main()
