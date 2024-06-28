 # Voice Command Project

This Voice Command Project is a Python-based application designed to enable users to control their computer through voice commands. The project leverages various Python libraries to provide functionalities such as opening a browser, searching and playing songs on YouTube, and opening the LinkedIn app. This project aims to enhance user interaction with the computer, making it more accessible and efficient through the use of voice recognition technology.

## Features

- **Open Browser**: Opens Google Chrome with a specified URL.
- **Open YouTube**: Opens YouTube in Google Chrome.
- **Play a Song**: Searches and plays a specified song on YouTube.
- **Open LinkedIn**: Opens the LinkedIn app (Windows only).
- **Voice Feedback**: Provides audio feedback for each command.
- **Exit**: Stops the voice command service.

Voice-Activated Browser Control: Users can open Google Chrome by simply saying "open browser." The application uses the webbrowser module to achieve this functionality.

YouTube Song Search and Play: The application allows users to search and play songs on YouTube by voice command. By saying "play a song" followed by the song name, the application will open YouTube, search for the specified song, and play it.

LinkedIn App Launch: Users can open the LinkedIn app on their Windows machine by saying "open LinkedIn." This feature is implemented using the subprocess module.

Text-to-Speech Feedback: The application provides voice feedback using the pyttsx3 library, making the interaction more intuitive and user-friendly.

Libraries and Tools
speech_recognition: For recognizing voice commands from the user.
pyttsx3: For converting text to speech, providing voice feedback to the user.
webbrowser: For opening web pages in the default browser.
os and platform: For interacting with the operating system.
time and pyautogui: For automating keyboard actions and controlling the browser.
subprocess: For opening the LinkedIn app on Windows.
