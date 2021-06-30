import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
from Prediction import pred_main
from Reverse_Recognition import rr_main
from easygui import *
from creating_dataset import cd_main

# ======================Main Login Screen============================================
while True:
    image   = "sign.png"
    msg="HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice","All Done!","Record Video","Create Dataset"]
    reply   = buttonbox(msg,image=image,choices=choices)
    if reply ==choices[0]:
        rr_main()
    if reply == choices[1]:
        quit()
    if reply == choices[2]:
        pred_main()
    if reply == choices[3]:
        cd_main()
