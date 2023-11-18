import streamlit as st
from transformers import pipeline
from PIL import Image
import base64
from improving_picture import improving_picture

pipeline = pipeline(task="image-classification", model="julien-c/hotdog-not-hotdog")

# Set the title and text color to dark green
st.markdown('<h1 style="color:darkgreen;">R3SELL</h1>', unsafe_allow_html=True)

# Create a file input option for uploading an image
file_name = st.file_uploader("Upload an image file (JPEG, PNG, etc.)", type=["png", "jpg", "jpeg"])

# Create a camera input widget to capture images from the webcam
image = st.camera_input("Capture an image from your webcam")

# Add a text bar to add a title
image_title = st.text_input("Image Title", value="Specificity is nice!")

# Add a text bar to add a description
image_description = st.text_input("Image Description", value="(Optional)")

if file_name is not None or image is not None:
    # Check if the image is a webcam image
    if file_name == 'webcam_image.jpg':
        # Use the Base64 encoded image
        image = Image.open('data:image/jpeg;base64,' + img_encoded)
    else:
        # Open the uploaded image
        image = image = Image.open(file_name)
        image_rem = improving_picture(file_name)

    # Pass the captured image to the pipeline function
    predictions = pipeline(image)

    col1, col2 = st.columns(2)


    col1.image(image_rem, use_column_width=True)

    col2.header("Probabilities")
    for p in predictions:
        col2.subheader(f"{ p['label'] }: { round(p['score'] * 100, 1)}%")
