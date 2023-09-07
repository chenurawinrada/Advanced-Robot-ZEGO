import cv2

################################################################################################
#################################### Talk function #############################################
################################################################################################
def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print(text)
    engine.say(text)
    engine.runAndWait()


################################################################################################
################################## Main class of tcpic #########################################
################################################################################################
class TakePicID:
    def PICID(self):
        cam = cv2.VideoCapture(0)
        s, img = cam.read()
        if s:
            cv2.imwrite("pics/ID.jpg", img)
            pass

    def PICNAME(self):
        try:
            Name = input("How may I call you?: ")
            with open('user/user.txt', 'w') as name:
                name.write(Name)
                name.close()
        except Exception:
            pass