import cv2
import numpy as np
import csv

# Read the image
image = cv2.imread('/home/navya/Pictures/n.jpg')

# Convert image to RGB format
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, channels = image_rgb.shape

# Flatten the image to get RGB values for each pixel
rgb_values = np.reshape(image_rgb, (height * width, channels))

# Write RGB values to a CSV file
with open('rgb_values.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['R', 'G', 'B'])
    csvwriter.writerows(rgb_values)
print("successfull")
    
