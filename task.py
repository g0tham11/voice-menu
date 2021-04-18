import os
import pyttsx3 as psy
import speech_recognition as sr

print('''
\t\t\t\t\t\t\tCommands Available:\n
\t\t\t\t\t\t\t1. Linux Commands Menu
\t\t\t\t\t\t\t2. AWS Configuration Menu
\t\t\t\t\t\t\t3. Docker Commands Menu
''')

psy.speak("Welcome to Python Automation program")
psy.speak("Choose option from above menu")

def commands():    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Start Speaking!")
        psy.speak("Star Speaking.")
        audio = r.record(source, duration=6)
        print("Working on it")
        psy.speak("Ok Working on it Please Wait!")
        text = r.recognize_google(audio, language="en-in")
        print("You said  {}".format(text))

    p = text.lower()
    return p

while True:

    p = commands()
    # p = "aws"
   
    if ("show linux command menu" in p) or ("linux" in p) or ("linux Command menu" in p) or ("first option" in p):
        psy.speak("Here is you Linux Commands Menu")
        os.system("python linux_menu/linux_menu.py")
        # os.system("python3 linux_menu/linux_menu.py")
   
    elif("aws" in p) or ("aws commands" in p) or ("aws configuration" in p) or ("cloud menu" in p) or ("fourth option" in p):
        psy.speak("Showing AWS configuration Menu")
        os.system("python aws_menu/aws_menu.py")
        # os.system("python3 aws_menu/aws_menu.py")
    
    elif("docker" in p) or ("docker command menu" in p) or ("third option" in p):
        psy.speak("Showing docker commands menu")
        os.system("python docker_menu/docker_menu.py")
        # os.system("python3 docker_menu/docker_menu.py") 

     else:
        psy.speak("Unable to run your command please try again")
        exit()

   

    