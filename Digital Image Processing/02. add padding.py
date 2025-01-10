from PIL import Image, ImageOps

# Load the original image
image = Image.open("lab_image.jpg")

# Define the padding size (left, top, right, bottom)
padding = (20,20,20,20)  # Add 50 pixels of padding to all sides

# Create a new image with padding around the original image
padded_image = ImageOps.expand(image, border=padding, fill=(255, 100, 100))  # fill is black

# Display the image with padding
padded_image.show()
