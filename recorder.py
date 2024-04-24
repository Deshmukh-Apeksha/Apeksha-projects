import cv2
import pyautogui
import win32api
from win32api import GetSystemMetrics
import numpy as np
import time
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimension = (width,height)
format = cv2.VideoWriter_fourcc(*"H264")
output = cv2.VideoWriter("test.mp4",format,30.0,dimension)
now_start_time= time.time()
duration = 10
end_time = now_start_time + duration
while True:
    image = pyautogui.screenshot()
    frame = np.array(image)
    framecolor = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break

output.release()
print("-----end-----")