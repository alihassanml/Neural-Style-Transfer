import streamlit as st
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import io

# Load the model from TensorFlow Hub
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(image_file):
    image = Image.open(image_file)
    image = image.convert("RGB")
    image = np.array(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = image[tf.newaxis, :]
    return image

def save_image(image_array):
    image_array = np.squeeze(image_array)
    image_array = (image_array * 255).astype(np.uint8)
    image = Image.fromarray(image_array)
    return image

st.title('Neural Style Transfer Application')

# Create two columns for file upload
col1, col2 = st.columns(2)

with col1:
    uploaded_content_image = st.file_uploader("Upload Content Image", type=["jpg", "jpeg", "png"])
    st.image(uploaded_content_image, caption="Content Image", use_column_width=False, width=300)

with col2:
    uploaded_style_image = st.file_uploader("Upload Style Image", type=["jpg", "jpeg", "png"])
    st.image(uploaded_style_image, caption="Style Image", use_column_width=False, width=300)


if st.button('Submit'):
    st.success('File Transfer')
    content_image = load_image(uploaded_content_image)
    style_image = load_image(uploaded_style_image)
    
    
    st.title('Style Transfer With tensorflow')
    styled_image = model(tf.constant(content_image), tf.constant(style_image))
    
    # Display styled image with smaller size
    styled_image_pil = save_image(styled_image)
    st.image(styled_image_pil, caption="Styled Image", use_column_width=False, width=600)
