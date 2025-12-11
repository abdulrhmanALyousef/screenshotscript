import pyautogui
import cv2
import numpy as np

imgPath = "img path"  

screenshot = pyautogui.screenshot()
img = np.array(screenshot)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
flipped = cv2.flip(gray, 1)

cv2.imwrite(imgPath, flipped)

print("Image saved on Desktop")

cv2.imshow("Final Image", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
