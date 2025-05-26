import numpy as np
import cv2

# Capture the generated video
cap = cv2.VideoCapture("processed_data/GOT-10k_Test_000001.avi")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
