from PIL import Image
import os

'''Transparent BG Image'''
def convertImageBG(imagePath, savePath):
  img = Image.open(imagePath)
  img = img.convert("RGBA")
  
  data = img.getdata()
  # print(list(data))

  newData = []
  
  for item in data:
      if (item[0] < 20 and item[1] < 20 and item[2] < 20 and item[3] == 255):
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  
  img.putdata(newData)
  img.save(savePath, "PNG")
  print("Transparent Segment Background Done")

  os.remove(imagePath)