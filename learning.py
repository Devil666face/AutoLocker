import pickle, face_recognition, os
from threading import Thread
from cv2 import cv2
from datetime import datetime
from database import *

def take_screen_thread():
    thread = Thread(target=take_screen)
    thread.start()

def take_screen():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'screen/{datetime.now()}.jpg', frame)
        if not screen_state():
            cap.release()
            cv2.destroyAllWindows()
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def train_model():
    known_encodings = []
    images = os.listdir("screen")
    for (i, image) in enumerate(images):
        print(f'[+] открытие изображения {i + 1}/{len(images)}')
        face_img = face_recognition.load_image_file(f"screen/{image}")
        try:
            face_enc = face_recognition.face_encodings(face_img)[0]
            if len(known_encodings) == 0:
                known_encodings.append(face_enc)
            else:
                for item in range(0, len(known_encodings)):
                    result = face_recognition.compare_faces([face_enc], known_encodings[item])
                    if result[0]:
                        known_encodings.append(face_enc)
                        print("Один и тот же человек")
                        break
                    else:
                        print("Другой человек")
                        break
        except Exception as ex:
            print("Лицо не распознано")

    data = {
        "encodings": known_encodings
    }
    with open(f"model.pickle", "wb") as file:
        file.write(pickle.dumps(data))


