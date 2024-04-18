import os
import pyautogui
import pprint as pp
import time
import datetime
import traceback

# Define the base directory for images
image_dir = 'image'

while True:
    try:
        pp.pp("running auto clicker === "
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

        button_redpacket_location = pyautogui.locateOnScreen(os.path.join(image_dir, 'redpacket.png'), confidence=0.9)

        if button_redpacket_location is None:
            raise pyautogui.ImageNotFoundException("Image 'redpacket.png' not found.")

        pp.pp(button_redpacket_location)

        c1 = pyautogui.center(button_redpacket_location)

        pyautogui.click(c1.x, c1.y)

        time.sleep(3)
        button_join_location = pyautogui.locateOnScreen(os.path.join(image_dir, 'join.png'), confidence=0.9)

        if button_join_location is None:
            raise pyautogui.ImageNotFoundException("Image 'join.png' not found.")

        c2 = pyautogui.center(button_join_location)
        pyautogui.click(c2.x, c2.y)

        pp.pp(button_join_location)

        time.sleep(3)

        button_ok_location = pyautogui.locateOnScreen(os.path.join(image_dir, 'ok.png'), confidence=0.9)

        if button_ok_location is None:
            raise pyautogui.ImageNotFoundException("Image 'ok.png' not found.")

        c3 = pyautogui.center(button_ok_location)
        pyautogui.click(c3.x, c3.y)

        pp.pp(button_ok_location)

        time.sleep(3)
    except pyautogui.ImageNotFoundException as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        time.sleep(5)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print(traceback.format_exc())
        time.sleep(5)
