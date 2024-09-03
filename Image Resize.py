import cv2
img = cv2.imread("C://Users//Victus//Documents//Images//bird.jpg")
img = cv2.resize(img,(500,500))#resizing the image in terms of the x and y axis
cv2.imwrite("C://Users//Victus//Documents//Images//birdnew.jpg",img)
# img = cv2.resize(img, (0,0),fx=0.1,fy=0.08) #resizing the image in terms of the pixel values
cv2.imshow('Image Window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()