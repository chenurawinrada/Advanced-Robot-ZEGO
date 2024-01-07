'''
################################################################################################
                                ______________________________
                               -                              -
                                A Breif Description About ZEGO
                               -______________________________-

                    ZEGO is a multi perpose AI terminal robot (Like an assistant 
              robot in terminal mode). It can talk, control your pc for you,
              free chat (Using a trained AI model) and much more. Special thing
              is that this robot's coded using python. So any one can understand 
              the code. Also able to edit this code as you want. In future 
              updates, I will add some additional features to this robot. Github
              url-https://github.com/chenurawinrada/ZEGO-Bot. You can re-train
              the AI model. To do that, all you have to do is just type "train.py"
              on your terminal and hit enter. Or just tell the robot to train
              itself by typing 'train' and hit enter when the robot is running.
              If you do that it will train itself and re-start the Robot. If you
              want to edit the "intents.json", then make sure to  follow the
              current pattern of it. Otherwise you will have to create the whole
              file (intents.json) yourself. You also will be able to use the chat
              gpt in through this robot. To do that it will require "API KEY"
              in your accont in "openAI".

################################################################################################
'''

VERSION = "4.0"

import pyttsx3
import datetime
import os
import SystemCheckup
import random
import urllib.request
import hashlib
import maskpass
import colorama
import pickle
import time
import numpy as np
import json
from packaging import version
from colorama import Fore, init, Style
from urllib.request import urlopen
from threading import Thread
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

os.system('cls')

################################################################################################
###################################Colors for the terminal######################################
################################################################################################
init()
g = Fore.GREEN
m = Fore.MAGENTA
y = Fore.YELLOW
c = Fore.CYAN
w = Fore.WHITE
B = Style.BRIGHT

colors = [g, m, y, c, w]

################################################################################################
#################################### Check the system ##########################################
################################################################################################
check = SystemCheckup.SystemStatus()
BATTERY_STATUS = check.BatteryStatus()
RAM_USAGE = check.RamStatus()

################################################################################################
##################################### Talk function ############################################
################################################################################################

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print(text)
    engine.say(text)
    engine.runAndWait()

################################################################################################
###################################### Main initialize #########################################
################################################################################################
talk("Initialicing....")
try:
    with open('logs/system.log', 'r') as LOG:
        LOG.close()
except Exception:
    talk("Preparing for first run....")
    LOG = open('logs/system.log', 'w')
    ctime = "[" + str(datetime.datetime.now()) + "] Bot first run."
    LOG.write(ctime)
    LOG.write('\n')
    LOG.close()
    print("Created user profile files: 1", end="\r")
try:
    with open('logs/data.log', 'r') as DATA_LOG:
        DATA_LOG.close()
except Exception:
    LOG_D = open('logs/data.log', 'w')
    LOG_D.close()
    print("Created user profile files: 2", end="\r")
try:
    with open('logs/error.log', 'r') as ERROR_LOG:
        ERROR_LOG.close()
except Exception:
    LOG_E = open('logs/error.log', 'w')
    LOG_E.close()
    print("Created user profile files: 3", end="\r")
try:
    with open('user/user.txt', 'r') as name:
        name.close()
except Exception:
    user_ = open('user/user.txt', 'w')
    user_.close()
    print("Created user profile files: 4", end="\r")
try:
    with open("user/password.txt", "r") as g:
        g.close()
except Exception:
    user_ = open('user/password.txt', 'w')
    user_.close()
    print("Created user profile files: 5", end="\r")
time.sleep(0.01)
os.system('cls')
import sys

################################################################################################
########################################## Logger ##############################################
################################################################################################
def log_system(text):
    with open('logs/system.log', 'a+') as LOG:
        ctime = "[" + str(datetime.datetime.now()) + "]" + " " + text
        LOG.write(ctime)
        LOG.write('\n')
        LOG.close()
