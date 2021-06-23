import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def TaskExe():

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Jarvis .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis!")
            break
