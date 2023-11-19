import streamlit as st
from transformers import pipeline
from PIL import Image
from rembg import remove
from io import BytesIO
from ebay import search_ebay_sold_items
from llava import get_quality
from os.path import abspath
import os
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


def improving_picture(file_name):
    image = file_name.getvalue()
    new_image = remove(image, alpha_matting=True)
    return new_image
def add_white_background_to_image_bytes(modified_image_bytes):
    # Convert bytes to PIL Image
    modified_image = Image.open(BytesIO(modified_image_bytes))
    
    # Create a new image with a white background of the same size as the modified image
    new_image = Image.new("RGB", modified_image.size, "white")
    
    # Paste the modified image onto the white background
    new_image.paste(modified_image, (0, 0), modified_image)
    
    # Convert the new image to bytes
    output_image_bytes = BytesIO()
    new_image.save(output_image_bytes, format='PNG')  # Change format if needed
    
    return output_image_bytes.getvalue()
pipeline = pipeline(task="image-classification", model="julien-c/hotdog-not-hotdog")

# Set the title and text color to dark green
st.markdown('<h1 style="color:darkgreen;">R3SELL</h1>', unsafe_allow_html=True)

# Create a file input option for uploading an image
file_name = st.file_uploader("Upload an image file (JPEG, PNG, etc.)", type=["png", "jpg", "jpeg"])

# Create a camera input widget to capture images from the webcam
image = st.camera_input("Capture an image from your webcam")

# Add a text bar to add a title
#image_title = st.text_input("Image Title", value="Specificity is nice!")
st.write('Prices: ' + str(search_ebay_sold_items(st.text_input("Image Title", value="Specificity is nice!"))))

# Add a text bar to add a description
#mage_description = st.text_input("Image Description", value="(Optional)")

if file_name is not None or image is not None:
    # Check if the image is a webcam image

    if file_name == 'webcam_image.jpg':
        # Use the Base64 encoded image
        image = Image.open('data:image/jpeg;base64,' + img_encoded)
    else:
        # Open the uploaded image
        image = Image.open(file_name)
        
        nameFile = file_name.name
        def save_uploaded_image_locally(uploaded_file):
            if uploaded_file is not None:
                file_path = os.path.join(".", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
        save_uploaded_image_locally(file_name)
        st.write('Description: ' + get_quality(abspath(nameFile))[5:])

        image_rem = add_white_background_to_image_bytes(improving_picture(file_name))

    # Pass the captured image to the pipeline function
    predictions = pipeline(image)

    col1, col2 = st.columns(2)


    col1.image(image_rem, use_column_width=True)

    col2.header("Probabilities")
    for p in predictions:
        col2.subheader(f"{ p['label'] }: { round(p['score'] * 100, 1)}%")
anthropic = Anthropic(
    api_key="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",
)
name = "Macbook Pro M1"
description = "get_quality(abspath(nameFile))[5:]"
price = str(search_ebay_sold_items(st.text_input("Image Title", value="Specificity is nice!")))
s = "Name of Product is "+ name +". Min, 1st quartile, median, 3rd quartile, and max of used prices are "+ price +". Assume max is best used quality and min in worst used quality. Color and defects(consider in price and description) -  "+description+"(sub color with official colorname). Generate a price given previous which ends in .99. Feel free to search the web. Video should be a product/review video make sure video is real. Generate a product description and the relevant information for an ebay listing. Search the web for additional help and it should be good for the ebay algorithms. Give it as a JSON with these categories Product Name, Price, Condition, Brand, Type, Color, Description, Specifications, Size, Video, Department. Generate Facebook and Instagram ads with hashtags and other stuff to boost algorithm. "
promp = "\n\nHuman ${userQuestion}\n\nAssistant:"
completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=1000,
    prompt=f"{HUMAN_PROMPT} "+s+f" {AI_PROMPT}",
)
st.write(completion.completion)