# import streamlit as st
# import requests

# st.set_page_config(page_title="Reddit Persona Generator", layout="centered")

# st.title("🔎 Reddit Persona Generator")
# st.markdown("Paste a Reddit profile URL and get a generated persona using Gemini AI.")

# reddit_url = st.text_input("🔗 Enter Reddit profile URL", "")

# if st.button("✨ Generate Persona") and reddit_url.strip():
#     with st.spinner("Generating persona... Please wait."):
#         try:
#             response = requests.post(
#                 "http://localhost:8000/generate-persona",  # Change to your deployed URL later
#                 json={"url": reddit_url.strip()},
#                 timeout=60
#             )
#             data = response.json()

#             if "error" in data:
#                 st.error(f"❌ {data['error']}")
#             else:
#                 st.success(f"Persona for u/{data['username']}:")
#                 st.markdown(data["persona"])

#                 # Optional: Download button
#                 st.download_button(
#                     label="📥 Download Persona (.md)",
#                     data=data["persona"],
#                     file_name=f"{data['username']}_persona.md",
#                     mime="text/markdown"
#                 )
#         except Exception as e:
#             st.error(f"⚠️ Something went wrong: {e}")





import streamlit as st
import requests

# App config
st.set_page_config(page_title="Reddit Persona Generator", layout="centered")

# UI Title & Description
st.title("🔎 Reddit Persona Generator")
st.caption("Generate a human-like persona summary from any Reddit user's posts and comments using Gemini AI.")

# Input
reddit_url = st.text_input("🔗 Enter Reddit profile URL", "")

# Mode Selector
mode = st.radio("📝 Persona Style", ["Concise", "Detailed"], horizontal=True)

# Trigger Button
if st.button("✨ Generate Persona") and reddit_url.strip():
    with st.spinner("🧠 Generating persona... Please wait."):
        try:
            api_url = "http://localhost:8000/generate-persona"  # Replace if deploying

            # Send request to FastAPI
            response = requests.post(
                api_url,
                json={
                    "url": reddit_url.strip(),
                    "mode": mode.lower()  # Optional: modify backend to support this
                },
                timeout=60
            )
            data = response.json()

            # Show error or result
            if "error" in data:
                st.error(f"❌ {data['error']}")
            else:
                st.success(f"🎉 Persona for u/{data['username']}")
                st.markdown("Here is the AI-generated persona:")
                st.code(data["persona"], language="markdown")

                # Download button
                st.download_button(
                    label="📥 Download Persona (.md)",
                    data=data["persona"],
                    file_name=f"{data['username']}_persona.md",
                    mime="text/markdown"
                )
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
