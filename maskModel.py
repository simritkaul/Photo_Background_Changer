# import the necessary packages
import numpy as rnp
import argparse
import imutils
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mask-rcnn", required=True,
	help="base path to mask-rcnn directory")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3,
	help="minimum threshold for pixel-wise mask segmentation")
ap.add_argument("-u", "--use-gpu", type=bool, default=0,
	help="boolean indicating if CUDA GPU should be used")
ap.add_argument("-e", "--iter", type=int, default=5,
	help="# of GrabCut iterations (larger value => slower runtime)")
args = vars(ap.parse_args())

