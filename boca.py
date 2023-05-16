import cv2
import dlib

# Load the pre-trained model for facial point detection
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the face detector from dlib
detector = dlib.get_frontal_face_detector()

# Initialize the video capture from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the current frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Detect facial points
        landmarks = predictor(gray, face)

        # Extract the coordinates of the mouth points
        mouth_points = []
        for n in range(48, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            mouth_points.append((x, y))

        # Calculate the vertical distance between the mouth points
        mouth_height = abs(mouth_points[2][1] - mouth_points[10][1])

        # Set a threshold value
        threshold = 23  # adjust this value based on your observations

        # Check if the mouth is open or closed
        if mouth_height > threshold:
            status = "Aberta"
        else:
            status = "Fechada"

        # Draw the outline of the mouth
        for i in range(0, len(mouth_points) - 1):
            cv2.line(frame, mouth_points[i], mouth_points[i + 1], (0, 255, 0), 2)
        cv2.line(frame, mouth_points[len(mouth_points) - 1], mouth_points[0], (0, 255, 0), 2)

        # Write the status of the mouth on the frame
        cv2.putText(frame, f"Mouth: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show the resulting frame
    cv2.imshow('Mouth Detection', frame)

    # Stop the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources used
cap.release()
cv2.destroyAllWindows()
