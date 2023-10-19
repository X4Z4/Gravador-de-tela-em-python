import cv2
import keyboard
import pyautogui
import numpy as np
import pyaudio

fps = 60
tamanho_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("video.avi",codec,fps,tamanho_tela)

while True:
    print_tela = pyautogui.screenshot()
    print_tela = np.array(print_tela)
    print_tela = cv2.cvtColor(print_tela,cv2.COLOR_RGB2BGR)

    video.write(print_tela)

    if keyboard.is_pressed("esc"):
        break
video.release()
cv2.destroyAllWindows
