def build_html(elements, page_width, page_height):
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"/>
<style>

@page {{
    size: A4;
    margin: 0;
}}

body {{
    margin: 0;
    padding: 0;
    width: {page_width}px;
    height: {page_height}px;
    position: relative;
    font-family: Helvetica, Arial, sans-serif;
}}

.word {{
    position: absolute;
    white-space: nowrap;
    color: #000000;
}}

</style>
</head>

<body>
"""

    for el in elements:
        html += f"""
<div class="word" style="
    left:{int(el['x'])}px;
    top:{int(el['y'])}px;
    font-size:{int(el['font_size'])}px;
">
{el['text']}
</div>
"""

    html += """
</body>
</html>
"""
    return html
