import pdfplumber
from utils.html_builder import build_html

A4_WIDTH = 595
A4_HEIGHT = 842

def convert_pdf(uploaded_file):
    elements = []

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_height = page.height
            words = page.extract_words(use_text_flow=True)

            for w in words:
                elements.append({
                    "text": w["text"],
                    "x": w["x0"],
                    "y": page_height - w["top"],
                    "font_size": max(8, w["bottom"] - w["top"])
                })

    return build_html(elements, A4_WIDTH, A4_HEIGHT)
