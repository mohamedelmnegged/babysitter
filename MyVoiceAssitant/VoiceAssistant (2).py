#pip install pipwin
#pipwin install pyaudio
# python -m pip install SpeechRecognition
#pip install playsound
# pip install gTTs
#pip install playsound==1.2.2


import speech_recognition as sr   # recognise speech
from playsound import playsound   #to play an audio file
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
        #     speak('لم أفهم هذا')
        except sr.RequestError:
            speak('اسف فالخدمه لا تعمل') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='ar') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = os.getcwd() + '\\' +'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound(audio_file) # play the audio file
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
    # 1: greeting
    if there_exists(['اهلا', 'مرحبا', 'كيف حالك']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}",
                     f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak("انا بخير كيف حالك؟")

        # 2: name
    if there_exists(["ما هو اسمك", "ماذا تسمي", "اسمك اي"]):
        if person_obj.name:
            speak("اسمي دادا")
        else:
            speak("اسمي دادا واسمك اي؟")

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
        time.sleep(0.05)
        speak("حسنا")
    if there_exists(["امشي","اتحرك"]):
       # arduino.write(bytes("stop", 'utf-8'))
        time.sleep(0.05)
        speak("حسنا")
    if there_exists(["اسم مطور ك"]):
       # arduino.write(bytes("stop", 'utf-8'))
        
        speak("محمد عاطف تحت اشراف جامعة كفر الشيخ")
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
while (1):
    voice_data = record_audio()  # get the voice input
    if voice_data == 'اهلا': #to make start when want to start speaking
        isOpen = True
    #print(isOpen)
    if isOpen == True:
       if respond(voice_data) == True:
           isOpen = False
        #break  # respond