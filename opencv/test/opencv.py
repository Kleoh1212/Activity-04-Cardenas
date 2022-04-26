import cv2
filepath = 'red.jpg'
image = cv2.imread(filepath, 1)
cv2.imshow("Kleoh", image)
cv2.waitKey(0)
cv2.destroyAllWindows()