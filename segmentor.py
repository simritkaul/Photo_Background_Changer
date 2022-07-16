from pixellib.instance import instance_segmentation
import os

def create_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

def subjectExtractor(imagePath):
  segmentation_model = instance_segmentation()
  segmentation_model.load_model('mask_rcnn_coco.h5')

  """ Directory for storing files """
  create_dir("remove_bg")

  """ Read the image """
  # image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

  target_classes = segmentation_model.select_target_classes(person=True)

  segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True, extract_segmented_objects= True, save_extracted_objects=True)
  # res = segmentation_model.segmentImage(imagePath, segment_target_classes= target_classes, show_bboxes= True, extract_segmented_objects= True, save_extracted_objects=True)
  # img = res[1]