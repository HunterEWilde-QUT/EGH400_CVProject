import numpy as np
import cv2 as cv

# Capture the generated video
cap = cv.VideoCapture("processed_data/GOT-10k_Test_000001.avi")

# Define the tracking window
_, frame = cap.read()
bbox = cv.selectROI("select", frame, False)
x, y, w, h = bbox

roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

# Track objects in the captured video
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Alter the frame's colours to aid in detection
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # Move the tracking window
        ret, track_window = cv.meanShift(dst, bbox, term_crit)
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

        # Display the resulting frame
        cv.imshow('frame',frame)

        # Quit the program
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
