import cv2

img = cv2.imread("images/board.png")

thresh_upper = 90
thresh_lower = 45
canny = cv2.Canny(img, thresh_lower, thresh_upper)

win_name = "Carambole"
cv2.namedWindow(win_name)

cv2.imshow(win_name, canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
