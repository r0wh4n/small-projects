
import pyautogui as pt
import time

limit = input("Enter no. of Messages: ")
msg = input("Message you want to send: ")
i = 0

time.sleep(3)

while i < int(limit):

    pt.typewrite(msg)
    pt.press('Enter')

i += 1
