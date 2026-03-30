import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
    except:
        command = ""
        speak("Sorry, I didn't understand that")
    
    return command

def run_assistant(command):
    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today's date is " + date)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        speak(info)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I can search that for you")
        webbrowser.open("https://www.google.com/search?q=" + command)

# Run continuously
while True:
    command = take_command()

    if "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        break

    run_assistant(command)

    
    
##   py -3.9 -m streamlit run assistant.py