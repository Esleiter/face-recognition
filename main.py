import os
import cv2
import face_recognition

directory = "./data/faces/"

known_face_encodings = []
known_face_names = []

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_of_person = face_recognition.load_image_file(os.path.join(directory, filename))
        face_encoding = face_recognition.face_encodings(image_of_person)
        if len(face_encoding) > 0:
            known_face_encodings.append(face_encoding[0])
            known_face_names.append(os.path.splitext(filename)[0])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    frame = cv2.flip(frame, 1)

    face_locations = face_recognition.face_locations(frame, number_of_times_to_upsample=2)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1, (255, 255, 255), 1)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
