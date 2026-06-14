import cv2
import numpy as np
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array

# Load your pre-trained model
try:
    model = load_model("face_antispoofing_model.h5")
    print("Model loaded successfully.")
    print(f"Model input shape: {model.input_shape}")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Threshold for classification
threshold = 0.8  # Adjust based on your model performance

# Open the webcam
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to exit the live feed.")

# Set up window
cv2.namedWindow("Live Camera Feed", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Camera Feed", 800, 600)
cv2.setWindowProperty("Live Camera Feed", cv2.WND_PROP_TOPMOST, 1)

# Timer variables
live_start_time = None
live_duration_threshold = 5  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Resize and normalize frame
    resized_frame = cv2.resize(frame, (224, 224))
    image_array = img_to_array(resized_frame)
    image_array = image_array / 255.0

    # Model prediction
    prediction = model.predict(np.expand_dims(image_array, axis=0))[0]
    liveness_score = prediction[0]
    label = "Live Image" if liveness_score <= threshold else "Not Live Image - Spoofed"

    # Handle timer for continuous live detection
    current_time = time.time()
    if label == "Live Image":
        if live_start_time is None:
            live_start_time = current_time
        elif current_time - live_start_time >= live_duration_threshold:
            print("Live face detected continuously for 5 seconds.")
            break
    else:
        live_start_time = None  # Reset if spoofed detected

    # Display prediction
    cv2.putText(
        frame,
        f"{label} (Score: {liveness_score:.2f})",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if label == "Live Image" else (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    cv2.imshow("Live Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

if live_start_time and (time.time() - live_start_time >= live_duration_threshold):
    print("Live face")