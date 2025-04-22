import streamlit as st
import re 


st.set_page_config(page_title="Password Strength Checker")

st.title("Password Strength Checker")
st.markdown("""
## Welcome to the Password Strength Checker!""")


password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
      score += 1
    else :
       feedback.append("8️⃣ Password should be atleast 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
          score += 1
    else:
          feedback.append("🅰 Password should contain both upper and lower case letter.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("1️⃣ Password should contain atleast one digit.")
    
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("⁉ Password should contain atleast one special character. (!@#$%&*)")

    if score == 4:
        feedback.append("😆 Your password is strong.")
    elif score == 3:
        feedback.append("🙂 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("😭 Your password is weak, please make it stronger.")

    if feedback:
        st.markdown("## improvement suggestion:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")