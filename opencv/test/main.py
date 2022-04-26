import cv2
from tkinter import filedialog, Tk

root = Tk()
root.withdraw()

filepath = filedialog.askopenfilename()


print("Select Image Flag")
print("1. Color")
print("2. Grayscale")
print("3. Unchange")

flagInput = int(input())

if flagInput == 1:
    flag = 1
elif  flagInput == 2:
    flag = 0
elif flagInput == 3: 
    flag = -1
else: 
    flag = 1


cv2.startWindowThread()
image = cv2.imread(filepath, flag)
windowTitle = "Kleoh"
cv2.imshow( windowTitle , image)
cv2.waitKey(0)
cv2.destroyAllWindows()
