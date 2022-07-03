# #pip install pipwin
# #pipwin install pyaudio
# # python -m pip install SpeechRecognition
# #pip install playsound
# # pip install gTTs
# #pip install playsound==1.2.2


# import speech_recognition as sr   # recognise speech
# from playsound import playsound   #to play an audio file
# from gtts import gTTS #google text to speech
# import random
# from datetime import datetime
# import webbrowser #open browser
# import ssl
# import certifi
# import time
# import os # to remove created audio files
# #import serial
# from datetime import datetime as date


# isOpen = False
# r = sr.Recognizer() # initialise a recogniser
# # listen for audio and convert it to text:
    
# #arduino = serial.Serial(port="Com4", baudrate=115200, timeout=.1)

    
    
# def record_audio(ask=False):
#     with sr.Microphone() as source: # microphone as source
#         if ask:
#             speak(ask)
#         r.adjust_for_ambient_noise(source,duration=2)
#         print("Listening...")
#         audio = r.listen(source)  # listen for the audio via source
#         voice_data = ''
#         try:
#             print("Recognizing...")
#             voice_data = r.recognize_google(audio, language ='ar-Ar')  # convert audio to text
#         except sr.UnknownValueError: # error: recognizer does not understand
#             print("nothing")
#         #     speak('لم أفهم هذا')
#         except sr.RequestError:
#             speak('اسف فالخدمه لا تعمل') # error: recognizer is not connected
#         print(f">> {voice_data.lower()}") # print what user said
#         return voice_data.lower()

# def speak(audio_string):
#     tts = gTTS(text=audio_string, lang='ar') # text to speech(voice)
#     r = random.randint(1,20000000)
#     audio_file = os.getcwd() + '\\' +'audio' + str(r) + '.mp3'
#     tts.save(audio_file) # save as mp3
#     playsound(audio_file) # play the audio file
#     print(f"انت تقول : { audio_string}") # print what app said
#     os.remove(audio_file) # remove audio file


# class person:
#     name = ''
#     def setName(self, name):
#         self.name = name


# def there_exists(terms):
#     for term in terms:
#         if term in voice_data:
#             return True


# def respond(voice_data):
#     # speak('كيف حالك ؟ ')
#     # 1: greeting
#     if there_exists(['اهلا', 'مرحبا', 'كيف حالك']):
#         greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
#                      f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
#                      f"hello {person_obj.name}"]
#         greet = greetings[random.randint(0, len(greetings) - 1)]
#         speak("انا بخير كيف حالك؟")

#         # 2: name
#     if there_exists(["ما هو اسمك", "ماذا تسمي", "اسمك اي"]):
#         if person_obj.name:
#             speak("اسمي دادا")
#         else:
#             speak("اسمي دادا واسمك اي؟")

#     if there_exists(["اسمي", "انا اسمي"]):
#         person_name = voice_data.split("اسمي")
#         person_name2=person_name[-1].strip()

#         speak(f"حسنا سوف اتذكرك يا  {person_name2}")
#         person_obj.setName(person_name)  # remember name in person object

#     # 3: greeting
#     if there_exists(["كيف حالك", "عامل اي", "اخبارك"]):
#         speak(f"انا تمام شكرا علي سؤالك يا  {person_obj.name}")
    
#     # 4: time
#     if there_exists(["ما هو الوقت", "الساعه كام", "ساعتك كام"]):
#         time = datetime.now().strftime("%H:%M:%S")
#         speak(f"الساعه {time}")

#     # 5: search google
#     if there_exists(["ابحث عن"]) and 'اليوتيوب' not in voice_data:
#         search_term = voice_data.split("for")[-1]
#         url = f"https://google.com/search?q={search_term}"
#         webbrowser.get().open(url)
#         speak(f'هذا ماوجدته علي جوجل {search_term}')

