import cv2
img1 = cv2.imread("C://Users/Victus/Documents/Images/flower.jpg")
img1 = cv2.resize(img1,(500,500))
cv2.circle(img1,(290,330),100,(0,255,255),5)
cv2.imshow('Circle in Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()