import cv2
import random
from datetime import datetime
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import os
import sys
current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from insert_into_database import insert_gameplay_data
from dashboard_analytics import user_dashboard
from playsound import playsound
import threading
working_dir = '/BalloonPopGame/'
def wrong():
    playsound(os.getcwd() + working_dir + 'wrong.mp3')

def correct():
    playsound(os.getcwd() + working_dir + 'correct.mp3')


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5) 
def number_generation():
    l=[1,2,3,4,5,6,7,8,9,10]
    values = random.sample(l,4)
    predict = random.sample(values,1)
    predict_index_value =values.index(predict[0])
    return values,predict,predict_index_value

def main(flag):
    current_directory = os.getcwd()+ "/assets/cardreasoning/"
    coordinate_values= [(175,600),(625,600),(1100,600),(1550,600)]
    # rectangle_coordinate = [[(75,250),(500,900)]]
    # print(values,predict[0])
    cv2.namedWindow('DISPLAY SCREEN',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    values,predict,predict_index_value = number_generation()
    score =0
    detector = HandDetector(maxHands=2, detectionCon=0.8)
    cap = cv2.VideoCapture(0)
    start_time = datetime.now()
    start_time1= datetime.now()
    game_time =20
    while True:
        count=0
        current_time = datetime.now()
        termination_time = int((current_time-start_time1).total_seconds())
        time_difference = int((current_time-start_time).total_seconds())
        bg = cv2.imread(current_directory+"cards.png")
        if termination_time>game_time:
            print("terminating")
            break
        if time_difference<=5:
            for i in range(len(values)):
                cv2.putText(bg,str(values[i]),coordinate_values[i],cv2.FONT_HERSHEY_SIMPLEX,6,(0,0,0),10)
        # cv2.rectangle(bg,rectangle_coordinate[0][0],rectangle_coordinate[0][1],(0,0,255),5,cv2.LINE_4)
            # cv2.putText(bg,str(count),(320,125),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),5)
            cv2.putText(bg,str(score),(340,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
            cv2.putText(bg,str(game_time - termination_time),(1720,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
        elif 5<time_difference<10:
            _,img = cap.read()
            bg = cv2.imread(current_directory+str(predict_index_value)+".png")
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
            # print(predict,score)
            if count==predict[0]:
                score+=10
                start_time=current_time
                values,predict,predict_index_value = number_generation()
                t1 = threading.Thread(target=correct)
                t1.start()

            cv2.putText(bg,str(score),(350,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
            cv2.putText(bg,str(game_time - termination_time),(1720,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
            cv2.putText(bg,str(count),(950,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
        else:
            start_time=current_time
            values,predict,predict_index_value = number_generation()
        # print(time_difference)
        cv2.imshow("DISPLAY SCREEN",bg)
        cv2.waitKey(1)
    score_img = cv2.imread(current_directory+"score.png")
    cv2.putText(score_img,str(score),(900,520),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),7)
    cv2.imshow("DISPLAY SCREEN",score_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    insert_gameplay_data(score,"memorizing numbers")
    user_dashboard("memorizing numbers")
main('try')