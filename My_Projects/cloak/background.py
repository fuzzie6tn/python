import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

# Ensure the webcam is working
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

# Give some time for the camera to start
import time
time.sleep(2)

# Capture the background frame
ret, background = cap.read()
if not ret or background is None:
    print("Error: Could not read frame from webcam")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Flip the background image
background = np.flip(background, axis=1)

# Save the background image
cv2.imwrite("image.jpg", background)

# Release resources
cap.release()
cv2.destroyAllWindows()
