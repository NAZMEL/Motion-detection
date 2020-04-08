# coding: utf8
import cv2 
import numpy as np
from time import perf_counter, sleep

from sendmail import *

def IsCameraSignal(cam):
        sleep(1)
        ret = cam.read()[0]
        if ret == False:
            print('Your camera haven\'t been found.')
            getpass.getpass('Press ENTER to continue...')
            exit(1)  

def main():
    cam = cv2.VideoCapture(0)

    IsCameraSignal(cam)

   # sender = Mail_Sender()

    kernel = np.ones((7,7), np.uint8)

    fgbg = cv2.createBackgroundSubtractorMOG2()   # create segment phone
    sleep(3)
    send_flag = None 
    start_t = None

    while 1:
        if start_t is not None and perf_counter() - start_t  >= 30:
            send_flag = True
            #print(perf_counter() - start_t)
            start_t = perf_counter()

        frame = cam.read()[1]
        cv2.imshow('frame', frame) 

        blur = cv2.GaussianBlur(frame, (21, 21), 0)

        fgmask = fgbg.apply(blur)

        fgmask2 = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN, kernel)             # delete clouds
        thresh = cv2.threshold(fgmask2, 145, 255, cv2.THRESH_BINARY)[1]

        cnts =  cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

        if send_flag is None:
            sleep(2)
            send_flag = True
            continue
        
        for item in cnts:
            if cv2.contourArea(item) < 800:
                continue

            (x,y,w,h) = cv2.boundingRect(item)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)
            if send_flag:
                #cv2.imwrite('frame.jpg', frame)
                #sender.AddImageSend()
                #sender.sendLetter()
                send_flag = False
                start_t = clock()
        
        cv2.imshow('frame', frame)      
        c= cv2.waitKey(1)
        if c==27 or c == 1048603: #Break if user enters 'Esc'.
            break

    #sender.sendClose()
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
