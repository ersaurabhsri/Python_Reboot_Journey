# First of all install in VS code or where are you runing. -> pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am just having fun with Python")
engine.runAndWait()