def log_data(text):
    with open('logs/data.log', 'a+') as LOG:
        ctime = "[" + str(datetime.datetime.now()) + "]" + " " + text
        LOG.write(ctime)
        LOG.write('\n')
        LOG.close()
def log_error(text):
    with open('logs/error.log', 'a+') as LOG:
        ctime = "[" + str(datetime.datetime.now()) + "]" + " " + text
        LOG.write(ctime)
        LOG.write('\n')
        LOG.close()
def clean_logs():
    with open('logs/system.log', 'w') as cl:
        cl.write('')
        cl.close()

################################################################################################
################################### Pre checking system ########################################
################################################################################################
try:
    talk("Checking system....")
    log_system("System Cchecked.")
    import faceRec
    import tcpic
    with open("commands/commands.json") as file:
        _data_ = json.load(file)
    talk("System online, Waiting for a user recognition....")
    log_system("Online")
except Exception as e:
    print(e)
    talk("Critical error, System files currupted or damaged!, Quitting....")
    log_error("Error occured.")
    log_system("Quited.")
    sys.exit(0)

################################################################################################
#################################### Check for updates #########################################
################################################################################################
def check_for_updates():
    try:
        print("Checking for updates")
        if check_connection(timeout=1):
            # (Remember) Add the update url
            url = 'https://raw.githubusercontent.com/chenurawinrada/Advanced-Robot-ZEGO/main/Advanced%20Robot/Metadata/metadata.json'
            rqt = requests.get(url, timeout=5)
            meta_sc = rqt.status_code
            if meta_sc == 200:
                metadata = rqt.text
                json_data = json.loads(metadata)
                gh_version = json_data['version']
                if version.parse(gh_version) > version.parse(VERSION):
                    return True
                else:
                    return False
        else:
            os.system('cls')
            pass
    except json.decoder.JSONDecodeError as e:
        log_error("Error occured while checking for updates", e)
        print("Error occured while checking for updates")
        pass

################################################################################################
################################### Print animated logo ########################################
################################################################################################
def logo():
    WIDTH = 50

    message = "ZEGO".upper()

    printedMessage = ["", "", "", "", ""]

    characters = {" ": [" ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " ",
                        " "],
                  "Z": ["▒███████▒",
                        "▒ ▒ ▒ ▄▀░",
                        "░ ▒ ▄▀▒░ ",
                        "  ▄▀▒   ░",
                        "▒███████▒",
                        "░▒▒ ▓░▒░▒",
                        "░░▒ ▒ ░ ▒",
                        "░ ░ ░ ░ ░",
                        "  ░ ░    ",
                        "░"],
                  "E": ["▓█████  ",
                        "▓█   ▀  ",
                        "▒███   ▒",
                        "▒▓█  ▄ ░",
                        "░▒████▒░",
                        "░░ ▒░ ░ ",
                        " ░ ░  ░ ",
                        "   ░   ░",
                        "   ░  ░ ",
                        ""],
                  "G": [" ▄████  ",
                        "██▒ ▀█▒▒",
                        "██░▄▄▄░▒",
                        "▓█  ██▓▒",
                        "▒▓███▀▒░",
                        "░▒   ▒ ░",
                        " ░   ░  ",
                        " ░   ░ ░",
                        "     ░  "],
                  "O": [" █████",
                        "██▒  ██▒",
                        "██░  ██▒",
                        "██   ██░",
                        " ████▓▒░",
                        " ▒░▒░▒░",
                        " ░ ▒ ▒░",
                        " ░ ░ ▒",
                        "   ░ ░"]}

    for row in range(5):
        for char in message:
            printedMessage[row] += (str(characters[char][row]) + " ")
    offset = WIDTH
    counttime = 0
    while counttime != 50:
        counttime = counttime + 1
        time.sleep(0.01)
        os.system('cls')
        for row in range(5):
            blow = random.choice(colors)
            print(blow+ B + " " * offset + printedMessage[row][max(1, offset*-1):WIDTH-offset
                                                     ])
        offset -= 1
        if offset <= ((len(message)+2)*6)*-1:
            offset = WIDTH
    time.sleep(0.9)
    print("********ZEGO THE FUTER OF AI********")