#     # 6: search youtube
#     if there_exists(["يوتيوب"]):
#         search_term = voice_data.split("عن")[1]
#         url = f"https://www.youtube.com/results?search_query={search_term}"
#         webbrowser.get().open(url)
#         speak(f'هذا ما وجدته علي اليوتيوب {search_term}')

#     if there_exists(["انهاء", "قفل", "سلام"]):
#         speak("مع السلامة")
#         isOpen = False
#         return True
#     if there_exists(["قف","وقوف"]):
#         #arduino.write(bytes("stop", 'utf-8'))
#         time.sleep(0.05)
#         speak("حسنا")
#     if there_exists(["امشي","اتحرك"]):
#        # arduino.write(bytes("stop", 'utf-8'))
#         time.sleep(0.05)
#         speak("حسنا")
#     if there_exists(["اسم مطور ك"]):
#        # arduino.write(bytes("stop", 'utf-8'))
        
#         speak("محمد عاطف تحت اشراف جامعة كفر الشيخ")
#     if there_exists(["ما هو اليوم"]):
#        # arduino.write(bytes("stop", 'utf-8'))
#          data=date.today().strftime("%A")
#          if data=="Friday":
#               speak("الجمعة")
#          if data=="ٍSaturday":
#               speak("السبت")
#          if data=="Sunday":
#               speak("الاحد")
#          if data=="Monday":
#               speak("الاثنين")
#          if data=="Tuesday":
#               speak("الثلاثاء")
#          if data=="Wednesday":
#               speak("الالربعاء")
#          if data=="Thursday":
#               speak("الخميس")
             
        
   
    


# time.sleep(1)

# person_obj = person()
# while (1):
#     voice_data = record_audio()  # get the voice input
#     if voice_data == 'اهلا': #to make start when want to start speaking
#         isOpen = True
#     #print(isOpen)
#     if isOpen == True:
#        if respond(voice_data) == True:
#            isOpen = False
#         #break  # respond


#pip install pipwin
#pipwin install pyaudio
#python -m pip install SpeechRecognition
#pip install playsound
# pip install gTTs
#pip install playsound==1.2.2


import speech_recognition as sr   # recognise speech
from playsound import playsound
import pygame

# Wait until sound has finished playing

#to play an audio file
from gtts import gTTS #google text to speech
import random
from datetime import datetime
import webbrowser #open browser
import ssl
import certifi
import time
import os # to remove created audio files
#import serial
from datetime import datetime as date

#Servo

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

pwm = GPIO.PWM(17,50)
pwm2 = GPIO.PWM(27,50)
pwm.start(0)
pwm2.start(0)



# start moving code


import RPi.GPIO as GPIO          
from time import sleep

in1 = 14
in2 = 15
in3 = 11
in4 = 8
en = 21
en2 = 20
temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en,1000)
p2=GPIO.PWM(en2,1000)

p.start(60)
p2.start(60)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

def move(x):
    
    if x=='run':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        p.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'
        
    elif x == 'r':
        print('right')
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        p.ChangeDutyCycle(70)
        p.ChangeDutyCycle(70)
        
        x= 'z'
    
    elif x == 'l':
        print('left')
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        p.ChangeDutyCycle(70)
        p.ChangeDutyCycle(70)
        x= 'z'
        
    elif x=='low':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        #break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

# end moving code 

isOpen = False
r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
    
#arduino = serial.Serial(port="Com4", baudrate=115200, timeout=.1)
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source,duration=2)
        print("Listening...")
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            print("Recognizing...")
            voice_data = r.recognize_google(audio, language ='ar-Ar')  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print("nothing")
            #speak('لم أفهم هذا')
        except sr.RequestError:
            #speak("is not avaliable")
            #print('here')
            speak('اسف فالخدمه لا تعمل') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='ar') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = os.getcwd() + '/' +'audio' + str(r) + '.mp3'
    #print(os.getcwd() + '/' +'audio' + str(r) + '.mp3')
    print(audio_string)
    print(audio_file)
    tts.save(audio_file) # save as mp3
    #playsound(audio_file) # play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    print(f"انت تقول : { audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

