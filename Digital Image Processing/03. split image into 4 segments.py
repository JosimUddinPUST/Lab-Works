from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
print(cv2.__version__)


# Load the image
# image = Image.open('lab_image.jpg')
image_array=cv2.imread('lab_image.jpg')

# Get the dimensions of the image
height, width, _ = image_array.shape


# Split the image into 4 segments (top-left, top-right, bottom-left, bottom-right)
top_left = image_array[0:height//2, 0:width//2]
top_right = image_array[0:height//2, width//2:width]
bottom_left = image_array[height//2:height, 0:width//2]
bottom_right = image_array[height//2:height, width//2:width]

# Merge the segments back together
top = np.concatenate((top_left, top_right), axis=1)
bottom = np.concatenate((bottom_left, bottom_right), axis=1)
merged_image = np.concatenate((top, bottom), axis=0)


# Plot the original segments and the merged image
fig, ax = plt.subplots(2, 3, figsize=(12, 5))

# Display each segment without labels
ax[0][0].imshow(top_left)
ax[0][0].set_title('Top Left')
ax[0][0].axis('off')  # Hide the axis

ax[0][1].imshow(top_right)
ax[0][1].set_title('Top Right')
ax[0][1].axis('off')  # Hide the axis

ax[1][0].imshow(bottom_left)
ax[1][0].set_title('Bottom Left')
ax[1][0].axis('off')  # Hide the axis

ax[1][1].imshow(bottom_right)
ax[1][1].set_title('Bottom Right')
ax[1][1].axis('off')  # Hide the axis

# Display the merged image
ax[0][2].imshow(merged_image)
ax[0][2].set_title('Merged Image')
ax[0][2].axis('off')  # Hide the axis

# Hide the unused subplot
ax[1][2].axis('off')  # In case there is an extra plot in the grid

# Show the plot
plt.tight_layout()
plt.show()
