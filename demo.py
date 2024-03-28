from nudenet import NudeDetector

# Initialize the NudeDetector
nude_detector = NudeDetector()

# Detect nudity in an image
image_path = 'img.png'
detections = nude_detector.detect(image_path)

# Print the detections
print(detections)
