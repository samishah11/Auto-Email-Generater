import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(page_title="Auto Email Generator", page_icon="📧")

# Title and Description
st.title("📧 Auto Email Generator")
st.markdown("Generate professional emails quickly with predefined templates and tone control.")

# Sidebar Inputs
st.sidebar.header("✍️ Fill Email Details")

recipient_name = st.sidebar.text_input("Recipient Name", "John Doe")
email_purpose = st.sidebar.selectbox(
    "Purpose of Email",
    ["Job Application", "Meeting Request", "Follow-up", "Thank You", "Custom"]
)
tone = st.sidebar.selectbox("Tone of the Email", ["Formal", "Friendly", "Apologetic", "Grateful"])
custom_subject = st.sidebar.text_input("Custom Subject (optional)", "")
extra_details = st.sidebar.text_area("Extra Info or Notes (optional)")
sender_name = st.sidebar.text_input("Your Name", "Shahbaz Mehmood")
email_date = datetime.now().strftime("%B %d, %Y")

# Subject Generator
def generate_subject():
    if custom_subject:
        return custom_subject
    default_subjects = {
        "Job Application": "Application for Open Position",
        "Meeting Request": "Meeting Request",
        "Follow-up": "Following Up",
        "Thank You": "Thank You",
        "Custom": "Personal Message"
    }
    return default_subjects.get(email_purpose, "Professional Email")

# Body Generator
def generate_body():
    greeting = f"Dear {recipient_name},\n\n"
    
    # Base content per purpose
    content_map = {
        "Job Application": "I hope you are doing well. I am writing to express my interest in a role at your organization. My resume is attached for your review.",
        "Meeting Request": "I hope this message finds you well. I would like to request a meeting to discuss important matters at your convenience.",
        "Follow-up": "I’m following up regarding my last email. I would greatly appreciate any updates you can share.",
        "Thank You": "Thank you very much for your time and support. It has been a pleasure interacting with you.",
        "Custom": "I hope you're doing well. I just wanted to reach out."
    }

    body = content_map.get(email_purpose, "")
    
    # Adjust tone
    if tone == "Friendly":
        body = body.replace("I hope you are doing well", "Hey! Hope everything’s great on your end")
    elif tone == "Apologetic":
        body = "Please accept my sincere apologies. " + body
    elif tone == "Grateful":
        body = "I’m truly grateful for the opportunity to connect. " + body

    # Add custom notes
    if extra_details:
        body += f"\n\n{extra_details}"

    closing = f"\n\nSincerely,\n{sender_name}"
    return greeting + body + closing

# Output Section
st.subheader("📄 Generated Email")

subject = generate_subject()
body = generate_body()

# Markdown preview
with st.expander("📬 Email Preview (Markdown Format)"):
    st.markdown(f"""
**Subject:** {subject}

---

{body.replace('\n', '\n\n')}
""")

# Separate editable fields
st.text_input("✉️ Subject", value=subject, key="subject_output")
st.text_area("📝 Email Body", value=body, height=300)

# Download Button
file_content = f"Date: {email_date}\nTo: {recipient_name}\nSubject: {subject}\n\n{body}"
filename = f"{email_purpose.lower().replace(' ', '_')}_email.txt"

st.download_button(
    label="📥 Download Email as Text",
    data=file_content,
    file_name=filename,
    mime="text/plain"
)

# Footer
st.markdown("Made with ❤️ by [Shahbaz Mehmood]")
st.markdown("Contact me at ❤️[LinkedIn](http://www.linkedin.com/in/shahbaz-mehmood-data-analyst-19b32125b)")

