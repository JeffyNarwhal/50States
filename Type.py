import json
import os
import time
import pyautogui
from PIL import Image
import pytesseract
import keyboard
pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe')
stateloader = open('50states\states.json')
states = json.load(stateloader)

text = ""
for i in range(51):
    if i == 14:
        continue
    text += states[i]

time.sleep(3)
pyautogui.typewrite(text)

