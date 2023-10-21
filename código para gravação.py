import cv2
import pyaudio
import wave
import keyboard
import pyautogui
import numpy as np
import pyaudio
import sys
from cx_Freeze import setup, Executable

webcam = cv2.VideoCapture(0)
if webcam.isOpened():
    print("conectou")


audio = pyaudio.PyAudio()
stream = audio.open(
    input= True,
    format= pyaudio.paInt16,
    channels= 1,
    rate = 44000,
    frames_per_buffer= 1024



)
frames = []



fps = 60
tamanho_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("video.avi",codec,fps,tamanho_tela)


while True:
    bloco = stream.read(1024)
    frames.append(bloco)

    print_tela = pyautogui.screenshot()
    print_tela = np.array(print_tela)
    print_tela = cv2.cvtColor(print_tela,cv2.COLOR_RGB2BGR)

    video.write(print_tela)
    if webcam.isOpened():
        validar,ftwebcam = webcam.read()
        cv2.imshow('video da webcam',ftwebcam)
        key = cv2.waitKey(1)


    if keyboard.is_pressed("esc"):
        break
stream.start_stream()
stream.close()
audio.terminate()
audio_final=wave.open("gravação.wav", "wb")
audio_final.setnchannels(1)
audio_final.setframerate(44000)
audio_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
audio_final.writeframes(b"".join(frames))
audio_final.close()
video.release()
webcam.release()
cv2.destroyAllWindows

