import cv2 as cv
import cv2
import numpy as np
import pytesseract
# import utlis
import time
import threading
# import sys

import os
start = time.time()

def imageFunc(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = cv.imread(img)
    # image =cv.imread('img/Image/xga 3.jpg')
    # image = cv.imread('img/ICUmonitor/capture 3.jpg')
    # image = cv.imread('img/different/dislplay1.jpg')


    widthImg = 800
    heightImg = 400
    image = cv2.resize(image, (widthImg, heightImg))
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # cv.imshow('hsv',hsv)
############## GREEN ##############

# lower_green = np.array([30,75,120])
# upper_green = np.array([70,255,255])

    lower_green = np.array([30, 50, 150])
    upper_green = np.array([75, 255, 255])

    mask_green = cv.inRange(hsv, lower_green, upper_green)
    # cv.imshow("maskgreen",mask_green)

    result_green = cv.bitwise_and(image, image, mask=mask_green)
    # cv.imshow("resultGreen",result_green)

    grey = cv.cvtColor(result_green, cv.COLOR_BGR2GRAY)
    ret, threshold_green = cv.threshold(grey, 1, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(threshold_green, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv.contourArea(cnt) <= 200:
            cv.drawContours(threshold_green, [cnt], -1, 255, -1)
# text = pytesseract.image_to_string(threshold_green)
# print(text)
# cv.imshow('threshold',removed_green)

# cv.imshow('re',mask_green)
    g_color = threshold_green
# cv.imshow('green',threshold_green)


############## BLUE ##############

# lower_blue = np.array([70,20,170])
# upper_blue = np.array([95,255,255])
    lower_blue = np.array([75, 30, 180])
    upper_blue = np.array([100, 255, 255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    result_blue = cv.bitwise_and(image, image, mask=mask_blue)
    grey = cv.cvtColor(result_blue, cv.COLOR_BGR2GRAY)
    ret, threshold_blue = cv.threshold(grey, 1, 255, cv.THRESH_BINARY_INV)
    # cv.imshow('th',threshold_blue)
    contours1, hierarchy1 = cv.findContours(threshold_blue, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours1:
        if cv.contourArea(cnt) <= 300:
            cv.drawContours(threshold_blue, [cnt], -1, 255, -1)
    # cv.imshow('b',threshold_blue)
    kernel = np.ones((5, 5), np.uint8)
    # erosion = cv.dilate(threshold_blue, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)),3)
    opening = cv2.morphologyEx(threshold_blue, cv2.MORPH_OPEN, kernel)
    erosion = cv.dilate(opening, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), 3)
    # text1 = pytesseract.image_to_string(erosion,config='--oem 3 --psm 11 outputbase digits')
    # print(text1)
    # cv.imshow('threshoald',threshold_blue)
    b_color = erosion
    # cv.imshow('threshoalasdd',erosion)

    res = cv2.bitwise_and(g_color, g_color, mask=b_color)

    text = pytesseract.image_to_string(res, config='--oem 3 --psm 11 outputbase digits').split()
    # print(text)
    cv.waitKey(0)

    if len(text)>=2:
        finalText = []
        for i in range(len(text)):
            if text[i].isdigit() == True:
                finalText.append(text[i])
        if len(finalText) >= 2:
            HR = int((finalText[0]))
            spo2 = int((finalText[1]))
        else:
            HR = 'None'
            spo2 = ''

        ######## For python 3 ##########
        # print('Heart Rate=',finalText[0])
        # print('Oxygen Saturation=', finalText[1])


        ######### For python 2 & python 3 #########
        # print('Heart Rate = '+finalText[0])
        # print('Oxygen Saturation = '+ finalText[1])
        # HR= (finalText[0])
        # spo2=(finalText[1])

    else:
        HR= 'None'
        spo2=''

    return HR,spo2
        # print("Image isn't clear")
# # end1 = time.time()
image = os.listdir('static/imagesForData')
image = ['imagesForData/' + file for file in image]
Data = []
for singleImage in image:
    name = 'static/'+singleImage
    if cv.haveImageReader(name)==True:
        data = imageFunc(name)
        Data.append(data)
    else:
        data =('None','')
        Data.append(data)
print (Data)
# end = time.time()
# print(end-start)
# print(Data)
# cv.imshow('res', res)
# print(imageFunc('./static/images/res0.jpg')[0])
# time.sleep(10)


# cv.waitKey(0)
