import streamlit as st

st.set_page_config(page_title="Menu Bar + Form", layout="centered")

st.markdown(
    """
    <style>
    .menu-bar {
        display: flex;
        justify-content: center;
        gap: 2rem;
        padding: 12px 0;
        background: #f1f5f9;
        border-radius: 10px;
        margin-bottom: 24px;
    }
    .menu-bar a {
        color: #0f172a;
        font-weight: 600;
        text-decoration: none;
        padding: 4px 8px;
    }
    .menu-bar a:hover {
        color: #2563eb;
    }
    .menu-bar .active {
        color: #2563eb;
        border-bottom: 2px solid #2563eb;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

menu_options = ["Home", "Form", "About"]
selected_page = st.radio("", menu_options, horizontal=True)

if selected_page == "Home":
    st.header("Welcome to the app")
    st.write("Use the menu above to go to the form or read more about this page.")
    st.write("This is a simple Streamlit app with a menu bar and a form.")

elif selected_page == "Form":
    st.header("Contact Form")
    st.write("Please fill out the fields below and submit your information.")

    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")

    if submitted:
        if not name or not email:
            st.error("Please enter both name and email.")
        else:
            st.success(f"Thanks, {name}! Your message has been sent.")
            st.write("We will contact you at", email)

else:
    st.header("About")
    st.write("This example app shows how to create a menu bar and a form using Streamlit.")
    st.write("Use the menu at the top to switch between pages.")
