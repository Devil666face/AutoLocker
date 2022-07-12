import face_recognition,pickle, schedule
from datetime import datetime
from cv2 import cv2
from control import lock_system
from threading import Thread
from database import *
from unlocker import *

def take_reco_thread():
    thread = Thread(target=start_detection)
    thread.start()

def get_params_for_recogn(frame):
    locations = face_recognition.face_locations(frame, model="cnn")
    encodings = face_recognition.face_encodings(frame, locations)
    return locations,encodings

def detect_person():
    data = pickle.loads(open("model.pickle","rb").read())
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        locations,encodings = get_params_for_recogn(frame)
        if (len(locations)>0):
            for face_encoding, face_location in zip(encodings,locations):
                result = face_recognition.compare_faces(data["encodings"],face_encoding)
                if not True in result:
                    lock_system()
                    cv2.imwrite(f'no_success/{datetime.now()}.jpg',frame)
                    update_detect_state(False)

                    update_unlock_state(True)
                    take_unlock_thread()
    cap.release()
    cv2.destroyAllWindows()
    del cap

def start_detection():
    schedule.every(5).seconds.do(detect_person)
    while True:
        schedule.run_pending()
        if not detect_state():
            break