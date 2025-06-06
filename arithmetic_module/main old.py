#############################################       LIBRARIES       #####################################################
import cv2
import ctypes
import mediapipe as mp
from PIL import Image, ImageTk 
from tkinter import *
import ctypes 
from datetime import datetime 
from functools import partial
from cvzone.HandTrackingModule import HandDetector
import random
import threading
from playsound import playsound
import os
import sys

def wrong():
    playsound(os.getcwd()+'/assets/arithmetic_module/wrong.mp3')

def correct():
    playsound(os.getcwd()+'/assets/arithmetic_module/correct.mp3')

########################################        SYSTEM      ################################################################3
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
geometry =  str(screensize[0])+"x"+str(screensize[1])
# print(geometry)
##################################################      HAND TRACKING       #############################################
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 

#GUI window
window1 = Tk()
window1.geometry(geometry)
window1.title("Workout")
video = cv2.VideoCapture(0)

def number_selection(selected,count):
    temp = random.randint(1,10)
    while temp==count:
        temp = random.randint(1,10)
    if selected=="addition":
        num1=random.randint(1,100)
        final_num = num1+temp
    elif selected=="subtraction":
        num1=random.randint(1,100)
        final_num = num1-temp
    elif selected=="multiplication":
        num1=random.randint(2,10)
        final_num = num1*temp
    elif selected=="division":
        num1=random.randint(2,10)
        final_num = num1*temp
        num1,final_num=final_num,num1
    return num1,temp,final_num


    
def logic(selected):
    # mp_drawing = mp.solutions.drawing_utils
    # mp_drawing_styles = mp.solutions.drawing_styles

    for widget in window1.winfo_children():
        widget.destroy()
    global video
    detector = HandDetector(maxHands=2, detectionCon=0.8)
    start_time = datetime.now()
    score = 0
    num1 = 0
    final_num =0
    
    if selected=="addition" or selected=="subtraction" or selected=="multiplication" or selected == "division":
        num1,temp,final_num = number_selection(selected,0)
        while True:
            _, img = video.read()

            current_time = datetime.now()
            total_seconds = (current_time-start_time).total_seconds()
            if total_seconds>30:
                break
            bg = cv2.imread(os.getcwd()+"/assets/arithmetic_module/"+selected+".png")
            bg = cv2.resize(bg,screensize)
            count=0
            img = cv2.flip(img, 1)
            try:
                hand = detector.findHands(img, draw=True)
                # print(hand)
            except:
                hand=None
            # print(hand)
            # fing = cv2.imread("Put image path with 0 fingures up")
            if hand:
                # lmlist = hand[0]
                for i in hand[0]:
                    if i:
                        fingerup = detector.fingersUp(i)
                        # print(fingerup)
                        if fingerup == [0, 1, 0, 0, 0]:
                            fing = 1
                        elif fingerup == [0, 1, 1, 0, 0]:
                            fing = 2
                        elif fingerup == [0, 1, 1, 1, 0]:
                            fing = 3
                        elif fingerup == [0, 1, 1, 1, 1]:
                            fing = 4
                        elif fingerup == [1, 1, 1, 1, 1]:
                            fing = 5
                        else:
                            fing=0
                        count+=fing
            bg[215:705,65:1310]=cv2.resize(img,(1245,490))
            cv2.putText(bg,str(count),(630,125),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            cv2.putText(bg,str(score),(110,110),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            cv2.putText(bg,str(num1),(350,125),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            # cv2.putText(bg,str(),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            cv2.putText(bg,str(final_num),(900,125),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            cv2.putText(bg,str(int(total_seconds)),(1255,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            if count==temp:
                score+=10
                t1= threading.Thread(target=correct)
                t1.start() 
                num1,temp,final_num = number_selection(selected,count)

            # cv2.putText(bg,str(count),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            cv2.namedWindow('DISPLAY SCREEN',cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("DISPLAY SCREEN", bg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
                
    
    bgimg3 = ImageTk.PhotoImage(Image.open("images/result.png").resize(screensize))
    back_button_img = ImageTk.PhotoImage(Image.open("images/home.png").resize((80, 80)))
    label1= Label(window1, image=bgimg3)
    Label(label1,text = str(int(score)),font="Helvetica 42 bold").place(x = 610,y = 335)
    Button(window1,image=back_button_img,borderwidth=0,command=partial(start,None)).place(x=600,y=495)
    #Button(window1,image=squats_button_img,borderwidth=0,command=main).place(x=550,y=530)
    label1.place(x=0,y=0)
    window1.wm_attributes('-fullscreen', 'True')
    window1.mainloop()


# def category():
#     for widget in window1.winfo_children():
#         widget.destroy()
    
#     bgimg1 = ImageTk.PhotoImage(Image.open("images/categories.png").resize(screensize))
#     addition_button_img = ImageTk.PhotoImage(Image.open("images/addition_button_m.png").resize((270, 70)))
#     subtraction_button_img = ImageTk.PhotoImage(Image.open("images/subtraction_button_m.png").resize((270, 70)))
#     multiplication_button_img = ImageTk.PhotoImage(Image.open("images/multiplication_button_m.png").resize((270, 70)))
#     division_button_img = ImageTk.PhotoImage(Image.open("images/division_button_m.png").resize((270, 70)))
#     game_zone_button_img = ImageTk.PhotoImage(Image.open("images/game_zone.jpg").resize((130, 160)))
#     label1= Label(window1, image=bgimg1)
#     Button(window1,image=addition_button_img,borderwidth=0,command=partial(logic,"addition")).place(x=540,y=160)
#     Button(window1,image=subtraction_button_img,borderwidth=0,command=partial(logic,"subtraction")).place(x=540,y=300)
#     Button(window1,image=multiplication_button_img,borderwidth=0,command=partial(logic,"multiplication")).place(x=540,y=460)
#     Button(window1,image=division_button_img,borderwidth=0,command=partial(logic,"division")).place(x=540,y=630)
#     Button(window1,image=game_zone_button_img,borderwidth=0,command=partial(logic,"game")).place(x=1165,y=390)

#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()

# def start(flag):
#     for widget in window1.winfo_children():
#         widget.destroy()
    
#     bgimg = ImageTk.PhotoImage(Image.open("images/start.png").resize(screensize))
#     start_button_img = ImageTk.PhotoImage(Image.open("images/start_button.png").resize((280, 80)))
#     label1= Label(window1, image=bgimg)
    
#     Button(window1,image=start_button_img,borderwidth=0,command=category).place(x=545,y=360)
#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()


# category()
    

# main.py

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) > 1:
        operation = sys.argv[1]
        print(operation)
        logic(operation)
    else:
        print("No operation specified.")
