import customtkinter as ck 
import ctypes
import pandas as pd 
import numpy as np 
import pickle 
import mediapipe as mp
import cv2
import os
from PIL import Image, ImageTk 
from landmarks import landmarks
from tkinter import *
from PIL import Image, ImageTk 
import ctypes 
from datetime import datetime 
from functools import partial
import sys
import joblib



current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from insert_into_database import insert_gameplay_data
from dashboard_analytics import user_dashboard
#SYSTEM SCREEN 
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
geometry =  str(screensize[0])+"x"+str(screensize[1])

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 

working_dir = os.getcwd()+"/fitnessExercise/assets/"
#GUI window
# window1 = Tk()
# window1.geometry(geometry)
# window1.title("Workout")
# window = Tk()

# window.geometry("1920x1080")
# window.configure(bg = "#FFFFFF")

# Load the model using joblib
#model = joblib.load(working_dir + 'deadlift.pkl', 'rb')

with open(working_dir + 'deadlift.pkl', 'rb') as f: 
    model = pickle.load(f)

cap = cv2.VideoCapture(0)

def main(category):
    # for widget in window1.winfo_children():
    #     widget.destroy()
    current_stage = ''
    counter = 0 
    bodylang_prob = np.array([0,0]) 
    bodylang_class = ''
    start_time = datetime.now()
    total_time =20
    while True:
        current_time = datetime.now()
        total_seconds = (current_time-start_time).total_seconds()
        if total_seconds>total_time:
            break
        bg = cv2.imread(working_dir + "bg.png")
        refrence_image = cv2.imread(working_dir + category +"_image.png")
        ret, image = cap.read()
        image = cv2.flip(image, 1)
        #image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        results = pose.process(image)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, 
            mp_drawing.DrawingSpec(color=(106,13,173), thickness=4, circle_radius = 5), 
            mp_drawing.DrawingSpec(color=(255,102,0), thickness=5, circle_radius = 10)) 

        try: 
            row = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten().tolist()
            X = pd.DataFrame([row], columns = landmarks) 
            bodylang_prob = model.predict_proba(X)[0]
            bodylang_class = model.predict(X)[0] 

            if bodylang_class =="down" and bodylang_prob[bodylang_prob.argmax()] > 0.5: 
                current_stage = "down" 
            elif current_stage == "down" and bodylang_class == "up" and bodylang_prob[bodylang_prob.argmax()] > 0.5:
                current_stage = "up" 
                counter += 10 
        except Exception as e: 
            print(e)

        image = cv2.resize(image,screensize)
        #cv2.rectangle(image, (50,50), (200,100), (255,0,0),-1)
        #cv2.rectangle(image, (550,50), (700,100), (255,0,0),-1)
        #cv2.rectangle(image, (1050,50), (1200,100), (255,0,0),-1)
        cv2.putText(bg,str(counter),(200,200),cv2.FONT_HERSHEY_DUPLEX,2,(0, 0, 0),3,cv2.LINE_4)
        cv2.putText(bg,bodylang_class,(620,200),cv2.FONT_HERSHEY_DUPLEX,2,(0, 0, 0),3,cv2.LINE_4)
        cv2.putText(bg,str(bodylang_prob[bodylang_prob.argmax()]),(1135,200),cv2.FONT_HERSHEY_DUPLEX,2,(0,0, 0),3,cv2.LINE_4)
        cv2.putText(bg,str(int(total_time-total_seconds)),(1620,200),cv2.FONT_HERSHEY_DUPLEX,2,(0, 0, 0),3,cv2.LINE_4)
        cv2.namedWindow('DISPLAY SCREEN',cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        bg[366:1011,74:830]=cv2.resize(image,(756,645))
        bg[366:1011,1097:1853]=cv2.resize(refrence_image,(756,645))

        cv2.imshow("DISPLAY SCREEN",bg)
        cv2.waitKey(1)

        if cv2.waitKey(1)  & 0xff==ord('q'):
                break
        
    cv2.namedWindow('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    score_img = cv2.imread(working_dir + "score.png")
    cv2.putText(score_img, "Score", (750, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (14, 53, 138), 10)
    cv2.putText(score_img, str(counter), (900, 700), cv2.FONT_HERSHEY_SIMPLEX, 5, (14, 53, 138), 10)
    cv2.imshow("DISPLAY SCREEN", score_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    insert_gameplay_data(counter,"physical fitness")
    user_dashboard("physical fitness")
if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) > 1:
        operation = sys.argv[1]
        print(operation)
        main(operation)
    else:
        print("No operation specified.")
    # main("squats")
    # bgimg3 = ImageTk.PhotoImage(Image.open(working_dir + "result.png").resize(screensize))
    # back_button_img = ImageTk.PhotoImage(Image.open(working_dir + "home.png").resize((215, 105)))
    # label1= Label(window1, image=bgimg3)
    # Label(label1,text = str(int(counter)),font="Helvetica 60 bold").place(x = 940,y = 470)
    # Button(window1,image=back_button_img,borderwidth=0,command=start).place(x=850,y=755)
    # #Button(window1,image=squats_button_img,borderwidth=0,command=main).place(x=550,y=530)
    # label1.place(x=0,y=0)
    # window1.wm_attributes('-fullscreen', 'True')
    # window1.mainloop()

# main("squats")
# def category():
#     for widget in window1.winfo_children():
#         widget.destroy()
    
#     bgimg1 = ImageTk.PhotoImage(Image.open(working_dir + "category.png").resize(screensize))
#     high_jump_button_img = ImageTk.PhotoImage(Image.open(working_dir + "high_jump_button.png").resize((425, 120)))
#     squats_button_img = ImageTk.PhotoImage(Image.open(working_dir + "squats_button.png").resize((425, 120)))
#     label1= Label(window1, image=bgimg1)
#     Button(window1,image=high_jump_button_img,borderwidth=0,command=partial(main,"high_jump")).place(x=735,y=480)
#     Button(window1,image=squats_button_img,borderwidth=0,command=partial(main,"squats")).place(x=735,y=780)
#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()
    
# def start():
#     for widget in window1.winfo_children():
#         widget.destroy()
    
#     bgimg = ImageTk.PhotoImage(Image.open(working_dir + "start.png").resize(screensize))
#     start_button_img = ImageTk.PhotoImage(Image.open(working_dir + "start_button.png").resize((315, 95)))
#     label1= Label(window1, image=bgimg)
    
#     Button(window1,image=start_button_img,borderwidth=0,command=category).place(x=795,y=880)
#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()

# start()
#main()
# category()