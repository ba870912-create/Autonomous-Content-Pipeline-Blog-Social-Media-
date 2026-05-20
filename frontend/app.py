import streamlit as st
import requests

st.title("📝 Content Pipeline")

topic = st.text_input("Topic", "Microservices Architecture Best Practices")
audience = st.text_input("Target Audience", "Software developers")

if st.button(" Generate Content"):
    with st.spinner("Generating... this may take a few minutes ⏳"):
        try:
            res = requests.post("http://localhost:8000/generate", json={
                "topic": topic,
                "audience": audience
            }, timeout=300)
            data = res.json()

            st.subheader("📄 Blog Post")
            st.markdown(data["blog"])

            st.subheader("🔍 SEO")
            st.code(data["seo"], language="json")

            st.subheader("📱 Social Media")
            st.markdown(data["social"])

            st.subheader("✅ Review")
            st.markdown(data["review"])

        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. Try again.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

st.divider()

if st.button(" Show History"):
    try:
        res = requests.get("http://localhost:8000/history", timeout=10)
        history = res.json()
        if history:
            for item in history:
                st.write(f"**{item['topic']}** — {item['created_at']}")
        else:
            st.info("No history yet.")
    except Exception as e:
        st.error(f" Error: {str(e)}")