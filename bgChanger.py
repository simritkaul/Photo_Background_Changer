import os
import cv2
import cvzone
from inputValidity import validInput

def background_changer(subjectPath, name, pos_w, pos_h, scale):

    bgList = os.listdir('images/background/')

    ''' The background '''
    for bgs in bgList:
        bg_image = cv2.imread(f'images/background/{bgs}', cv2.IMREAD_COLOR)
        bg_h, bg_w, _ = bg_image.shape
        bg_name = bgs.split(".")[0]
        subject_image = cv2.imread(subjectPath, cv2.IMREAD_UNCHANGED)
        sub_h, sub_w, _ = subject_image.shape

        os.remove(subjectPath)
        
        valid = validInput(pos_w, pos_h, scale, bg_w, bg_h, sub_w, sub_h)

        if not valid:
            print('Invalid Input! Default parameters applied.')
            ratio = round(bg_h / sub_h)
            if ratio > 4 or ratio < 2:
                scaling = round((bg_h/2)/sub_h, 1)
                subject_image = cv2.resize(subject_image, None, fx= scaling, fy= scaling, interpolation= cv2.INTER_LINEAR)
                sub_h, sub_w, _ = subject_image.shape
            res = cvzone.overlayPNG(bg_image, subject_image, [bg_w - sub_w, bg_h - sub_h])
            cv2.imwrite(f'remove_bg/{name}-{bg_name}.png', res)
            print('Background change done')

        else:
            print('Preparing image with the input parameters.')
            sub_hnew = int(sub_h * scale)
            sub_wnew = int(sub_w * scale)
            new_dim = (sub_wnew, sub_hnew)
            # scaling = round(sub_hnew/sub_h, 1)
            subject_image = cv2.resize(subject_image, new_dim, interpolation= cv2.INTER_LINEAR)
            res = cvzone.overlayPNG(bg_image, subject_image, [pos_w, pos_h])
            cv2.imwrite(f'remove_bg/{name}-{bg_name}.png', res)
            print('Background change done')