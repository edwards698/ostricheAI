import cv2
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images_data_set/")

# Load Camera
webcam = cv2.Videowebcamture(0)  # Choose the Webcam that you want to use starting from 0

# Check if camera is opened successfully
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = webcam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    
    # Annotate frame with detected faces
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    
    # Display frame
    cv2.imshow("Frame", frame)

    # Exit condition (ESC key)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
# Release the camera and close windows
webcam.release()
cv2.destroyAllWindows()
