import cv2
img = cv2.imread("C://Users/Victus/Documents/Images/bird.jpg",)
img = cv2.resize(img,(500,500))
img_gr = cv2.cvtColor(img,cv2.CV_64F)
cv2.imshow("Original Image", img)
cv2.imshow("Color Changed Image",img_gr)
cv2.waitKey(0)
cv2.destroyAllWindows()
