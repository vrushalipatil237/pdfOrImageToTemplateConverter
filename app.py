import streamlit as st
from utils.pdf_to_html import convert_pdf
from utils.image_to_html import convert_image

st.set_page_config(page_title="PDF/Image to HTML", layout="wide")

st.title("📄 PDF / Image → HTML (Java PDF Compatible)")

uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        html_content = convert_pdf(uploaded_file)
    else:
        html_content = convert_image(uploaded_file)

    st.subheader("🔍 HTML Preview")
    st.components.v1.html(html_content, height=700, scrolling=True)

    st.download_button(
        label="⬇ Download HTML (Java-PDF Safe)",
        data=html_content,
        file_name="converted.html",
        mime="text/html"
    )
