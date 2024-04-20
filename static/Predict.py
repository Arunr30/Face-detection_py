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
cap = cv2.VideoCapture('123.mp4')

root_image = face_recognition.load_image_file("static/upload/1234.jpg")
root_encoding = face_recognition.face_encodings(root_image)[0]


known_face_encodings = [
    root_encoding,
]
known_face_names = [
    "san",
]

IMG_SIZE = 200
frame_rate = 15
delay = int(1000 / frame_rate)
while True:
    # Capture the video frame
    ret, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

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
        #os.system("gnome-terminal")

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
