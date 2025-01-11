import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread('lab_image.jpg')

# Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the gamma value
gamma = 1.9

# Apply power-law (gamma) transformation
c = 255 / (np.max(image_rgb) ** gamma)  # Calculate scaling constant
power_image = c * (image_rgb ** gamma)  # Apply the transformation

# Convert to uint8 for display
power_image = np.array(power_image, dtype=np.uint8)

# Apply log transformation
log_c = 255 / (np.log(1 + np.max(image_rgb)))
log_image = log_c * (np.log(1 + image_rgb))

# Convert to uint8 for display
log_image = np.array(log_image, dtype=np.uint8)

# Plot the original, power-law transformed, and log transformed images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Power-law (Gamma) Transformation")
plt.imshow(power_image)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Log Transformation")
plt.imshow(log_image)
plt.axis("off")

plt.show()