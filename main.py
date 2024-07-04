import numpy as np
import cv2
import pyautogui
import pyautogui as pg
from PIL import ImageGrab
import time

while True:
    image = pyautogui.screenshot(region=(235, 589, 350, 300))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

    black_pixel_count = np.sum(image < 100)
    white_pixel_count = np.sum(image > 100)
    print(black_pixel_count, white_pixel_count)
    if black_pixel_count > 4000 and  black_pixel_count< 30000:
        pyautogui.press('up')

    elif white_pixel_count > 4000 and white_pixel_count< 30000:
        pyautogui.press('up')


    cv2.imshow('image', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


