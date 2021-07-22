from ctypes import pydll
import pyautogui
from win32api import GetSystemMetrics
import sys, os


path="D:/SMP"
if not os.path.exists(path):
    os.makedirs(path)

width= GetSystemMetrics(0)
height=GetSystemMetrics(1)

pyautogui.hotkey('winleft')
pyautogui.typewrite('salesmate\n')
pyautogui.press("enter",1,20)
pyautogui.press("enter",1,5)
pyautogui.press(['alt','c'])
pyautogui.press("a")
pyautogui.press("d",1,1)
pyautogui.press("enter",1,1)
pyautogui.press("enter",1,1)
pyautogui.typewrite("abcd")
pyautogui.press("enter",1,1)
pyautogui.typewrite("zxc")
pyautogui.press("enter",1,1)
pyautogui.press("enter",1,1)
pyautogui.typewrite("qwertyuiop")
pyautogui.press("enter",1,1)
pyautogui.typewrite("123456")
pyautogui.press("enter",1,1)
pyautogui.typewrite("zxcvbn12345@gmail.com")
pyautogui.press("enter",1,1)
pyautogui.press(['left','left','left'])
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.typewrite('download.png') 
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)
pyautogui.press('enter',1,1)












