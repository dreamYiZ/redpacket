import pyautogui
import pprint as pp
import time
import datetime

while True:
    try:
        pp.pp("running auto clicker === "
              + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

        button_redpacket_location = pyautogui.locateOnScreen('image/redpacket.png', confidence=0.9)

        if button_redpacket_location is not None:
            pp.pp(button_redpacket_location)

            c1 = pyautogui.center(button_redpacket_location)

            pyautogui.click(c1.x, c1.y)

            time.sleep(3)

        button_join_location = pyautogui.locateOnScreen('image/join.png', confidence=0.9)

        if button_join_location is not None:
            c2 = pyautogui.center(button_join_location)
            pyautogui.click(c2.x, c2.y)

            pp.pp(button_join_location)

            time.sleep(3)

        button_ok_location = pyautogui.locateOnScreen('image/ok.png', confidence=0.9)

        if button_ok_location is not None:
            c3 = pyautogui.center(button_ok_location)
            pyautogui.click(c3.x, c3.y)

            pp.pp(button_ok_location)

        time.sleep(3)
    except Exception as e:
        print(f"An error occurred: {e}. Skipping this iteration.")
        time.sleep(5)
