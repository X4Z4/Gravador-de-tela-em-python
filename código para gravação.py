import cv2
import pyaudio
import wave
import keyboard
import pyautogui
import numpy as np
import pyaudio
from time import sleep

opcao = input("Você quer ligar a webcam? [s] ou [n]: ").lower()
webcam = None
if opcao == "s":
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
        print("Conectado")

elif opcao == "n":
    print("Webcam não será ligada")

else:
    print("Webcam não localizada")

audio = pyaudio.PyAudio()
stream = audio.open(
    input=True,
    format=pyaudio.paInt16,
    channels=1,
    rate=44000,
    frames_per_buffer=4096
)
frames = []

original_fps = 24  # FPS original
fator_retardante = 0.47

fps = int(original_fps * fator_retardante)  
tamanho_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"XVID")
video = cv2.VideoWriter("video.avi", codec, fps, tamanho_tela)

print("Gravação iniciando em:")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
print("Começou")
while True:
    bloco = stream.read(4096)
    frames.append(bloco)

    print_tela = pyautogui.screenshot()
    print_tela = np.array(print_tela)
    print_tela = cv2.cvtColor(print_tela, cv2.COLOR_RGB2BGR)

    video.write(print_tela)

    if webcam is not None:
        validar, ftwebcam = webcam.read()
        cv2.imshow('Vídeo da webcam', ftwebcam)
        key = cv2.waitKey(1)

    if keyboard.is_pressed("esc"):
        print("Terminando e compilando gravação")
        break

stream.start_stream()
stream.close()
audio.terminate()
audio_final = wave.open("gravação.wav", "wb")
audio_final.setnchannels(1)
audio_final.setframerate(44000)
audio_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
audio_final.writeframes(b"".join(frames))
audio_final.close()
video.release()
if webcam is not None:
    webcam.release()
cv2.destroyAllWindows()

