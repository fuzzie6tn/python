import cv2
import mediapipe as mp

# Initialize MediaPipe face detection and drawing modules
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Initialize the camera
cap = cv2.VideoCapture(0)

# Start face detection
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            break

        # Convert the image to RGB because mediapipe requires RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform face detection
        results = face_detection.process(rgb_frame)

        # Draw face detections
        if results.detections:
            for detection in results.detections:
                # Draw the bounding box around the face
                mp_drawing.draw_detection(frame, detection)

                # Extract and print facial key points
                bboxC = detection.location_data.relative_bounding_box
                key_points = detection.location_data.relative_keypoints
                print(f"Face detected at [{bboxC.xmin}, {bboxC.ymin}], "
                      f"Width: {bboxC.width}, Height: {bboxC.height}")

                # Extract and print key features
                left_eye = key_points[0]
                right_eye = key_points[1]
                nose_tip = key_points[2]
                mouth_center = key_points[3]

                print(f"Left Eye: ({left_eye.x}, {left_eye.y})")
                print(f"Right Eye: ({right_eye.x}, {right_eye.y})")
                print(f"Nose Tip: ({nose_tip.x}, {nose_tip.y})")
                print(f"Mouth Center: ({mouth_center.x}, {mouth_center.y})")

        # Display the resulting frame
        cv2.imshow('Face Detection', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
