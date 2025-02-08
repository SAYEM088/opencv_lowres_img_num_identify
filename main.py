import cv2
import numpy as np

image_path = r"D:\RR246\ocr\opencv-testkit\img2.JPG"
image = cv2.imread(image_path)
image =cv2.resize(image,(500,500))
width, height = (280, 280)
srcImg = np.float32([[100, 50], [460, 50], [100, 460], [460, 460]])
destinationImg = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
mask = cv2.getPerspectiveTransform(srcImg, destinationImg)
new_img = cv2.warpPerspective(image, mask, (width, height))
gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 31, 2)
kernel = np.ones((2, 2), np.uint8)
processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Processed Image", processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