################################################################################################
################################ Print the logo(Normal logo) ###################################
################################################################################################
def bannar():
    os.system('cls')
    print(f"""{c}

                    ▒███████▒▓█████   ▄████  ▒█████
                    ▒ ▒ ▒ ▄▀░▓█   ▀  ██▒ ▀█▒▒██▒  ██▒
                    ░ ▒ ▄▀▒░ ▒███   ▒██░▄▄▄░▒██░  ██▒
                      ▄▀▒   ░▒▓█  ▄ ░▓█  ██▓▒██   ██░
                    ▒███████▒░▒████▒░▒▓███▀▒░ ████▓▒░
                    ░▒▒ ▓░▒░▒░░ ▒░ ░ ░▒   ▒ ░ ▒░▒░▒░
                    ░░▒ ▒ ░ ▒ ░ ░  ░  ░   ░   ░ ▒ ▒░
                    ░ ░ ░ ░ ░   ░   ░ ░   ░ ░ ░ ░ ▒
                      ░ ░       ░  ░      ░     ░ ░
                    ░{c}V {VERSION} BY MAXMOUSE \n
{g}""")

################################################################################################
######################################## GPT Chat ##############################################
################################################################################################
def OpenAI_GPT():
    try:
        with open('key.txt', 'r') as key_:
            _key = key_.read()
            key_.close()
        if _key == '':
            k = input("Enter the openai api key and rerun the command: ")
            key = str(k)
            with open("key.txt", "w") as file:
                file.write(key)
                file.close()
            main()
        else:
            with open('key.txt', 'r') as key_:
                _key = key_.read()
                key_.close()
            

        openai.api_key = _key
        def generate_text(prompt):
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=1024,
                n=1,
                stop=None,
            )

            message = response.choices[0].text.strip()
            return message

        print(f"{y}If you want to hear the text, then use {w}'-t' {y}at the start of the sentence{g}, Type 'exit' to return to zego.")
        while True:
            prompt = input("(ChatGPT)>> ")
            if '-t' in prompt:
                prompt = prompt.replace('-t', '')
                try:
                    if prompt != "exit" and prompt != "cls":
                        message = generate_text(prompt)
                        message = message + '\n'
                        talk(message)
                    elif prompt == 'cls':
                        os.system('cls')
                    else:
                        main()
                except KeyboardInterrupt:
                    main()
            else:
                try:
                    if prompt != "exit" and prompt != "cls":
                        message = generate_text(prompt)
                        message = message + '\n'
                        print(message)
                    elif prompt == 'cls':
                        os.system('cls')
                    else:
                        main()
                except KeyboardInterrupt:
                    main()
    except Exception as e:
        print(str(e))

################################################################################################
######################################### AI Chat ##############################################
################################################################################################
def AI_Chat():
    with open("intents.json") as file:
        data = json.load(file)
    model = keras.models.load_model('chat_model')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    max_len = 20
    while True:
        print(Fore.LIGHTBLUE_EX + "You: " + Style.RESET_ALL, end='')
        inp = input()
        # inp = take_command()
        # print(Fore.LIGHTBLUE_EX + "You: " + Style.RESET_ALL + inp)
        if inp.lower() == 'quit' or inp.lower() == 'exit':
            main()
        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                prase = np.random.choice(i['responses'])
                print(Fore.GREEN + "ZEGO: " + Style.RESET_ALL, prase)
                talk(prase)

