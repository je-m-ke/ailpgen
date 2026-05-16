import streamlit as st
import requests

st.set_page_config(page_title="AI Landing Page Generator")

st.title("🚀 AI Landing Page Generator")
style = st.selectbox(
    "Choose Style",
    ["Modern", "Minimal", "Luxury", "Playful"]
)

st.write("Generate startup landing page copy using AI")

prompt = st.text_area(
    "Describe your startup idea",
    height=150
)

if st.button("Generate Landing Page Copy"):

    with st.spinner("Generating..."):

        response = requests.get(
            "https://ailpgen.onrender.com/generate",
            params={
            "prompt": prompt,
             "style": style
}
        )

        data = response.json()
        st.success("Landing Page Copy Generated")
        st.markdown("---")
        st.markdown(data["result"])


    
if st.button("Show History"):

        history = requests.get("https://ailpgen.onrender.com/history")

        history_data = history.json()

        for item in history_data:
            st.markdown("---")
            st.write("Prompt:", item["prompt"])
            st.write(item["result"])