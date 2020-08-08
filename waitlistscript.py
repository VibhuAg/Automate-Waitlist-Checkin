# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:53:13 2020

@author: Vibhu Agrawal
"""

import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()

#Open Chrome
pyautogui.moveTo(width/2+150, 1800, duration=0.25)
pyautogui.click()

#Open new tab
pyautogui.moveTo(2350, 20, duration=0.25)
pyautogui.click()

#Go to Testudo
pyautogui.moveTo(1168, 1112, duration= 0.25)
pyautogui.click()

#Go to waitlist check in
pyautogui.moveTo(width/3*2, height/9*8, duration=0.25)
pyautogui.click()

#Click log in button
pyautogui.moveTo(width/4, height/2, duration=0.25)
pyautogui.click()


#Click on send Duo push
pyautogui.moveTo(width/5*3+200, height/2-200, duration=0.25)
pyautogui.click()

'''
#Open Google Messages
pyautogui.moveTo(2500, 500, duration=0.25)
pyautogui.doubleClick()
'''
