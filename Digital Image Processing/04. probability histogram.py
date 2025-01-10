from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert to grayscale
image = Image.open('lab_image.jpg').convert('L')

# Convert image to a numpy array
image_array = np.array(image)

# Get image dimensions
height, width = image_array.shape[:2]  # Assuming it's a grayscale image

# Initialize histogram for 256 intensity levels
hist_manual = [0] * 256

# Manually compute the histogram
for i in range(height):
    for j in range(width):
        pixel_value = image_array[i, j]
        hist_manual[pixel_value] += 1

# Total number of pixels in the image
total_pixels = height * width

prob_hist=[0]*256
for i in range(256):
    prob_hist[i]=hist_manual[i]/total_pixels

# Plot the manually computed probability histogram
plt.figure(figsize=(10, 5))
plt.bar(range(256), prob_hist, edgecolor='black')
plt.xlim(0, 255)
plt.title('Manually Computed Probability Histogram of Pixel Intensities')
plt.xlabel('Pixel Intensity')
plt.ylabel('Probability')
plt.show()