class person:
    name = ''
    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def respond(voice_data):
    # speak('كيف حالك ؟ ')
    #moving speak
    if there_exists(['تحرك']):
        print("HI")
        move('f')
    if there_exists(['ارجع', 'للخلف']):
        move('b')
    if there_exists(['توقف', 'قف']):
        move('s')
    if there_exists(['يمين']):
        move('r')
    if there_exists(['يسار']):
        move('l')
           
    # 1: greeting
    if there_exists(['اهلا', 'مرحبا', 'كيف حالك', 'دودي']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
                     f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak("انا بخير كيف حالك؟.")
        sleep(3)
        speak("أهلًا بك في كلية الحاسباتْ والمعلوماتْ. \n تم صُنعيِ فيِ قسم تكنولوجْيّا المعلوماتْ تحتَ إشراف الدكتورعَمرْ أبوهاني والدكتور مَيّ رمضانْ")
        
        pwm.ChangeDutyCycle(7.5)
        pwm2.ChangeDutyCycle(12.5)
        sleep(1)
        # 2: name
    if there_exists(["ما هو اسمك", "ماذا تسمي", "اسمك اي"]):
        if person_obj.name:
            speak("Hello")
        else:
            speak("اسم يدودي واسمك اي؟")

    if there_exists(["اسمي", "انا اسمي"]):
        person_name = voice_data.split("اسمي")
        person_name2=person_name[-1].strip()

        speak(f"حسنا سوف اتذكرك يا  {person_name2}")
        person_obj.setName(person_name)  # remember name in person object

    # 3: greeting
    if there_exists(["كيف حالك", "عامل اي", "اخبارك"]):
        speak(f"انا تمام شكرا علي سؤالك يا  {person_obj.name}")
    
    # 4: time
    if there_exists(["ما هو الوقت", "الساعه كام", "ساعتك كام"]):
        time = datetime.now().strftime("%H:%M:%S")
        speak(f"الساعه {time}")

    # 5: search google
    if there_exists(["ابحث عن"]) and 'اليوتيوب' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'هذا ماوجدته علي جوجل {search_term}')

    # 6: search youtube
    if there_exists(["يوتيوب"]):
        search_term = voice_data.split("عن")[1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'هذا ما وجدته علي اليوتيوب {search_term}')
    
    if there_exists(["انهاء", "قفل", "سلام"]):
        speak("مع السلامة")
        isOpen = False
        return True
    if there_exists(["قف","وقوف"]):
        #arduino.write(bytes("stop", 'utf-8'))
        #time.sleep(0.05)
        speak("حسنا")
    if there_exists(["امشي","اتحرك"]):
       # arduino.write(bytes("stop", 'utf-8'))
        #time.sleep(0.05)
        speak("حسنا")
    if there_exists(["ما هو اليوم"]):
       # arduino.write(bytes("stop", 'utf-8'))
         data=date.today().strftime("%A")
         if data=="Friday":
              speak("الجمعة")
         if data=="ٍSaturday":
              speak("السبت")
         if data=="Sunday":
              speak("الاحد")
         if data=="Monday":
              speak("الاثنين")
         if data=="Tuesday":
              speak("الثلاثاء")
         if data=="Wednesday":
              speak("الالربعاء")
         if data=="Thursday":
              speak("الخميس")
             
        
   



time.sleep(1)

person_obj = person()
firstTime = True
while (1):
    if firstTime:
        speak('السلام عليكم \n انا دودي')
        pwm2.ChangeDutyCycle(12)
        sleep(6)
        pwm2.ChangeDutyCycle(8)
        sleep(3)
        pwm2.ChangeDutyCycle(0)
        firstTime = False
    voice_data = record_audio()  # get the voice input
    if voice_data == 'اهلا' or voice_data == 'مرحبا' : #to make start when want to start speaking
        isOpen = True
    #print(isOpen)
    if isOpen == True:
       if respond(voice_data) == True:
           isOpen = False
        #break  # respond
        