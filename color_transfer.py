# To run: python3 color_transfer.py

import cv2
import numpy as np
import sys
# import argparse

def convert_color_space_BGR_to_RGB(img_BGR):
    img_RGB = np.zeros_like(img_BGR,dtype=np.float32)
    # to be completed ...
    return img_RGB

def convert_color_space_RGB_to_BGR(img_RGB):
    img_BGR = np.zeros_like(img_RGB,dtype=np.float32)
    # to be completed ...
    return img_BGR

def convert_color_space_RGB_to_Lab(img_RGB):
    '''
    convert image color space RGB to Lab
    '''
    img_LMS = np.zeros_like(img_RGB,dtype=np.float32)
    # to be completed ...

    img_Lab = np.zeros_like(img_RGB,dtype=np.float32)
    # to be completed ...
    return img_Lab

def convert_color_space_Lab_to_RGB(img_Lab):
    '''
    convert image color space Lab to RGB
    '''
    img_LMS = np.zeros_like(img_Lab,dtype=np.float32)
    # to be completed ...
    img_RGB = np.zeros_like(img_Lab,dtype=np.float32)
    # to be completed ...

    return img_RGB

def convert_color_space_RGB_to_CIECAM97s(img_RGB):
    '''
    convert image color space RGB to CIECAM97s
    '''
    img_CIECAM97s = np.zeros_like(img_RGB,dtype=np.float32)
    # to be completed ...

    return img_CIECAM97s

def convert_color_space_CIECAM97s_to_RGB(img_CIECAM97s):
    '''
    convert image color space CIECAM97s to RGB
    '''
    img_RGB = np.zeros_like(img_CIECAM97s,dtype=np.float32)
    # to be completed ...

    return img_RGB


def color_transfer_in_Lab(img_RGB_source, img_RGB_target):
    print('===== color_transfer_in_Lab =====')

    m1 = np.array([(0.3811, 0.5783, 0.0402), (0.1967, 0.7244, 0.0782), (0.0241, 0.1288, 0.8444)])

    a = [[ 0.57735026919, 0, 0], # 1/sqrt(3)
        [ 0, 0.40824829046, 0], # 1/sqrt(6)
        [ 0, 0, 0.70710678118]] # 1/sqrt(2)
    b = [[ 1, 1, 1],
        [ 1, 1,-2],
        [ 1,-1, 0]]

    lms_source = np.matmul(img_RGB_source, m1)
    lms_target = np.matmul(img_RGB_target, m1)

    lab_source = np.matmul(lms_source, np.matmul(a, b))
    lab_target = np.matmul(lms_target, np.matmul(a, b))

    ## color processing to LAB here...



def color_transfer_in_RGB(img_RGB_source, img_RGB_target):
    print('===== color_transfer_in_RGB =====')
    # to be completed ...

def color_transfer_in_CIECAM97s(img_RGB_source, img_RGB_target):
    print('===== color_transfer_in_CIECAM97s =====')
    # to be completed ...

def color_transfer(img_RGB_source, img_RGB_target, option):
    if option == 'in_RGB':
        img_RGB_new = color_transfer_in_RGB(img_RGB_source, img_RGB_target)
    elif option == 'in_Lab':
        img_RGB_new = color_transfer_in_Lab(img_RGB_source, img_RGB_target)
    elif option == 'in_CIECAM97s':
        img_RGB_new = color_transfer_in_CIECAM97s(img_RGB_source, img_RGB_target)
    return img_RGB_new

def rmse(apath,bpath):
    """
    This is the help function to get RMSE score.
    apath: path to your result
    bpath: path to our reference image
    when saving your result to disk, please clip it to 0,255:
    .clip(0.0, 255.0).astype(np.uint8))
    """
    a = cv2.imread(apath).astype(np.float32)
    b = cv2.imread(bpath).astype(np.float32)
    print(np.sqrt(np.mean((a-b)**2)))


if __name__ == "__main__":
    print('==================================================')
    print('PSU CS 410/510, Winter 2022, HW1: color transfer')
    print('==================================================')


    # path_file_image_source = sys.argv[1]
    # path_file_image_target = sys.argv[2]
    # path_file_image_result_in_Lab = sys.argv[3]
    # path_file_image_result_in_RGB = sys.argv[4]
    # path_file_image_result_in_CIECAM97s = sys.argv[5]

    # Use following if you want to use below code -> python3 color_transfer.py --image IMAGE_NAME_HERE.wtvr
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required=True, help="path to input image")
    # args = vars(ap.parse_args())
    # img_RGB_source = cv2.imread(args["image"])

    path_file_image_source = 'source1.png'
    path_file_image_target = 'target1.png'

    # [:, :, ::-1] is used to convert BGR to the necessary RGB color space
    img_RGB_source = cv2.imread(path_file_image_source)[:, :, ::-1] 
    img_RGB_target = cv2.imread(path_file_image_target)[:, :, ::-1] 

    print(img_RGB_source.shape) # (height, width, channels) = (599, 800, 3)
    # print(np.moveaxis(img_RGB_source, 0)

    cv2.imshow("image", img_RGB_source)
    cv2.waitKey(0)

    # ===== read input images
    # img_RGB_source: is the image you want to change its color
    # img_RGB_target: is the image containing the color distribution that you want to change the img_RGB_source to (transfer color of the img_RGB_target to the img_RGB_source)

    # converts TO lab color space
    img_RGB_new_Lab       = color_transfer(img_RGB_source, img_RGB_target, option='in_Lab')
    # todo: save image to path_file_image_result_in_Lab

    # img_RGB_new_RGB       = color_transfer(img_RGB_source, img_RGB_target, option='in_RGB')
    # todo: save image to path_file_image_result_in_RGB

    # img_RGB_new_CIECAM97s = color_transfer(img_RGB_source, img_RGB_target, option='in_CIECAM97s')
    # todo: save image to path_file_image_result_in_CIECAM97s
