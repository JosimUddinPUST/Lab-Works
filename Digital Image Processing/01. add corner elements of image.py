from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = Image.open('lab_image.jpg')

# Convert the image to grayscale
gray_image = image.convert('L')

# Convert the grayscale image to a numpy array with proper dtype (uint8)
image_array = np.array(gray_image, dtype=np.uint8)

# Get the shape of the array (height and width of the image)
height, width = image_array.shape

# Get the corner elements
top_left = image_array[0, 0]
top_right = image_array[0, width - 1]
bottom_left = image_array[height - 1, 0]
bottom_right = image_array[height - 1, width - 1]

# Print corner elements to confirm
print("Corner elements are:", top_left, top_right, bottom_left, bottom_right)

# Calculate corner sum and print again for verification
corner_sum = np.add(top_left, np.add(top_right, np.add(bottom_left, bottom_right)), dtype=np.int32)
print("Sum of corner elements (manual):", corner_sum)



# Get the boundary rows and columns (excluding the corners)
top_row = image_array[0, 1:-1]  # Exclude top-left and top-right
bottom_row = image_array[height - 1, 1:-1]  # Exclude bottom-left and bottom-right
left_column = image_array[1:-1, 0]  # Exclude top-left and bottom-left
right_column = image_array[1:-1, width - 1]  # Exclude top-right and bottom-right

# Add the Boundary elements (excluding corners)
boundary_sum = (np.sum(top_row) + np.sum(bottom_row) + np.sum(left_column) + np.sum(right_column))

# Total boundary sum including corners (if you need it)
total_boundary_sum = boundary_sum + corner_sum

print("Total boundary sum (including corners):", total_boundary_sum)

plt.figure(figsize=(12,6))

plt.subplot(1,1,1)
plt.title("Original Image")
plt.axis('off')
plt.imshow(image)
plt.show()