'''#import face_recognition
import cv2
import numpy as np

import time
import os


video_capture = cv2.VideoCapture(0)

#root_image = face_recognition.load_image_file("1244.png")
#root_encoding = face_recognition.face_encodings(root_image)[0]


known_face_encodings = [
    root_encoding,
]
known_face_names = [
    "san",
]

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    name = "Unknown"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    if name != "san":
        print('unknow')

    else:
        print("Welcome BOSS")
        os.system("gnome-terminal")

    # Display the resulting image
    cv2.imshow('Video', frame)


# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()'''




import face_recognition
import cv2
import time
import numpy as np
cap = cv2.VideoCapture('21423534.mp4')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))


# Load some sample pictures and learn how to recognize them.
female_image = face_recognition.load_image_file("WhatsApp.jpeg")
female_face_encoding = face_recognition.face_encodings(female_image)[0]


known_faces = [
    female_face_encoding

]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0




IMG_SIZE = 200
frame_rate = 5
#delay = int(1000 / frame_rate)
while True:
    # Capture the video frame
    ret, frame = cap.read()
    #frame = cv2.rotate(frame)

    #ret, frame = input_video.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "person1"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file

    cv2.imshow("Output", frame)

    # cv2.imshow("Cropped", cropped)
    # cv2.imshow("orginal", frame)
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
