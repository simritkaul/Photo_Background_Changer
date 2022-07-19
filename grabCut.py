import cv2
import os
import numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow.keras.utils import CustomObjectScope
from metrics import dice_loss, dice_coef, iou

def mask_refine(name):
  """ Seeding """
  np.random.seed(42)
  tf.random.set_seed(42)

  """ Global parameters """
  H = 512
  W = 512

  """ Loading model: DeepLabV3+ """
  with CustomObjectScope({'iou': iou, 'dice_coef': dice_coef, 'dice_loss': dice_loss}):
      model = tf.keras.models.load_model("model.h5")

  """ Read the image """

  # image = cv2.imread(f'remove_bg\{name}-crop.png', cv2.IMREAD_COLOR)
  image = cv2.imread('segmented_object_1.jpg', cv2.IMREAD_COLOR)
  h, w, _ = image.shape
  x = cv2.resize(image, (W, H))
  x = x/255.0
  x = x.astype(np.float32)
  x = np.expand_dims(x, axis=0)

  # """ Prediction """
  y = model.predict(x)[0]
  y = cv2.resize(y, (w, h))
  y = np.expand_dims(y, axis=-1)
  y = y > 0.5

  photo_mask = y
  masked_photo = image * photo_mask
  cv2.imwrite(f'remove_bg\{name}-Seg.png', masked_photo)
  print('Mask refining done')
  os.remove('segmented_object_1.jpg')

# def grab_cut(name):
#   img = cv2.imread('segmented_object_1.jpg', cv2.IMREAD_COLOR)
#   img_mask = cv2.imread(f'remove_bg\{name}-mask.png', cv2.IMREAD_COLOR)

#   gcMask = img_mask.copy()
#   gcMask[gcMask > 0] = cv2.GC_PR_FGD
#   gcMask[gcMask == 0] = cv2.GC_BGD

#   fgModel = np.zeros((1, 65), dtype="float")
#   bgModel = np.zeros((1, 65), dtype="float")

#   (gcMask, bgModel, fgModel) = cv2.grabCut(img, gcMask, None, bgModel, fgModel, iterCount= 5, mode=cv2.GC_INIT_WITH_MASK)

#   outputMask = np.where((gcMask == cv2.GC_BGD) | (gcMask == cv2.GC_PR_BGD), 0, 1)
#   outputMask = (outputMask * 255).astype("uint8")

#   output = cv2.bitwise_and(img, img, mask=outputMask)

#   cv2.imwrite(f'remove_bg\{name}-grabcut.png', output)

#   print('Grab Cut done')

#   # os.remove('segmented_object_1.jpg')
