import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pywhatkit #This method can be used to remotely control your PC using your phone (Windows only)
import pyautogui
from welcome_backsir import *#welcomeback sir animation code
from requests import get
import wikipedia
import webbrowser
import keyboard

engine=pyt.init("sapi5")
voices=engine.getProperty("voices")#voices is a variable
print(voices)
'''
voice[0] and voice[3]=david voice
voice[1]= microsoft mark voice(better one)'
voice[2] and voice[4]=zira voice'''
engine.setProperty("voice",voices[1].id)#1st parameter lo voices ani pedthe male voice ye osthadi everytime change it to voice and voices[should be 1 for female 0 for male]
engine.setProperty("rate",140)#2nd parameter sets speed of voice

#converts text to speech
def speak(audio):
    engine.say(audio)#says the given audio
    engine.runAndWait()


#takecommand takes voiceinput from user and converts it to text and displays it on screen (required module=speechrecognition)
def takecommand():
    listener=sr.Recognizer()
    # microphone is source for voice
    with sr.Microphone() as source:
        print("Listening.....")
        listener.pause_threshold = 1
        voice = listener.listen(source,timeout=10,phrase_time_limit=5)#listens user voice from source(microphone)
        #if you dont speak or microphone is off for sometime(5) jarvis will automatically terminate


    try:
        print("Recognizing...")
        query = listener.recognize_google(voice,language="en-in")#lang=english-india
        #string madyala variable name iyaniki format strings vadtham

        query=query.lower()#converts user input to small letters
        print(f"user said:{query}")#prints what user said

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
    return query


#to wish
def wishme():
    hour=int(datetime.datetime.now().hour)
    #print(hour)

    if hour>=0 and hour<12:
        print("good morning")
        speak("good morning ")
    elif hour>=12 and hour<18:
        print("good afternoon")
        speak("good afternoon")
    else:
        print("good evening")
        speak("good evening")
    print("i am jarvis,how can i help you")
    speak("i am jarvis,how can i help you")



