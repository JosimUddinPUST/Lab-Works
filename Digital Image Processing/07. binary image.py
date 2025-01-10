from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale for binary processing
image = Image.open("lab_image.jpg").convert("L")

# Convert the grayscale image to a NumPy array
image_array = np.array(image)
height, width= image_array.shape
total_pixels = height * width

# Flatten the array for easier thresholding
binary_image = np.zeros(total_pixels, dtype=np.uint8)
threshold = 128

# Apply threshold to convert the image to binary
for i in range(total_pixels):
    binary_image[i] = 0 if image_array.flatten()[i] <= threshold else 255

# Reshape binary image to the original dimensions
binary_image = binary_image.reshape((height, width))

# Convert to PIL Image for display
b_img=Image.fromarray(binary_image)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image,cmap="gray")
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Binary Image")
plt.imshow(b_img,cmap="gray")
plt.axis('off')
plt.show()