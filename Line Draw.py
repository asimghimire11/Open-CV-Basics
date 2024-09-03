import cv2
img1 = cv2.imread("C://Users/Victus/Documents/Images/bird.jpg")
img1 = cv2.resize(img1,(500,500))
h = img1.shape[0]
w = img1.shape[1]
img1 = cv2.line(img1,(0,0),(h,w),(0,0,255),10)
img1 = cv2.line(img1,(w,0),(0,h),(0,0,255),10)
cv2.imshow("Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()