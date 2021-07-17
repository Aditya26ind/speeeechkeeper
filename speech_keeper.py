import pyttsx3
import speech_recognition as sr # if pyauio is not working go to the cmd run as admisnitrator and then
# pip install pipwin then pipwin install pyaudio
# THIS APP IS USE TO RECORD YOUR SPEECH AND KEEP IN TXT FORMAT DURATION CAN BE MANAGE BY YOU AND
# PLEASE TAKE 2 SEC AFTER LISTENING POP UP TO SPEAK AND SPEEK CLEAR....@ADITYA SALABH...
def speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        TIME_OF_SPEECH = int(input("Please Tell time till you speak:"))
        name = str(input("Name:"))
        print("listening...")
        r.pause_threshold=0.7
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio=r.listen(source,phrase_time_limit=TIME_OF_SPEECH)
    try:
        print("reccognising")
        command = r.recognize_google(audio, language="en-in")
        print(command)
        i=0
        fi=open(f'speech{i}.txt',"w")
        i=i+1
        fi.write(f"{name}:{command}")
        fi.close()
        text_to_speech(command)
    except Exception as e:
        print(e)
        print("say it again sir")
        text_to_speech("say it again sir")

def text_to_speech(audio):
    engine=pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

while True:
    speech()