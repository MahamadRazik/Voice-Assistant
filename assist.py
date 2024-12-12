import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Charmy your personal voice assistant. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "made" in query or "developed" in query:
            speak("I was created by Shree Krishna, Yashwanth, Prajwal and Razik")

        elif "how" in query:
            speak("I am doing good. Thank you for being a kind human being.")
            print("I am doing good. Thank you for being a kind human being.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif "what time is it" in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "what's the date" in query:
            now = datetime.datetime.now()
            current_date = now.strftime("%B %d, %Y")
            speak(f"Today is {current_date}")
            print(f"Today is {current_date}")

        elif "open file" in query:
            filename = query.split()[-1]
            try:
                os.startfile(filename)
                speak(f"Opening file {filename}")
            except Exception as e:
                speak(f"File {filename} not found.")

        elif 'music' in query:
            music_dir = 'C:\\Music Downloader'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found in the directory.")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'take me to' in query:
            task = query.replace('take me to', '')
            speak('opening' + task)
            pywhatkit.search(task)

        elif 'who is' in query or 'tell me' in query or 'what is' in query:
            if 'who is' in query:
                person = query.replace('who is', '').strip()
            elif 'tell me' in query:
                person = query.replace('tell me', '').strip()
            elif 'what is' in query:
                person = query.replace('what is', '').strip()
            try:
                info = wikipedia.summary(person, sentences=3)
                speak(info)
                print(info)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
                print(e.options)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that.")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif "bye" in query or "cya" in query or "stop" in query:
            speak("Goodbye, have a nice day!")
            break

        elif "weather" in query:
            webbrowser.open("https://www.weather.com/")
            speak("Here is the weather report.")

        elif "news" in query:
            webbrowser.open("https://news.google.com/")
            speak("Here are the latest news headlines.")

        elif "search" in query:
            query = query.replace("search the web", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching the web for {query}")

        elif "directions to" in query:
            location = query.replace("directions to", "")
            webbrowser.open(f"https://www.google.com/maps/dir/?api=1&destination={location}")
            speak(f"Getting directions to {location}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
