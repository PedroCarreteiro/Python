import pyautogui
import time

print("Posicione o mouse... (Ctrl+C para sair)")
time.sleep(2)

try:
    while True:
        x, y = pyautogui.position()
        print(f"Posição: ({x}, {y})", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nFinalizado!")