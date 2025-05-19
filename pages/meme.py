# meme_generator.py

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

from utils.platform.header import same_old


same_old()
# Titolo dell'app
st.title("🎉 Meme Creator 🎉")
st.write("Upload an image, add your text and download your meme!")

# Caricamento dell'immagine
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Image uploaded", use_container_width=True)

    # Input per il testo
    st.write("Add your text:")

    (sx, dx) = st.columns(2)
    top_text = sx.text_input("Top text")
    bottom_text = dx.text_input("Bottom text")

    # Menu a tendina per il colore del testo
    text_color = sx.selectbox("Choose text color", ["white", "black", "red", "blue", "green"])

    # Slider per la dimensione del testo
    text_size = dx.slider("Choose text size", min_value=10, max_value=100, value=40)

    # Font per il testo
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Helvetica.ttc", text_size)
    except IOError:
        st.warning("Font non trovato! Verrà utilizzato un font di default.")
        font = ImageFont.load_default()

    # Generazione del meme
    if st.button("Create Meme"):
        img_with_text = img.copy()
        draw = ImageDraw.Draw(img_with_text)

        # Aggiungere il testo in alto
        if top_text:
            bbox = draw.textbbox((0, 0), top_text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw.text(
                ((img.width - text_width) / 2, 10), top_text, font=font, fill=text_color
            )

        # Aggiungere il testo in basso
        if bottom_text:
            bbox = draw.textbbox((0, 0), bottom_text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw.text(
                ((img.width - text_width) / 2, img.height - text_height - 10),
                bottom_text,
                font=font,
                fill=text_color,
            )

        # Mostrare il meme generato
        st.image(img_with_text, caption="Meme created", use_container_width=True)

        # Salvare e scaricare il meme
        img_with_text.save("meme.png")
        with open("meme.png", "rb") as file:
            st.download_button(
                label="Scarica il tuo meme",
                data=file,
                file_name="meme.png",
                mime="image/png",
            )

# Footer
st.write("💡 Powered by Streamlit | Enjoy!")
