from pixellib.instance import instance_segmentation
import os
import cv2
import numpy as np
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

def create_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

def grab_cut(imagePath, name, mask, bbox):
  img = cv2.imread(imagePath, cv2.IMREAD_COLOR)
  # imgSeg = cv2.imread('segmented_object_1.jpg', cv2.IMREAD_COLOR)
  img_mask = mask

  gcMask = mask.copy()
  gcMask = np.float32(gcMask).astype(np.uint8)
  print(f'Image: {img.shape}')
  print(f'Mask: {gcMask.shape}')
  gcMask[gcMask > 0] = cv2.GC_PR_FGD
  gcMask[gcMask == 0] = cv2.GC_BGD

  fgModel = np.zeros((1, 65), dtype="float")
  bgModel = np.zeros((1, 65), dtype="float")

  (gcMask, bgModel, fgModel) = cv2.grabCut(img, gcMask, None, bgModel, fgModel, iterCount= 1, mode=cv2.GC_INIT_WITH_MASK)

  outputMask = np.where((gcMask == cv2.GC_BGD) | (gcMask == cv2.GC_PR_BGD), 0, 1).astype(np.uint8)
  outputMask = (outputMask * 255).astype("uint8")

  # outputMask = np.array(outputMask)

  output = cv2.bitwise_and(img, img, mask=outputMask)

  # rect = (5, 5, imgSeg.shape[1]-5, imgSeg.shape[0]-5)

  # cv2.grabCut(imgSeg, img_mask, rect, bgModel, fgModel, iterCount= 20, mode=cv2.GC_INIT_WITH_RECT)
  print(bbox)

  cv2.imwrite(f'remove_bg\{name}-grabcut.png', output)

  print('Grab Cut done')

def subjectExtractor(imagePath, name):
  segmentation_model = instance_segmentation()
  segmentation_model.load_model('mask_rcnn_coco.h5')

  """ Directory for storing files """
  create_dir("remove_bg")

  """ Read the image """
  # image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

  target_classes = segmentation_model.select_target_classes(person=True)

  # segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True, extract_segmented_objects= True, save_extracted_objects=True)
  seg_mask, res = segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True, extract_segmented_objects= True, save_extracted_objects=True)
  # img = res[1]
  mask = seg_mask['masks']
  bbox = seg_mask['rois']
  grab_cut(imagePath, name, mask, bbox)