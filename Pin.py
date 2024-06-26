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

stateloader2 = open('50states\statespos.json')
states2 = json.load(stateloader2)

pyautogui.moveTo(920,860)

for i in range(50):
    mx, my = pyautogui.position()
    screenshot = pyautogui.screenshot(region=(mx + 75, my + 15, 150, 30))
    screenshot.save(
        r"C:\Users\Tyler\Desktop\Coding\Visual Studio Code\50states\state.png")

    img = Image.open("50states\state.png")
    text = pytesseract.image_to_string(
        img, config='--psm 6')

    print(text)
    for i in range(len(states)):
        if states[i] in text:
            text = states[i]
            states.remove(states[i])
            break
    
    print(text, ((states2[text])[0], (states2[text])[1]))
    pyautogui.click((states2[text])[0], (states2[text])[1])
