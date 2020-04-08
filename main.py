# coding: utf8
import cv2 
import numpy as np
import os, datetime, time
import threading
from cam_functions import *
from sender import Sender
from csv_work import read_as_dict
from config import *


if __name__ == '__main__':
    
    send_email = Sender(receivers = read_as_dict(FILE_RECEIVERS))

    # for allow to save image and send message
    permit_status = True
    detect_status = False

    # get current time from begin epoch
    last_time = time.time()

    # full path to this directory
    path = os.getcwd()

    # union main path with an important folder
    directory = os.path.join(path, "images")
    os.chdir(directory)

    # using image from default camera
    cam = cv2.VideoCapture(0)
      
    # check signal from camera
    IsCameraSignal(cam)
    
    # create array with ones 7x7
    kernel = np.ones((7,7), np.uint8)

    # Gaussian Mixture-based Background/Foreground Segmentation
    # create a mask
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:
        # to take image from camera
        frame = cam.read()[1]
        
        cv2.imshow('Move Detector', frame)
        k = cv2.waitKey(1)

        # blur image
        blur = cv2.GaussianBlur(frame, (21, 21), 0)

        fgmask = fgbg.apply(blur)

        fgmask2 = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN, kernel)             # delete clouds

        thresh = cv2.threshold(fgmask2, 145, 255, cv2.THRESH_BINARY)[1]
        cnts =  cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

        # paint contour as rectangle around
        for item in cnts:
            if cv2.contourArea(item) < 3000:
                continue
            
            detect_status = True
            (x,y,w,h) = cv2.boundingRect(item)

            # print coordinate of rectangle points
            # bprint('\t', cv2.boundingRect(item))

            # paint rectangle
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 3)
        
        if int(time.time() - last_time) > DELAY_SEND:
            permit_status = True
            last_time = time.time()

        if detect_status and permit_status:
            time_detected = str(datetime.datetime.now())[:-7]
            print(f"Move was detected: {bcolors.WARNING} {time_detected} {bcolors.ENDC}")

            # save image in folder
            img_name = "DETECT_{0}.jpg".format(time_detected)
            img_name = img_name.replace("-", "_").replace(":", "-")

            cv2.imwrite(img_name, frame)

            thread = threading.Thread(target = send_email.send_mails, args = (MESSAGE, img_name), daemon = True)
            thread.start()
            
            permit_status = False
            detect_status = False

        cv2.imshow('Move Detector', frame)  
        c= cv2.waitKey(1)

        # Break if user enters 'Esc'
        if c==27 or c == 1048603: 
            break

    
    cam.release()
    cv2.destroyAllWindows()