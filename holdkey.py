from pynput.keyboard import Controller
from time import sleep
from datetime import datetime

print("Which key?")
pressedkey = input()
print("Time (one number of hour for finishing) \nType 5 when u want the program to stop at 5 o'clock.")
runtime = input()
print("How long the delay of pressing?")
delay = input()

print("Pressed the key \"" + str(pressedkey) + "\" with the delay of " + str(delay) + ". Finished at " + str(runtime) + " o'clock")
print("Starting....\n")

keyboard = Controller()

def holdingKey(key, runtime, delay):
    currenttime = datetime.now()
    while True:
        keyboard.press(key)
        sleep(delay)
        currenttime = datetime.now()
        if currenttime.hour >= runtime:
            print("Stopped - reached runtime")
            break;

try:
    holdingKey(pressedkey, int(runtime), int(delay))
except Exception as e:
    print("Stopped - error")
