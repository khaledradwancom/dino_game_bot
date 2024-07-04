import pyautogui
import selenium
from PIL import ImageGrab
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://elgoog.im/dinosaur-game/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)





time.sleep(2)


body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.SPACE)
time.sleep(4)

time = time.time()

def detect_obstacles():
    # bbox (xmin, ymin, xmax, ymax)
    # Get the values for the grab-box by trying
    xmax = 335
    width = 65
    ymax = 620
    height = 80
    box = ImageGrab.grab(bbox=(xmax - width, ymax - height, xmax, ymax))
    colors = [color[1] for color in box.getcolors()]
    if (172, 172, 172, 255) in colors:
        return True
    else:
        return False

def jump():
    body.send_keys(Keys.ARROW_UP)
    if time.time() > time + 50:
        time.sleep(0.16)
    else:
        time.sleep(0.19)
    body.send_keys(Keys.ARROW_DOWN)
detect_obstacles()
jump()
