import cv2
import pyttsx3 as pyt
import speech_recognition as sr
import datetime
import os
import cv2
import random
import pywhatkit as pwt #This method can be used to remotely control your PC using your phone (Windows only)
import pyautogui
from welcome_backsir import *

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


            if (accuracy < 100 and accuracy>=40):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                #pyautogui.press('esc')
                welcomebacksir(video_path)
                #speak("verification successfull")
                #speak("welcome back sir")
                flag=False #flag becomes zero andd ends while loop
                break #breaks the current for loop



            else:
                speak("verification unsuccessful")
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                #line for jarvis.py you get error if you run face_recognition code
                #break

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break

    print("face reciognition code execution completed.")
    cam.release()
    cv2.destroyAllWindows()
facerecogition()