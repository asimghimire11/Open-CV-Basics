from tkinter import *
import tkinter.simpledialog
import cv2
def displayImage():
    img1 = cv2.imread("C://Users/Victus/Documents/Images/flower.jpg")
    cv2.imshow('Image',img1)
def resizeImage():
    img1 = cv2.imread("C://Users/Victus/Documents/Images/flower.jpg")
    x = tkinter.simpledialog.askinteger("Width", "Enter Width: ")
    y = tkinter.simpledialog.askinteger("Height", "Enter Height: ")
    img1 = cv2.resize(img1,(x,y))
    cv2.imshow('Image', img1)

myRoot = Tk()
myRoot.title = 'Dynamic Resizing'
myRoot.minsize(500,500)
myRoot.maxsize(500,500)

btn1 = Button(text="Display Image",font=('Arial', 10, 'bold'), command=displayImage)
btn1.grid(row=0,column=0)

btn2 = Button(text="Resize Image",font=('Arial', 10, 'bold'), command=resizeImage)
btn2.grid(row=0,column=4)

cv2.waitKey(0)
cv2.destroyAllWindows()

myRoot.mainloop()