from PIL import Image
import os
import cv2

'''Segment Image Masker'''
def imageToMask(imagePath, savePath):
  img = Image.open(imagePath)
  
  data = img.getdata()
  # print(list(data))

  newData = []
  
  for item in data:
      if (item[0] <= 10 and item[1] <= 10 and item[2] <= 10):
          newData.append((0, 0, 0))
      else:
          newData.append((1, 1, 1))
  
  img.putdata(newData)
  img.save(savePath, "PNG")
  imagemask = cv2.imread(savePath)
  print(imagemask.shape)
  cv2.imshow('Mask', imagemask * 255)
  cv2.waitKey(0)
  
  print("Segment Mask Generation Done")

  # os.remove(imagePath)