import streamlit as st
from PIL import Image

from utils.platform.header import same_old


same_old()

st.title("📸 Collage Maker")
st.write("Upload multiple images and create a collage!")

uploaded_files = st.file_uploader("Upload images", type=["jpg", "png"], accept_multiple_files=True)
if uploaded_files:
    images = [Image.open(file) for file in uploaded_files]

    # Selezione del layout
    layout = st.selectbox("Choose a layout", ["2x2", "3x3"])
    if layout == "2x2":
        rows, cols = 2, 2
    elif layout == "3x3":
        rows, cols = 3, 3

    # Creazione del collage
    collage_width = min(img.width for img in images)
    collage_height = min(img.height for img in images)
    collage = Image.new("RGB", (collage_width * cols, collage_height * rows))

    for i, img in enumerate(images):
        x = (i % cols) * collage_width
        y = (i // cols) * collage_height
        collage.paste(img, (x, y))

    # Mostrare il collage
    st.image(collage, caption="Collage", use_container_width=True)

    # Scaricare il collage
    collage.save("collage.png")
    with open("collage.png", "rb") as file:
        st.download_button(
            label="Download Collage",
            data=file,
            file_name="collage.png",
            mime="image/png",
        )

st.write("💡 Powered by Streamlit | Enjoy!")
