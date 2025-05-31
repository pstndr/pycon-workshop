from PIL import Image
import streamlit as st

from utils.params import LOGOS_PATH


def menu(logo_path: str,):

    (c1, c2, c3, c4, c5) = st.columns(5)
    image = Image.open(logo_path)
    base_width = 100
    wpercent = base_width / float(image.size[0])
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((base_width, hsize), Image.Resampling.LANCZOS)

    c1.image(image, caption="")

    c2.page_link("pages/meme.py", label="Meme builder", icon="👾")
    c3.page_link(
        "pages/collage.py",
        label="Collage Maker",
        icon="🖼️",
        disabled=False,
    )
    c4.page_link(
        "pages/data_visualization.py",
        label="Data Viz",
        icon="📊",
        disabled=False,
    )
    c5.page_link(
        "pages/new_page.py",
        label="New Page",
        icon="📊",
        disabled=False,
    )
    st.divider()  # 👈 Draws a horizontal rule


def same_old():
    menu(logo_path=LOGOS_PATH)
