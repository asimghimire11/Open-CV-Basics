import cv2
img1 = cv2.imread("C://Users/Victus/Documents/Images/tree.jpg")
img1 = cv2.resize(img1, (600,600))
img2 = cv2.imread("C://Users/Victus/Documents/Images/bird.jpg")
img2 = cv2.resize(img2, (600,600))
img3 = cv2.imread("C://Users/Victus/Documents/Images/flower.jpg")
img3 = cv2.resize(img3, (600,600))
img_merged = cv2.add(img1,img2,img3)

cv2.imshow("Merged Image",img_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()



