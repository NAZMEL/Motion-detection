# coding: utf8
import cv2 
from time import sleep
import keyboard
from config import bcolors

# check signal from camera
def IsCameraSignal(cam):
    sleep(1)

    ret = cam.read()[0]  # is signal from camera

    if ret == False:
        print(f'{bcolors.FAIL} Your camera haven\'t been found. {bcolors.ENDC}')
        print('if you want to continue to work with program press \"ENTER\" or \"ESC\" for exit.')

        # get any key from keyboard 
        key = keyboard.read_key()
        
        if key  == "esc":
            # key == ESC
            exit(1)  
        elif key == "enter":
            # key == ENTER
            IsCameraSignal(cam)
        else:
            exit(1)
    else:
        print(f"{bcolors.HEADER}Your camera are ready! {bcolors.ENDC} \n")




