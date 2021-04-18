import subprocess
import os
import shlex
import boto3
import json
import datetime
import pandas as pd
import time
from subprocess import check_call
import speech_recognition as sr
import pyttsx3 as psy

def change_color(x):
    cmd = "tput setaf {}".format(x)
    os.system(cmd)

def ask_choice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start Speaking!")
        psy.speak("Star Speaking.")
        print()
        r.pause_threshold = 1
        audio = r.record(source, duration=6) 
        text = r.recognize_google(audio, language="en-in")
        print("You said  {}".format(text))   
        option = text.lower()
    psy.speak("Ok Working on it Please Wait!")
    return option


def get_ip(interface=""):
    if not interface:
        interface = subprocess.getoutput("route | awk '/default/ {print $8}'")
    ip = subprocess.getoutput("ifconfig {0}".format(interface) + " | awk '/inet / {print $2}'")
    return ip


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)
