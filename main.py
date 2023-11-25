import Capture
from mss import mss
import numpy as np
import cv2 as cv2
from Matching import Detection

if __name__ == "__main__":
    game_window = Capture.setup_monitor("The Impossible Game")
    screen = mss()
    Detection.click_detection("Assets/start.png","Assets/main_menu.png")

    #while True:
    #    img = np.array(screen.grab(game_window))
    #    gray_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    #    print(gray_img)

