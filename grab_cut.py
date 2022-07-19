import cv2
import os
import numpy as np

def grab_cut(imagePath, name):
  # img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
  imgSeg = cv2.imread('segmented_object_1.jpg', cv2.IMREAD_COLOR)
  # img_mask = cv2.imread(f'remove_bg\{name}-mask.png', cv2.IMREAD_COLOR)

  img_mask = np.zeros(imgSeg.shape[:2], np.uint8)

  # gcMask = img_mask.copy()
  # gcMask[gcMask > 0] = cv2.GC_PR_FGD
  # gcMask[gcMask == 0] = cv2.GC_BGD

  fgModel = np.zeros((1, 65), dtype="float")
  bgModel = np.zeros((1, 65), dtype="float")

  rect = (5, 5, imgSeg.shape[1]-5, imgSeg.shape[0]-5)

  cv2.grabCut(imgSeg, img_mask, rect, bgModel, fgModel, iterCount= 20, mode=cv2.GC_INIT_WITH_RECT)

  outputMask = np.where((img_mask == 1) | (img_mask == 0), 0, 1).astype('uint8')
  outputImg = imgSeg * outputMask[:,:,np.newaxis]

  cv2.imwrite(f'remove_bg\{name}-grabcut.png', outputImg)

  print('Grab Cut done')

  # os.remove('segmented_object_1.jpg')