from pynput.mouse import Controller
from pynput.keyboard import Listener 
print(" Press any key on your keyboard to get the x,y ")
mouse = Controller()
def on_press(key):
    print(mouse.position)
with Listener(on_press=on_press) as listener:
    listener.join()
