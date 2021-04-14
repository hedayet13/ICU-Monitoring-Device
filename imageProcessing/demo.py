import cv2 as cv
import cv2
import numpy as np
import pytesseract
# import utlis
import time

# import sys


start = time.time()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# image = cv.imread('img/general/res2.jpg')
# image =cv.imread('img/Image/xga 3.jpg')
image = cv.imread('img/3rdres/res8.jpg')


# cv.imshow('ima',image)
############## Angled #################
def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100000:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area


def drawRectangle(img, biggest, thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)

    return img


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    return myPointsNew


count = 0
widthImg = 800
heightImg = 600
img = cv2.resize(image, (widthImg, heightImg))
# imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv.imwrite("grey.jpg",imgGray)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
cv.imwrite('blur.jpg',imgBlur)
imgThreshold = cv2.Canny(imgBlur, 100, 100)
cv.imwrite('canny.jpg',imgThreshold)
kernel = np.ones((5, 5))
imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)
cv.imwrite('dilate.jpg',imgBlur)
imgThreshold = cv2.erode(imgDial, kernel, iterations=1)
imgContours = img.copy()
imgBigContour = img.copy()
contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10)
biggest, maxArea = biggestContour(contours)
if biggest.size != 0:
    biggest = reorder(biggest)
    cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20)
    imgBigContour = drawRectangle(imgBigContour, biggest, 2)
    pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    image = imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    # REMOVE 20 PIXELS FORM EACH SIDE
    imgWarpColored = imgWarpColored[0:imgWarpColored.shape[0], 0:imgWarpColored.shape[1]]
    img2 = imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))
    # APPLY ADAPTIVE THRESHOLD
    # imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    # cv.imshow('venti',imgWarpColored)
    # cv.waitKey(0)

# image = cv.imread('img/Image/svga 2.jpg')
# image = cv.imread('img/ICUmonitor/capture .jpg')
# image = cv.blur(image,(3,3))

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
# cv.imwrite('hsv.jpg',hsv)
# cv.imwrite('hsvImage.jpg',hsv)

############## GREEN ##############

# lower_green = np.array([30,75,120])
# upper_green = np.array([70,255,255])

lower_green = np.array([30, 50, 150])
upper_green = np.array([75, 255, 255])

mask_green = cv.inRange(hsv, lower_green, upper_green)
# cv.imwrite('maskGreen.jpg',mask_green)
result_green = cv.bitwise_and(image, image, mask=mask_green)
# cv.imwrite('resultGreen.jpg',result_green)
grey = cv.cvtColor(result_green, cv.COLOR_BGR2GRAY)
ret, threshold_green = cv.threshold(grey, 1, 255, cv.THRESH_BINARY_INV)
# cv.imwrite('BinaryConversion.jpg',threshold_green)
contours, hierarchy = cv.findContours(threshold_green, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv.contourArea(cnt) <= 200:
        cv.drawContours(threshold_green, [cnt], -1, 255, -1)
# text = pytesseract.image_to_string(threshold_green)
# print(text)
# cv.imshow('threshold',removed_green)

# cv.imshow('re',mask_green)
g_color = threshold_green
# cv.imwrite('green.jpg',threshold_green)


############## BLUE ##############

# lower_blue = np.array([70,20,170])
# upper_blue = np.array([95,255,255])
lower_blue = np.array([75, 30, 180])
upper_blue = np.array([100, 255, 255])

mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
# cv.imwrite('maskBlue.jpg',mask_blue)
result_blue = cv.bitwise_and(image, image, mask=mask_blue)
# cv.imwrite('resultBlue.jpg',result_blue)
grey = cv.cvtColor(result_blue, cv.COLOR_BGR2GRAY)
ret, threshold_blue = cv.threshold(grey, 1, 255, cv.THRESH_BINARY_INV)
# cv.imwrite('binaryInversion.jpg',threshold_blue)
# cv.imshow('th',threshold_blue)
contours1, hierarchy1 = cv.findContours(threshold_blue, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours1:
    if cv.contourArea(cnt) <= 300:
        cv.drawContours(threshold_blue, [cnt], -1, 255, -1)
# cv.imwrite('removed small pixel.jpg',threshold_blue)
kernel = np.ones((5, 5), np.uint8)
# erosion = cv.dilate(threshold_blue, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)),3)
opening = cv2.morphologyEx(threshold_blue, cv2.MORPH_OPEN, kernel)
erosion = cv.dilate(opening, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), 3)
# text1 = pytesseract.image_to_string(erosion,config='--oem 3 --psm 11 outputbase digits')
# print(text1)
# cv.imshow('threshoald',threshold_blue)
b_color = erosion
# cv.imwrite('blue.jpg',erosion)

res = cv2.bitwise_and(g_color, g_color, mask=b_color)


text = pytesseract.image_to_string(res, config='--oem 3 --psm 11 outputbase digits').split()
# print(text)

if len(text)>=2:
    finalText = []
    for i in range(len(text)):
        if text[i].isdigit() == True:
            finalText.append(text[i])


    ######## For python 3 ##########
    # print('Heart Rate=',finalText[0])
    # print('Oxygen Saturation=', finalText[1])


    ######### For python 2 & python 3 #########
    print('Heart Rate = '+finalText[0])
    print('Oxygen Saturation = '+ finalText[1])
else:
    print("Image isn't clear")

end = time.time()

print(end - start)

# cv.imwrite('finalImage.jpg', res)

cv.waitKey(0)
