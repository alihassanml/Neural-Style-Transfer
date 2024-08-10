# Neural Style Transfer

Welcome to the **Neural Style Transfer** app! This application allows you to apply artistic styles to your images using a deep learning model. 

## Features

- **Upload Images:** Choose a content image and a style image.
- **Style Transfer:** Apply the style of the uploaded style image to the content image.
- **Visualize Results:** View the styled output alongside the original images.

## How to Use

1. **Upload Content Image:**
   - Select an image that you want to apply the style to.

2. **Upload Style Image:**
   - Select an image that provides the artistic style.

3. **See the Result:**
   - The application will process the images and display the styled result.

## Requirements

- Python 3.x
- Streamlit
- TensorFlow
- TensorFlow Hub
- PIL (Pillow)
- NumPy

## Installation

To set up the application, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/alihassanml/Neural-Style-Transfer.git
   ```

2. **Navigate to the Directory:**

   ```bash
   cd Neural-Style-Transfer
   ```

3. **Install Dependencies:**

   ```bash
   pip install streamlit tensorflow tensorflow_hub pillow numpy
   ```

4. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

5. **Open Your Browser:**
   - Visit `http://localhost:8501` to use the application.

## Notes

- Ensure that your images are in JPG, JPEG, or PNG format.
- The images will be displayed at a reduced size to fit the layout.

## Author

- **Ali Hassan** - [alihassanml](https://github.com/alihassanml)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
