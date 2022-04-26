import cv2
filepath = 'red.jpg'
windowTitle = 'Kleoh'
readCvImage = cv2.imread(filepath,1)
cv2.imshow( windowTitle , readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
