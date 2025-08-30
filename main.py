import speech_recognition as sr 
import webbrowser
import pyttsx3 #ham text to speech kar sakte hai agar kuch bolwana hai jarvis se to kar saktehai

recognizer=sr.Recognizer()#speech regonition funcitonliyt lene me madad karti hai 
engine=pyttsx3.init() #intiialize hojayega hmara pyttsx

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open Google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
     
if __name__=="__main__":
    speak("Initializing robo...")
    while True:
        #listen for the wake word "jarvis"
        #obtain audio from the microphone
        r=sr.Recognizer()
        
        print("reconginzing")
        #recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            # if(word.lower()=="robo" ):
            #    speak("Ya")
            #    #listen for command
            #    with sr.Microphone() as source:
            #         print("robo active....")
            #         audio=r.listen(source,timeout=2)
            #         command=r.recognize_google(audio)
            processCommand(word)
        except Exception as e:
            print("Error; {0}".format(e))

#hello suvan 
