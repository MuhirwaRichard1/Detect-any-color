import cv2
import numpy as np


cap = cv2.VideoCapture(0)  #load the camera (ex: pi cam or webcam
#Open your camera (process)

def empty(a):
    pass
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640,240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV",179,179, empty)
cv2.createTrackbar("SAT Min", "HSV",0,255, empty)
cv2.createTrackbar("SAT Max", "HSV",255,255, empty)
cv2.createTrackbar("VALUE Min", "HSV",0,255, empty)
cv2.createTrackbar("VALUE Max", "HSV",255,255, empty)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    higher = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, higher)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #cv2.imshow("hsv color", hsv)
    cv2.imshow("Frame", frame)
    cv2.imshow("mMsk", mask)
    cv2.imshow("Result", result)
    key = cv2.waitKey(1)

    if key == 27:   #27 is equal to the Esc key on keyboard
        break

cap.release()
cv2.destroyAllWindows()