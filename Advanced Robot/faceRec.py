import winsound
import datetime
import pyttsx3
import face_recognition
import numpy as np
import sys
import cv2
from threading import Thread

################################################################################################
##################################### System logger ############################################
################################################################################################
def log_system(text):
    with open('logs/system.log', 'a+') as LOG:
        ctime = "[" + str(datetime.datetime.now()) + "]" + " " + text
        LOG.write(ctime)
        LOG.write('\n')
        LOG.close()


################################################################################################
################################## Check the uername ###########################################
################################################################################################
def check_name():
    try:
        with open('user/user.txt', 'r') as namefile:
            Name = namefile.read()
            namefile.close()
        return Name
    except Exception:
        return Name

################################################################################################
#################################### Talk function #############################################
################################################################################################
def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print(text, end="\r")
    engine.say(text)
    engine.runAndWait()

################################################################################################
################################# Main class of faceRe #########################################
################################################################################################
class RecognizeUserFace:

    def con(self):
        winsound.Beep(1500, 300)
        video_capture = cv2.VideoCapture(0)
        user_image = face_recognition.load_image_file("pics/ID.jpg")
        user_face_encodings = face_recognition.face_encodings(user_image)[0]
        known_face_encodings = [
            user_face_encodings
        ]
        name_ = check_name()
        known_face_names = [
            name_
        ]
        for i in range(5):
            try:
                ret, frame = video_capture.read()

                rgb_frame = frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                    name = "Random Person"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]

                    if (name != "Random Person"):
                        winsound.Beep(1600, 300)
                        talk(f"Welcome {name_}")
                        return name_
                    else:
                        winsound.Beep(1600, 300)
                        print(f"Atempt {i} Couldn't recognize the face.", end="\r")
                        if i == 5:
                            return "randonperson"
                        pass


                # if cv2.waitKey(1) & 0xFF == ord('q'):
                    # break
            except Exception as e:
                print(e)
                print("an error occurred while recognizing the face.", end="\r")
                pass
