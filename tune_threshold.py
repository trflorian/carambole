import cv2

img = cv2.imread("images/board.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

otsu_thresh, img_thresh = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
otsu_thresh = int(otsu_thresh)

win_name = "Threshold"
cv2.namedWindow(win_name)

tb_thresh = "Threshold"
cv2.createTrackbar(tb_thresh, win_name, otsu_thresh, 255, lambda x: None)

while True:
    thresh = cv2.getTrackbarPos(tb_thresh, win_name)

    img_thresh = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]

    img_annot = img.copy()
    contours, _ = cv2.findContours(
        img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    if len(contours) > 0:
        contours = contours[: min(len(contours), 5)]
    cv2.drawContours(img_annot, contours, -1, (0, 255, 0), 1)

    cv2.imshow(win_name, img_annot)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
