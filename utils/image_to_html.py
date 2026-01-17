import pytesseract
import numpy as np
from PIL import Image
from utils.html_builder import build_html

A4_WIDTH = 595
A4_HEIGHT = 842

def convert_image(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    img_np = np.array(image)
    h, w, _ = img_np.shape

    scale_x = A4_WIDTH / w
    scale_y = A4_HEIGHT / h

    data = pytesseract.image_to_data(
        img_np,
        output_type=pytesseract.Output.DICT
    )

    elements = []

    for i in range(len(data["text"])):
        if data["text"][i].strip():
            elements.append({
                "text": data["text"][i],
                "x": data["left"][i] * scale_x,
                "y": A4_HEIGHT - (data["top"][i] * scale_y),
                "font_size": max(8, data["height"][i] * scale_y)
            })

    return build_html(elements, A4_WIDTH, A4_HEIGHT)
