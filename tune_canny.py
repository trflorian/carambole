import cv2

img = cv2.imread("images/board.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

otsu_thresh, _ = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh_upper = int(otsu_thresh)
thresh_lower = int(otsu_thresh / 2)

win_name = "Canny Edge Detection"
cv2.namedWindow(win_name)

tb_thresh_lower = "Threshold Lower"
tb_thresh_upper = "Threshold Upper"
cv2.createTrackbar(tb_thresh_lower, win_name, thresh_lower, 255, lambda x: None)
cv2.createTrackbar(tb_thresh_upper, win_name, thresh_upper, 255, lambda x: None)

while True:
    thresh_lower = cv2.getTrackbarPos(tb_thresh_lower, win_name)
    thresh_upper = cv2.getTrackbarPos(tb_thresh_upper, win_name)
    canny = cv2.Canny(img, thresh_lower, thresh_upper)

    cv2.imshow(win_name, canny)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
