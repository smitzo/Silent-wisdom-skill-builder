import cv2
from datetime import datetime
import random
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import os
import sys

current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from insert_into_database import insert_gameplay_data
from dashboard_analytics import user_dashboard

def main(flag):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
    cv2.namedWindow('DISPLAY SCREEN',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    start_time = datetime.now()
    total_time =30
    cap = cv2.VideoCapture(0)
    num = random.randint(1,8)
    condition = ["GREATER THAN","LESS THAN","EQUALS TO"]
    index_val = random.randint(0,2)
    detector = HandDetector(maxHands=2, detectionCon=0.8)
    score =0
    while True:
        count =0
        current_time = datetime.now()
        difference = int((current_time-start_time).total_seconds())
        # print(difference)
        if difference>total_time:
            break
        bg = cv2.imread(os.getcwd()+"/assets/guessthenumber/guess_the_number_bg.png")
        _,img = cap.read()
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
        if index_val==0:
            if count>num:
                score+=10
                num = count
                if num==1:
                    index_val = 0
                elif num == 10:
                    index_val=1
                if index_val == 2:
                    index_val = random.randint(0,1)
                else:
                    index_val = random.randint(0,2)
        elif index_val==1:
            if count<num:
                score+=10
                num = count
                if num==1:
                    index_val = 0
                elif num == 10:
                    index_val=1
                if index_val == 2:
                    index_val = random.randint(0,1)
                else:
                    index_val = random.randint(0,2)
        if index_val==2:
            if count==num:
                score+=10
                num = count
                if num==1:
                    index_val = 0
                elif num == 10:
                    index_val=1
                if index_val == 2:
                    index_val = random.randint(0,1)
                else:
                    index_val = random.randint(0,2)
        if num==0:
            num = random.randint(1,9)
            index_val =0
        if num==10:
            num = random.randint(1,9)
            index_val =1
        
        cv2.putText(bg,str(score),(350,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
        cv2.putText(bg,str(total_time - difference),(1720,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
        cv2.putText(bg,str(count),(950,125),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),4)
        cv2.putText(bg,"DISPLAY A NUMBER",(145,500),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),6)
        cv2.putText(bg,condition[index_val]+" "+str(num),(250,600),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,0),6)
        img = cv2.resize(img,(840,760))
        bg[245:245+760,975:975+840]= img
        cv2.imshow("DISPLAY SCREEN",bg)
        # cv2.imshow("try",img)
        cv2.waitKey(1)
    score_img = cv2.imread(os.getcwd()+"/assets/guessthenumber/score.png")
    cv2.putText(score_img,str(score),(850,520),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),7)
    cv2.imshow("DISPLAY SCREEN",score_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    insert_gameplay_data(score,"reflex game")
    user_dashboard("reflex game")
main("hello")