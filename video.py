import cv2
import os
from nudenet import NudeDetector

# Initialize the NudeDetector
nude_detector = NudeDetector()
detections = nude_detector.detect("totalnude.jpg")

# Print the list of detections
print(detections)
# Open the video file
video_path = "virtualorgy2.mov"
cap = cv2.VideoCapture(video_path)

# Read and process each frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Save the frame as an image file
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame_rgb)

    # Detect nudity in the image file
    detections = nude_detector.detect(temp_image_path)

    # Process the detections (e.g., count number of detections)
    num_nudity = len(detections)

    # Perform actions based on the number of detections (e.g., flag the video if nudity is detected)
    if num_nudity > 0:
        print("Nudity detected in frame!")
        break
    else:
        print("No nudity found")
        break

    # # Display the frame (optional)
    # cv2.imshow('Frame', frame)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break

    # # Delete the temporary image file
    # os.remove(temp_image_path)

# Release the video capture object and close any open windows
cap.release()
# cv2.destroyAllWindows()
