#! /usr/bin/env/ python

# needs some linux ubuntu packages, install with
# sudo apt-get install wmctrl
# sudo apt-get install python3
# sudo apt-get install python3-Xlib
# sudo apt-get install python3-pip
# sudo apt-get install scrot
# sudo apt-get install python3-tk
# sudo apt-get install python3-dev
#
# then in a virtualenv,
# pip3 install pillow
# pip3 install python3-xlib
# pip3 install pyautogui

# use 'xdotool getmouselocation' to get current mouse location

import subprocess
import pyautogui
import time

if __name__ == '__main__':

    # switch to desktop number 4 (in zero-based indexing)
    subprocess.call(['wmctrl', '-s', '4'])

    # start demo in Google Chrome webbrowser
    subprocess.Popen(['google-chrome-stable', 'http://nlesc.github.io/eEcology-Annotation-UI/demo/demo.html'],
                     shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)

    # select Google Chrome window and move to 0,0, resize to 1920x1080
    subprocess.call(['wmctrl', '-r', 'TrackAnnot - Demo - Google Chrome', '-e', '0,40,40,1840,1000'])

    # wait for stuff to load
    time.sleep(15)

    # 'Tracker' dropdown:
    pyautogui.moveTo(418,142)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # Select '355'
    pyautogui.moveTo(418,164)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # 'From' date dropdown
    pyautogui.moveTo(548,142)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # Select '28'
    pyautogui.moveTo(508,290)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # 'From' time dropdown
    pyautogui.moveTo(609,140)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('10:00:00', interval=0.25)
    time.sleep(1)
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(2)

    # 'To' date dropdown
    pyautogui.moveTo(761,142)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # Select '28'
    pyautogui.moveTo(717,290)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # 'To' time dropdown
    pyautogui.moveTo(850,140)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.typewrite('11:30:00', interval=0.25)
    time.sleep(1)
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    time.sleep(2)

    # 'Load tracker' button
    pyautogui.moveTo(1020,140)
    time.sleep(1)
    pyautogui.click()
    time.sleep(10)

    # delete current annotations
    pyautogui.moveTo(1695,797)
    time.sleep(1)
    for i in range(1,87):
        pyautogui.click()
        time.sleep(0.1)
    pyautogui.moveTo(1710,797)
    time.sleep(1)
    for i in range(1,19):
        pyautogui.click()
        time.sleep(0.1)

    # go to 'configure class' button
    pyautogui.moveTo(1443,752)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # delete class definitions
    pyautogui.moveTo(1080,558)
    time.sleep(1)
    for i in range(1,8):
        pyautogui.click()
        time.sleep(0.1)







