import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image using OpenCV
image = cv2.imread('lab_image.jpg')

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create the negative image
negative_image = 255 - image_rgb

# Plot the original and negative images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Negative Image")
plt.imshow(negative_image)
plt.axis("off")

plt.show()