################################################################################################
######################################## Commands ##############################################
################################################################################################
def get_commands(_command_):
    model = keras.models.load_model('commands/commands_model')
    with open('commands/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('commands/label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    max_len = 20
    inp = _command_
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in _data_['intents']:
        if i['tag'] == tag:
            prase = np.random.choice(i['responses'])
            return prase

################################################################################################
########################################## Main ################################################
################################################################################################
def main():
    logo()
    bannar()
    while True:
        # Get the user command
        com = input(f"\n{g}({c}ZeGo{g})>> {w}")
        if com == 'exit' or com == 'quit':
            talk('Have a nice day!')
            clean_logs()
            sys.exit(0)
        else:
            co = get_commands(com)
            match co:
                case "open explorer":
                    print("Openning explorer....")
                    pass
                case "open notepad":
                    print("Openning notepad....")
                    pass
                case "check connection":
                    print("Checking connection....")
                    pass
                case "check update":
                    print("Checking for updates....")
                    pass
                case "start chat":
                    AI_Chat()

################################################################################################
###################################Check the user pass##########################################
################################################################################################
def check_pass():
    try:
        with open('user/password.txt', 'r', encoding="utf-8") as pfile:
            hash_pass = pfile.read()
        return hash_pass
    except Exception:
        return ""

################################################################################################
#################################### Log in function ###########################################
################################################################################################
def log_in():
    # Ask for password and a user name
    line = check_pass()
    if line == '':
        talk("""\n\tWelcome to the future of artificial inteligence.
        First, let me introduce myself.
        My name is Zego.
        And I'm a fully functional console bot.
        I can help you with your day-today works.
        So, Let's get started!
        Create a profile to begin.\n""")
        pwd_ = maskpass.askpass(prompt="Creat a password: ", mask="#")
        conf_pwd = maskpass.askpass(prompt="Confirm the password: ", mask="#")
        if conf_pwd == pwd_:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("user/password.txt", "w") as f:
                f.write(hash1)
                f.close()
            with open('user/user.txt', 'w') as u:
                user = input("How may I call you?: ")
                u.write(user)
                print("Login completed!")
                talk("Profile created sucessfully.")
            time.sleep(2)
            os.system('cls')
            bannar()
            main()
        else:
            print("Sorry, Password was wrong!\n Try again!")
            time.sleep(2)
            os.system('cls')
            bannar()
            log_in()
    else:
        entpd = maskpass.askpass(prompt="Enter your password: ", mask="#")
        enc1 = entpd.encode()
        hash2 = hashlib.md5(enc1).hexdigest()
        if line == hash2:
            talk("Access granted!")
            os.system('cls')
            time.sleep(2)
            bannar()
            main()
        else:
            talk("Access denied!")
            talk("Wrong password! Try again!")
            time.sleep(1)
            os.system('cls')
            bannar()
            log_in()


################################################################################################
####################### Program start (Main will run after this)################################
################################################################################################
def start():
    try:
        with open('pics/ID.jpg', 'rb') as ID:
            ID.close()
    except Exception:
        talk('Preparing user ID, Look strait at the camera to take the face ID.')
        pic = tcpic.TakePicID()
        pic.PICID()
        talk("Face ID Captured. Continuing....")
        log_in()
        # Main is going on here....

    try:
        talk("recognizing the user....")
        with open("user/user.txt", "r") as namefile:
            username = namefile.read()
            namefile.close()
        rec = faceRec.RecognizeUserFace()
        if rec.con() == username:
            log_system("User recognized.")
            main()
        else:
            talk("Couldn't recognize the face. Use the password insted!")
            log_in()
    except Exception as e:
        print(f"Error is: {e}")
        log_error(e)
        log_system("Quited.")
        sys.exit(0)

################################################################################################
##################################Run the bot (Start)###########################################
################################################################################################

if BATTERY_STATUS:
    if RAM_USAGE:
        start()
        log_system("Run")
    else:
        talk("I need more memory...., Try boosting the host machine!")
        log_system("Quited.")
        sys.exit(0)
else:
    talk("Battery is running low!. Emergency shut down....")
    log_system("Quited.")
    sys.exit(0)

################################################################################################
