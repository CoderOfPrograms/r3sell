from rembg import remove
from PIL import Image
import io
import streamlit as st
import os
def improving_picture(file_name):
    image = file_name.getvalue()
    new_image = remove(image)
    return new_image