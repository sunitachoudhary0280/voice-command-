import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import platform
import time
import pyautogui
import subprocess

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to microphone input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

# Function to open Google Chrome with a specific URL
def open_chrome(url):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable
    webbrowser.get(chrome_path).open(url)

# Function to search a song on YouTube
def search_song_on_youtube(song_name):
    # Open YouTube
    open_chrome("https://www.youtube.com")
    # Wait for the page to load
    time.sleep(5)
    # Click on the search bar (usually we need to press 'tab' a few times)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.press('enter')
    # Type the song name and press Enter
    pyautogui.write(song_name)
    pyautogui.press('enter')
    speak(f"Searching for {song_name} on YouTube.")
    # Wait a bit for search results to load and then click the first result
    time.sleep(5)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.press('enter')

# Function to perform actions based on the command
def perform_action(command):
    if "open browser" in command:
        speak("Opening browser.")
        open_chrome("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        open_chrome("https://www.youtube.com")
    elif "play a song" in command:
        speak("Which song do you want to play?")
        song_name = listen()
        if song_name:
            search_song_on_youtube(song_name)
    elif "open linkedin" in command:
        open_linkedin_app()
    elif "exit" in command:
        speak("Goodbye!")
        return True
    else:
        speak("Command not recognized.")
    return False

# Function to open the LinkedIn app
def open_linkedin_app():
    os_name = platform.system()
    if os_name == "Windows":
        subprocess.Popen(["start", "linkedin://"], shell=True)
    else:
        speak("LinkedIn app opening is not supported on this OS.")

# Main function
def main():
    speak("How may I help you?")
    while True:
        command = listen()
        if command:
            if perform_action(command):
                break

if __name__ == "__main__":
    main()
