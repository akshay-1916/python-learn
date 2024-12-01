# for Mac
# from os import system
# names=["akshay","Rohan","hari","Ram","Alex"]
# for name in names:
#   system(f'say Shoutout to {name}')

# for Window
import pyttsx3 

# initialise the pyttsx3 engine 
e = pyttsx3.init() 

# convert text to speech 
e.say("Linkdedin,Instagram,Facebook,twitter,Snapchat") 
e.runAndWait()
