import cv2
img1 = cv2.imread("C://Users/Victus/Documents/Images/bird.jpg")
img1 = cv2.resize(img1,(500,500))
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img1,"Bird", (200,400), font, 2, (0, 255, 255))
cv2.imshow('Text in Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()