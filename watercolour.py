import os
import cv2

def watercolourEffect(name):
  masked_photo = cv2.imread('segmented_object_1.jpg', cv2.IMREAD_COLOR)

  os.remove('segmented_object_1.jpg')

  image_cleared = cv2.medianBlur(masked_photo, 3)
  image_cleared = cv2.medianBlur(image_cleared, 3)

  image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=5)

  image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

  for i in range(2):
    image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

  for i in range(3):
    image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

  gaussian_mask= cv2.GaussianBlur(image_filtered, (99,99), 2)
  image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
  image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

  cv2.imwrite(f'remove_bg\{name}-watercolor.png', image_sharp)

  print('Water Colour effect done')