from bgChanger import background_changer
from segmentor import subjectExtractor
from transparent import convertImageBG
from watercolour import watercolourEffect
import os

pos_w = int(input('Enter x position: '))
pos_h = int(input('Enter y position: '))

scale = float(input('Enter the scale factor (0.5 means half, 4 means four times): '))

""" Load the dataset """
imageList = os.listdir('images/subject/')

currPath = os.getcwd()
imagePath = os.path.join(currPath, f'images\subject\{imageList[0]}')

""" Extracting name """
name = imageList[0].split("/")[-1].split(".")[0]

subjectExtractor(imagePath)
watercolourEffect(name)
convertImageBG(f'remove_bg\{name}-watercolor.png', f'remove_bg\{name}-transparent.png')
background_changer(f'remove_bg\{name}-transparent.png', name, pos_w, pos_h, scale)