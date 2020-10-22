import cv2
import numpy as np

widthImg = 640
heightImg = 480


cap = cv2.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
cap.set(10,150)



def preprocess(image):
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imBlur = cv2.GaussianBlur(imgGray, (5,5),1)
    imgCanny = cv2.Canny(imgGray, 200, 200)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThresh = cv2.erode(imgDil, kernel, iterations=1)

    return imgThresh


def getContours(img):
    biggest = np.array([])
    maxArea = 0 

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
            
    return biggest


def reorder(points):
    points.reshape((4,2))
    newPoints = np.zeros((4,1,2), np.int32)
    add = points.sum(1)
    newPoints[0] = points[np.argmin(add)]
    newPoints[3] = points[np.argmax(add)]
    diff = np.diff(points, axis=1)
    newPoints[1] = points[np.argmin(diff)]
    newPoints[2] = points[np.argmax(diff)]

    return newPoints


def getWarped(img, biggest):
    biggest = reorder(biggest)
    point1 = np.float32(biggest)
    point2 = np.float32([[0,0], [widthImg, 0], [heightImg, 0], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(point1, point2)
    warped = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    return warped


while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgContour = img.copy()
    imgThresh = preprocess(img)
    getContours(imgThresh)
    cv2.imshow('Image', imgContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elif cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite("C:\\Users\\lm44\\Documents\\Data\\image1.jpg", imgContour)
        break 