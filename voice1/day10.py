import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys
#import selenium
import pywhatkit
#import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir !")
    #speak("I am friday, digital voice assistant. Please tell me how can I help you")

def whoareu():
    speak("I am friday, digital voice assistant. Please tell me how can I help you")


def takeCommand():
    # It take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en')
        print("user said:", query)
    # speak(query)

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query


def open_application(query):
    if 'chrome' in query:
        speak("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')


    elif 'microsoft word' in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word')
        return
    elif 'excel' in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\EXCEL')
        return
    else:
        speak("Application not available")
        return


def search_web(query):
    # driver = webdriver.Firefox()
    #driver.implicitly_wait(1)
    #driver.maximize_window()
    if 'youtube' in query:
        speak("what do you want to search ")
        search = takeCommand().lower()
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
       # kit.playonyt(search)
        print("Here is what I fount for " + search)
        speak("Here is what I fount for " + search)
       # indx = query.split().index('youtube')
       # query1 = takeCommand().lower()
        #webbrowser.get("http://www.youtube.com/results?search_query=" + '+'.join(query1))
        #return

    elif 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)


    elif 'google' in query:

        speak("what do you want to search")

        # indx = query.split().index('google')
        search = takeCommand().lower()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print("Here is what I fount for " + search)
        speak("Here is what I fount for " + search)

    elif 'location' in query:
        speak("what is the location")
        location = takeCommand().lower()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print("Here is what I found for " + location)
        speak("Here is what I found for " + location)






def verify():
   # to = "ipstha8@gmail.com"
    # up:
    speak("what should I say?")
    content = takeCommand()
    print(content)
    speak(content)
    speak("do you want send this message")
    test = takeCommand().lower()
    if 'yes' in test:
       return(content)

    else:
        process_text()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('example22@gmail.com', '#Password')  # email id ma aafno gmail account rakhanye that account must be enabled less secure app
    server.sendmail('example22@gmail.com', to, content)  #
    server.close()


def process_text():
    # logic for executing tasks based on query
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'open' in query:
            open_application(query)

        elif 'search' in query:
            search_web(query)




        elif 'play music' in query or 'next music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            n = len(songs)
            l = random.randint(0, n - 1)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[l]))

       # elif  'stop music' in query:
            #os.close(Groove Music)

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")

        elif 'send email' in query:
            try:
                speak("say the name of person to send email ")
                name = takeCommand().lower()
                if 'king' in name:
                    to = "ipstha8@gmail.com"

                    #speak("what should I say?")
                    content = verify()
                    '''  
                    print(content)
                    speak(content)
                    speak("do you want send this message")
                    test = takeCommand().lower()
                    if 'yes' in test:
                        sendEmail(to, content)
                        speak("Email has been sent")
                        print("Email has been sent")

                    else:
                        process_text()

                    '''

                    sendEmail(to, content)
                    speak("Email has been sent")
                    print("Email has been sent")

                elif 'prince' in name:
                    to = "ipstha8@gmail.com"
                    speak("what should I say?")
                    content = takeCommand()

                    sendEmail(to, content)
                    speak("Email has been sent")
                    print("Email has been sent")

                elif 'max' in name:
                    to = "pbc12359@gmail.com"
                    speak("what should I say?")
                    content = takeCommand()

                    sendEmail(to, content)
                    speak("Email has been sent")
                    print("Email has been sent")

                else:
                    speak("you provided name's email address doesnot save in file")





            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")


        elif 'stop' in query or 'bye' in query or 'thank you' in query:
            speak("bye sir,have a good day")
            sys.exit()


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'friday' in query:
            process_text()











