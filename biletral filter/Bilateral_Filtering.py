import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
image = cv2.imread('img1.jpg', cv2.IMREAD_COLOR)

# Apply bilateral filter
bilateral_filtered_image = cv2.bilateralFilter(image, d=15, sigmaColor=75, sigmaSpace=75)

# Display the original and filtered images
plt.figure(figsize=(10, 5))

# Display original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes

# Display bilateral filtered image
plt.subplot(1, 2, 2)
plt.title('Bilateral Filtered Image')
plt.imshow(cv2.cvtColor(bilateral_filtered_image, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axes

plt.show()
