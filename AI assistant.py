import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes



engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speak("Current time is "+time)

def date():
    days = str(datetime.datetime.now().day)
    month = str(datetime.datetime.now().month)
    year = str(datetime.datetime.now().year)
    print(year+" " + month+" " + days)
    speak("Day is "+days)
    speak("Month is "+month)
    speak(year)

def wishme():
    speak("Welcome back sir...")
    # time()
    # date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir...")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir...")
    elif hour >=18 and hour<24:
        speak("Good Evening sir...")
    else:
        speak("Good Night sir...")
    speak("Jarvis at your service...")

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lelouch33340@gmail.com','Avatarzuko')
    server.sendmail('lelouch33340@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak(battery.percent)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(query)
        except:
            print("Say that again...")
            return "None"
        
        return query
def screenshot():
    image = pyautogui.screenshot()
    image.save('C:/Users/Star/OneDrive/Pictures/4962187.png')


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'time'in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia'in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'send email'in query:
            try:
                speak("What is the content of email")
                content = takecommand()
                to = 'aazzizz10301@gmail.com'
                sendemail(to,content)
                speak("Email has been send...")
                print("Email has been send...")

            except:
                speak("email does not send...")
                print("email does not send...")
        elif 'search in google' in query:
            speak("what should i search in google...")
            search = takecommand().lower()
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(path).open_new_tab(search+'.com')
        elif 'logout'in query:
            os.system('shutdown -1')
        elif 'shutdown'in query:
            os.system('shutdown /s /t 1')
        elif 'restart'in query:
            os.system('shutdown /r /t 1')
        elif 'play songs'in query:
            songpath = 'c:/Users/Star/Music'
            songs = os.listdir(songpath)
            os.startfile(os.path.join(songpath,songs[0]))
        elif 'remember'in query:
            speak("what should i remember...")
            data = takecommand()
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
            speak("data remebered...")
        elif 'do you know anything'in query:
            remember = open('data.txt','r')
            speak("you asked me to remember that"+ remember.read())
            print("you asked me to remember that"+ remember.read())
        elif 'screenshot'in query:
            screenshot()
            speak("done...")
        elif 'cpu'in query:
            cpu()
        elif 'joke'in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'offline' in query:
            quit()
