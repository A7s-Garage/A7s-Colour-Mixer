import streamlit as st
import matplotlib.colors as mcolors
import io
from PIL import Image

# Streamlit page configuration
st.set_page_config(page_title="A7's Colour Mixer", page_icon="🎨", layout="wide")

# Sidebar for RGB Sliders and Text Inputs
st.sidebar.title("Adjust RGB Values")

# Red, Green, Blue sliders with text input for both
red = st.sidebar.slider("Red", 0, 255, 128)
green = st.sidebar.slider("Green", 0, 255, 128)
blue = st.sidebar.slider("Blue", 0, 255, 128)

# Allow user to input RGB values as text
red_input = st.sidebar.text_input("Red (0-255)", str(red))
green_input = st.sidebar.text_input("Green (0-255)", str(green))
blue_input = st.sidebar.text_input("Blue (0-255)", str(blue))


st.sidebar.write("---")
st.sidebar.write("Made by A7 Nostalgic under A7's Garage")
st.sidebar.write("Any Bugs or Suggestions")
st.sidebar.write("Feel free to reach out at: [a7sgarage@gmail.com](mailto:a7sgarage@gmail.com)")

# Update slider values when user types in text input
try:
    red = int(red_input) if 0 <= int(red_input) <= 255 else red
    green = int(green_input) if 0 <= int(green_input) <= 255 else green
    blue = int(blue_input) if 0 <= int(blue_input) <= 255 else blue
except ValueError:
    pass  # If input is not valid, keep the slider values as they are

# Mix the color using RGB values
mixed_color_rgb = (red / 255, green / 255, blue / 255)  # Convert RGB to 0-1 range for display

# Generate the hex code
mixed_color_hex = mcolors.rgb2hex(mixed_color_rgb)

# Main screen display
st.title("A7's Colour Mixer")

# Show the resulting color as a large color block
st.markdown(
    f"<div style='width:100%; height: 450px; background-color:{mixed_color_hex};'></div>",
    unsafe_allow_html=True
)

st.markdown(f"### **RGB values**: **{red} : {green} : {blue}** \t    **HEX value**: **{mixed_color_hex.upper()}**")

# Create an image with the specified size (6720 x 3840) and fill it with the generated color
image = Image.new("RGB", (3840, 2160), (red, green, blue))

# Save image to a BytesIO object to prepare for download
image_io = io.BytesIO()
image.save(image_io, format='JPEG')
image_io.seek(0)

# Download button for the generated color swatch
st.download_button(
    label="Download Colour Swatch (3840x2160 JPEG)",
    data=image_io,
    file_name=f"#{mixed_color_hex[1:].upper()}_{red}_{green}_{blue}-A7.jpeg",
    mime="image/jpeg"
)

st.write("\n\n")
st.write('<p style="font-size: 16px;">Want to view your images?</p>', unsafe_allow_html=True)
st.write("https://a7s-image-viewer.streamlit.app/")
st.write('<p style="font-size: 16px;">Choose A7\'s Image Viewer, which supports 25+ 🖼 formats.</p>', unsafe_allow_html=True)
