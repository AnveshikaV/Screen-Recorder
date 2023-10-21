import cv2
import pyautogui
import numpy as np
import time
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dim = (width, height)
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("recorded.mp4", f, 30.0 , dim)

start_time = time.time()
duration = 10
end_time = start_time + duration

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BG2BGR)

    output.write(frame)

    current_time = time.time()

    if current_time > end_time:
        break

output.release

print("Recording is ended.")
