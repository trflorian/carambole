import cv2

img = cv2.imread("images/board.png")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

thresh_upper = 50
thresh_lower = 30
canny = cv2.Canny(img, thresh_lower, thresh_upper)

contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
contours = [contours[0]]
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

win_name = "Carambole"
cv2.namedWindow(win_name)

cv2.imshow(win_name, img)
cv2.waitKey(0)

cv2.destroyAllWindows()