if __name__ == "__main__":
    def facerecogition():
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
        recognizer.read('trainer/trainer.yml')  # load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

        font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

        id = 2  # number of persons you want to Recognize

        names = ['', 'kiran']  # names, leave first empty bcz counter starts from 0

        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
        cam.set(3, 640)  # set video FrameWidht
        cam.set(4, 480)  # set video FrameHeight

        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        flag = True

        while flag:

            ret, img = cam.read()  # read the frames using the above created object

            converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

            faces = faceCascade.detectMultiScale(
                converted_image,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

                # Check if accuracy is less them 100 ==> 35 is perfect match

                ''' we are taking greater than 40 becuz sometimes for other persons accuracy will be 10 to 40 accuracy
                 depends upon on the camera quality in which sample photos are taken
                 if their is only one person sample then the model cannot distinguish between
                 different peoples so train more images add more images in samples either from internet or 
                  from camera but sequence must be 1.1, 2.1,3.1 etc each person should have unique sequence'''

                if (accuracy < 100 and accuracy >= 40):
                    id = names[id]
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    # pyautogui.press('esc')
                    welcomebacksir(video_path)

                    #speak("verification successfull")
                    #speak("welcome back sir")
                    flag = False  # flag becomes zero andd ends while loop
                    break  # breaks the current for loop



                else:
                    speak("verification unsuccessful")
                    id = "unknown"
                    accuracy = "  {0}%".format(round(100 - accuracy))
                    # line for jarvis.py you get error if you run face_recognition code
                    # break

                cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

            cv2.imshow('camera', img)

            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
        cam.release()
        cv2.destroyAllWindows()


    facerecogition()
    wishme()


    while True: #runs 1 time

         #userinput will be stored in query var
         query=takecommand()

         if "introduce yourself" in query or "tell me about yourself" in query or "jarvis introduce yourself" in query:
             from jarvis_with_sound import *

         elif "open notepad" in query or "open Notepad" in query:
             speak("opening notepad")
             npath ="C:\\Windows\\notepad.exe"#use double \\ by default you get \ only
             os.system(npath)

         elif "open command prompt" in query:
             speak("opening command prompt")
             os.system("start cmd")

         elif "open camera" in query:
             cap=cv2.VideoCapture(0)
             while True:
                 ret,img=cap.read()
                 cv2.imshow("webcam",img)
                 k=cv2.waitKey(50)
                 if k==27:
                     break
             cap.release()
             cv2.destroyAllWindows()



         #to make this work we have to link whatsapp web in microsoft edge to mobile
         elif "send WhatsApp message" in query:
             pywhatkit.sendwhatmsg("+919652261371","hello i am jarvis this message is sent by my boss from pycharms code",11,57)


         elif "play music" in query or "hit some music" in query:
             speak("playing music")
             music_dir_path = "C:\\Users\\kiran\\Music\\music folder"
             songs = os.listdir(music_dir_path)  # converting songs into list
             d = random.choice(songs)  # chooses random music
             os.startfile(os.path.join(music_dir_path, d))  # plays random music


         #<----------------IP ADDRESS(using request module)---------------------->
         elif "ip address " in query or "what is my ip address" in query:

             ip=get("https://api.ipify.org").text  #website gives ip address we are converting it into text
             print(f"your ip address is: {ip} ")
             speak(f"your ip address is: {ip} ")



         elif "who" in query or "where " in query or "what" in query or "how " in query:
             query=query.replace("who","")
             query = query.replace("what", "")
             query = query.replace("how", "")
             query = query.replace("where", "")
             info=wikipedia.summary(query,sentences=3)#read only 3 sentences
             speak("according to wikipedia")
             print(info)
             speak(info)


         elif "play" in query:
             query=query.replace('play','')#empty string replaces play
             #if i say play saranga dariya then system takes only saranga dariya.''(in this empty string saranga dariya will be stored)
             print("Playing"+query)
             speak("Playing"+query)
             pywhatkit.playonyt(query)
             break

         elif "search" in query or "google" in query:
             query=query.replace("search ","")
             query=query.replace("google ","")
             print("okay,Searching for",query)
             speak("okay searching for"+query)
             pywhatkit.search(query)


             #webbrowser.open("www.youtube.com")


         elif "open google" in query:
             webbrowser.open("www.google.com")

         elif "open facebook" in query:
             webbrowser.open("www.facebook.com")

         elif "I love you" in query or "Friday I love you" in query :
             from romeodilogue import *

         elif "he died loving but I am not his type" in query or "he died loving" in query:
             from chala_shekal_unnay import *

         elif "jarvis do you love me" in query or "do you love me" in query:
             from I_just_want_flirtationship import *

         elif "propose me" in query or "propose this lady" in query or "propose this girl" in query:
             from propose_dialogue import *

         elif "propose him" in query or "propose this guy" in query:
             from mca_proposal_scene import *

         elif "idiot" in query or "stupid" in query or "waste fellow" in query or "psycho" in query:
             from yendi_bro_anthamataannav import *


         elif "who is teja reddy" in query or "teja reddy" in query :
             from kingu_koduku import *

         elif "jarvis she loves you" in query or "love you" in query or "she loves you" in query:
             from devudu_unnadra import *

         elif "but as a friend" in query:
             from devudu_ledra import *

         elif "bye jarvis" in query or "bye" in query:
             from undiporadhe import *

         elif "jarvis sing a song for me" in query or "jarvis sing a song" in query or "sing a song" in query:
             from verejanmantu import *













    #<------PYAUTOGUI FEATURES=used to automate python using shortcut keys------->
         elif "open hidden menu" in query:
             #win +X=opens hidden menu
             pyautogui.hotkey("winleft","x")

         elif "open task manager" in query:
             #Crtl + Shift +Esc=opens task manager
             pyautogui.hotkey("ctrl","shift","esc")

         elif "open task view" in query:
             #win +tab=shows running tasks
             pyautogui.hotkey("winleft","tab")

         elif "shift tab" in query:
             #alt+tab=shifts the tab
             pyautogui.hotkey("alt","tab")

         elif "take screenshot" in query:
             #win+prtscr
             pyautogui.hotkey("winleft","prtscr")
             print("screenshot location C:\\Users\\kiran\\OneDrive\\Pictures\\Screenshots")
             speak("okay ,you the screenshot is in the given location")

         elif "take snip" in query:
             pyautogui.hotkey("winleft","shift","s")
             speak("please take your snip of your choice")

         elif "close current application" in query:
             pyautogui.hotkey("alt","f4")

         elif "take me to desktop" in query:
             pyautogui.hotkey("winleft","d")

         elif "open new virtual desktop" in query:
             pyautogui.hotkey("winleft","ctrl",'d')

         elif "open file explorer" in query:
             pyautogui.hotkey("winleft","e")

         elif "open run dialog box" in query:
             pyautogui.hotkey("winleft","r")

         elif "copy the selected text" in query or "copy" in query:
             pyautogui.hotkey("ctrl","c")
             speak("copied")

         elif "paste the copied text" in query or "paste" in query:
             pyautogui.hotkey("ctrl","v")
             speak("pasted")


   #<-----------------------------------BATTERY PERCENTAGE(psutil module)------------------------->

         elif "battery percentage" in query or "what is the battery percentage" in query or "battery percentage in my system" in query:
             import psutil
             battery=psutil.sensors_battery()
             percentage=battery.percent
             if percentage>=75 and percentage<=100:
                 speak(f"our system has {percentage} percent battery left,which is sufficient for about 2 hours at a moderate usage ")
             elif percentage>=30 and percentage<75:
                 speak(f"our system has {percentage} percent battery left,which might give you 60 to 70 minutes at a moderate usage")
             elif percentage>=0 and percentage<30:
                 speak(f"our system has a very crtical battery left, that is {percentage} percent battery,Please pluggin the charger")





   #<----------------------------------PLAYING MOVIE SCENES USING JARVIS-------------------------------->

         elif"play vijay sethupathi Entry from vikram" in query or "vijay sethupathi in vikram" in query or "vijay sethupathi from vikram" in query:
             speak("okay..")
             from santhanam_vikram import *

         elif "play radheshyam train scene" in query or "radheshyam train scene" in query:
             speak("okay..")
             from radheshyam import *

         elif "play agent tina from vikram" in query or "agent tina from vikram" in query:
             speak("okay..")
             from agent_tina import *

         elif "play vikram interval scene" in query or "vikram interval scene" in query:
             speak("okay..")
             from vikram_interval import *

         elif "play rrr trailer cut" in query or "triple r trailer cur" in query:
             speak("okay..")
             from rrr_trailercut import *

         elif "play vikram movie ending scene" in query or "play vikram movie ending scene" in query:
             speak("okay..")
             from suryarolex import *




         #<------------------------------webscraping------------------------->

         elif "extract data from website using web scraping" in query:
             speak("okay")
             from webscraping import *
             print("C:\\Users\kiran\\PycharmProjects\\kiranoruganti")
             print("kindly open the excel file in the location i have mentioned above.That excel file is your extracted data ")
             speak("kindly open the excel file in the location i have mentioned above and that excel file is your extracted data ")

         elif "sleep" in query or "jarvis sleep" in query:
             speak("bye")
             break
            
            
            
          
            

