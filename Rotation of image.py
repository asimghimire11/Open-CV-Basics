import cv2
img = cv2.imread("C://Users/Victus/Documents/Images/tree.jpg")
img = cv2.resize(img,(500,500))
img_90c = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('Original Image', img)
cv2.imshow('90 Degree Counter Clockwise', img_90c)
cv2.imshow('90 Degree Clockwise', img_90)
cv2.imshow('108 Degree', img_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
