import streamlit as st
import requests

st.set_page_config(page_title="Reddit Persona Generator", layout="centered")

st.title("🔎 Reddit Persona Generator")
st.caption(
    "Generate a human-like persona summary from any Reddit user's posts and comments using Gemini AI."
)

reddit_url = st.text_input("🔗 Enter Reddit profile URL", "")

mode = st.radio("📝 Persona Style", ["Concise", "Detailed"], horizontal=True)

if st.button("✨ Generate Persona") and reddit_url.strip():
    with st.spinner("🧠 Generating persona... Please wait."):
        try:
            api_url = "https://reddit-persona-generator-cj6y.onrender.com/generate-persona" 

            response = requests.post(
                api_url,
                json={
                    "url": reddit_url.strip(),
                    "mode": mode.lower(), 
                },
                timeout=60,
            )
            data = response.json()

            if "error" in data:
                st.error(f"❌ {data['error']}")
            else:
                st.success(f"🎉 Persona for u/{data['username']}")
                st.markdown("Here is the AI-generated persona:")
                st.code(data["persona"], language="markdown")

                st.download_button(
                    label="📥 Download Persona (.md)",
                    data=data["persona"],
                    file_name=f"{data['username']}_persona.md",
                    mime="text/markdown",
                )
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
