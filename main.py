from pynput.keyboard import Listener
import pyautogui
from time import sleep
from hashlib import sha1
from argparse import ArgumentParser

def on_press(key):
    try:
        if key.char == trigger_key:
            print("✅ {} pressed".format(trigger_key), end="\r")
            sleep(0.1)

            position = pyautogui.position()
            x = position[0]
            y = position[1]
            pyautogui.screenshot(region=(x, y, 10, 10)).save('screenshot.png')
            
            with open('screenshot.png', "rb") as f:
                hash1 = sha1(f.read(), usedforsecurity=False).hexdigest()

            while True:
                pyautogui.screenshot(region=(x, y, 10, 10)).save('new.png')
                
                with open('new.png', "rb") as f:
                    hash2 = sha1(f.read(), usedforsecurity=False).hexdigest()

                if hash1 != hash2:
                    pyautogui.mouseDown(button=mouse_button)
                    sleep(0.1)
                    pyautogui.mouseUp(button=mouse_button)
                    print("⏳ Waiting for {}".format(trigger_key), end="\r")
                    break
                else:
                    print("⌛ Checking ... ", end="\r")
    except:
        return

if __name__ == "__main__":
    parser = ArgumentParser(description='Triggerbot')

    parser.add_argument('-triggerkey', '-t', type=str, help='Sets the trigger key', default='t')
    parser.add_argument('-mousebutton', '-m', type=str, help='Sets the mouse button', default='left')

    args = parser.parse_args()
    
    trigger_key = args.triggerkey
    mouse_button = args.mousebutton

    print("Triggerbot is running \n Made by willi")
    print("Settings:\n - trigger key = {}\n - mouse button = {}".format(trigger_key, mouse_button))
    
with Listener(on_press=on_press,) as listener:
    listener.join()