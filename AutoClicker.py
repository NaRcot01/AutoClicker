from datetime import datetime
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import os

welcome_msg=input("NaRcot01 \n Get your mouse position from position.py \n press ENTER to continue... ")
delay=float(input('delay : '))
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')
how_many_repeat=int(input('How many times to repeat ? \n ' ))

 
 
class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        # self.button = button
        self.running = False
        self.program_run = True
        self.choices={
            'R':Button.right,
            'L':Button.left,
            'N':''
        }
        
 
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_run = False
        self.running=False

 
    def run(self):
        b=1
        while self.program_run:
            if b==1:
                x=([x for x in input("Mouse operations \n Pattern : position operation(R = right click , L = left click , N = none) \n Sample : 1560 700 R 1453 600 L 1000 400 N \n ").split()])
                # x.insert(0,0)
                b+=1
            
            now = datetime.now()
            global current_time
            current_time = now.strftime("%H:%M")
            current_time=str(current_time)
            time.sleep(10)
            
            
            while self.running:
                
                for q in range(how_many_repeat):
                    for ass in range(len(x)):
                        if ass % 3 == 0:
                            cvb1=ass+1
                            cvb2=ass+2
                            if x[cvb2]=='N':
                                mouse.position = (int(x[ass]),int(x[cvb1]))
                                # mouse.click(self.choices[x[cvb2]])
                                time.sleep(self.delay)
                            else:
                                mouse.position = (int(x[ass]),int(x[cvb1]))
                                mouse.click(self.choices[x[cvb2]])
                                time.sleep(self.delay)
                thread.exit()
            time.sleep(0.1)


mouse = Controller()
thread = ClickMouse(delay)
thread.start()
s=1
while thread.program_run:
    if s==1:
        rt=input('When? \n Sample : 22:22 ⤵ \n')
        s+=1
        print('Done')
    if current_time==rt:
        thread.start_clicking()