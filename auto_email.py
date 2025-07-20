import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Auto Email Generator", layout="centered")

# Title
st.title("📧 Auto Email Generator")

# Sidebar - user info
st.sidebar.header("✍️ Email Inputs")

# Input Fields
recipient_name = st.sidebar.text_input("Recipient's Name", "John Doe")
email_subject = st.sidebar.text_input("Email Subject", "Meeting Reminder")
main_message = st.sidebar.text_area("Main Message", "Just a reminder about our upcoming meeting tomorrow at 10 AM.")

your_name = st.sidebar.text_input("Your Name", "Shahbaz Mehmood")
closing_line = st.sidebar.text_input("Closing Line", "Best regards")

# Generate Email Button
if st.sidebar.button("Generate Email"):
    st.subheader("📨 Generated Email")

    email_body = f"""
Subject: {email_subject}

Dear {recipient_name},

{main_message}

{closing_line},  
{your_name}
"""
    st.code(email_body.strip(), language='text')
    st.success("Email generated! You can copy it from above.")

# Optional Footer
st.markdown("---")
st.caption(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
