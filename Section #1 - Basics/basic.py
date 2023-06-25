import cv2 as cv

# Viewing images
img = cv.imread('../Resources/Photos/park.jpg')
# cv.imshow('Park', img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)