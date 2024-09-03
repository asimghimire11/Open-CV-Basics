import cv2
img1 = cv2.imread("C://Users/Victus/Documents/Images/flower.jpg")
img1 = cv2.resize(img1,(500,500))
img_cropped = img1[50:100,100:400]
cv2.imshow('Cropped Image', img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()