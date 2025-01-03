import cv2
import numpy as np

# Read and convert image to HSV
img = cv2.imread("images/board.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a window for the trackbars
win_name = "HSV Thresholding"
cv2.namedWindow(win_name)

# Initial trackbar values for H, S, V
# Hue range is [0..179], Saturation and Value are [0..255] in OpenCV
h_min, s_min, v_min = 5, 50, 50
h_max, s_max, v_max = 30, 255, 255

# Trackbar names
tb_h_min = "Hue Min"
tb_h_max = "Hue Max"
tb_s_min = "Sat Min"
tb_s_max = "Sat Max"
tb_v_min = "Val Min"
tb_v_max = "Val Max"

# Create trackbars
cv2.createTrackbar(tb_h_min, win_name, h_min, 179, lambda x: None)
cv2.createTrackbar(tb_h_max, win_name, h_max, 179, lambda x: None)
cv2.createTrackbar(tb_s_min, win_name, s_min, 255, lambda x: None)
cv2.createTrackbar(tb_s_max, win_name, s_max, 255, lambda x: None)
cv2.createTrackbar(tb_v_min, win_name, v_min, 255, lambda x: None)
cv2.createTrackbar(tb_v_max, win_name, v_max, 255, lambda x: None)

while True:
    # Read the current positions of the trackbars
    h_min = cv2.getTrackbarPos(tb_h_min, win_name)
    h_max = cv2.getTrackbarPos(tb_h_max, win_name)
    s_min = cv2.getTrackbarPos(tb_s_min, win_name)
    s_max = cv2.getTrackbarPos(tb_s_max, win_name)
    v_min = cv2.getTrackbarPos(tb_v_min, win_name)
    v_max = cv2.getTrackbarPos(tb_v_max, win_name)

    # Build the lower and upper bound arrays
    lower = np.array([h_min, s_min, v_min], dtype=np.uint8)
    upper = np.array([h_max, s_max, v_max], dtype=np.uint8)

    # Threshold in HSV space
    mask = cv2.inRange(hsv, lower, upper)

    # Optionally, show the filtered image by applying the mask
    filtered = cv2.bitwise_and(img, img, mask=mask)

    # Show windows
    cv2.imshow("Mask", mask)
    cv2.imshow(win_name, filtered)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
