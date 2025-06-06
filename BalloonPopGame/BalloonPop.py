# Import
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
import sqlite3
from tkinter import *
from PIL import Image, ImageTk 
import ctypes 
import os

#SOUND
import threading
from playsound import playsound

def wrong():
    playsound(os.getcwd()+'/wrong.mp3')

def correct():
    playsound(os.getcwd()+'/correct.mp3')


#SYSTEM SCREEN 
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
geometry =  str(screensize[0])+"x"+str(screensize[1])

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

#GUI window
# window1 = Tk()
# window1.geometry(geometry)
# window1.title("Balloon game")

def end_screen():
    cv2.namedWindow('DISPLAY SCREEN',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    score_img = cv2.imread(os.getcwd()+"/images/score.png")
    cv2.putText(score_img,str(score),(900,520),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),7)
    database = "database/login.sqlite3"
    conn = sqlite3.connect(database)

    cursor = conn.cursor()
    sql = "select balloon_score from user_data where name='Alice' "
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    
    cv2.imshow("DISPLAY SCREEN",score_img)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()



def gameplay(flag):
    # Initialize
    global cap
    global score
    pygame.init()

    # Create Window/Display
    width, height = 1280, 720
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop")

    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()
    num = random.randint(1,10)
    num1 = random.randint(1,10)
    pop_number=num
    imgBalloon = pygame.image.load(os.getcwd()+'/Resources/randomballoon/'+str(num)+'.png').convert_alpha()
    rectBalloon = imgBalloon.get_rect()
    imgBalloon1 = pygame.image.load(os.getcwd()+'/Resources/randomballoon/'+str(num1)+'.png').convert_alpha()
    rectBalloon1 = imgBalloon1.get_rect()
    rectBalloon1.x, rectBalloon1.y = 600, 300
    rectBalloon.x, rectBalloon.y = 200, 300
    # Images
    # def balloon1(number):
    #     global imgBalloon,rectBalloon
        
    #     # rectBalloon.x, rectBalloon.y = 500, 300
    #     rectBalloon.x = random.randint(100, img.shape[1] - 100)
    #     rectBalloon.y = img.shape[0] + 50

    # def balloon2(number1):
    #     global imgBalloon1,rectBalloon1
    #     
    #     # rectBalloon1.x, rectBalloon1.y = 600, 300
    #     rectBalloon1.x = random.randint(100, img.shape[1] - 100)
    #     rectBalloon1.y = img.shape[0] + 50

    # Variables
    speed = 10
    score = 0
    startTime = time.time()
    totalTime = 5
    # Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    word_number_list =['one','two','three','four','five','six','seven','eight','nine','ten']
    def resetBalloon():
        rectBalloon.x = random.randint(100, img.shape[1] - 100)
        rectBalloon.y = img.shape[0] + 50

    def resetBalloon1():
        rectBalloon1.x = random.randint(100, img.shape[1] - 100)
        rectBalloon1.y = img.shape[0] + 50

    # Main loop
    start = True
    bg = cv2.imread("images/balloon_down.png")
    while start:
        # Get Events
        pop_number=num
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()

        # Apply Logic
        timeRemain = int(totalTime -(time.time()-startTime))
        if timeRemain <0:
            pygame.quit()
            end_screen()
            
            # window.fill((255,255,255))

            # font = pygame.font.Font('./Resources/Marcellus-Regular.ttf', 50)
            # textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
            # textTime = font.render(f'Time UP', True, (50, 50, 255))
            # window.blit(textScore, (450, 350))
            # window.blit(textTime, (530, 275))

        else:
            # OpenCV
            
            bg = cv2.resize(bg,screensize)
            success, img = cap.read()
            img= cv2.resize(img,(1280,720))
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)
            rectBalloon.y -= speed  # Move the balloon up
            rectBalloon1.y -= speed
            # check if balloon has reached the top without pop
            if rectBalloon.y < 0:
                # resetBalloon()
                num = random.randint(1,10)
                imgBalloon = pygame.image.load('./Resources/randomballoon/'+str(num)+'.png').convert_alpha()
                rectBalloon = imgBalloon.get_rect()
                resetBalloon()
                speed += 1
            if rectBalloon1.y < 0:
                # resetBalloon1()
                num1 = random.randint(1,10)
                imgBalloon1 = pygame.image.load('./Resources/randomballoon/'+str(num1)+'.png').convert_alpha()
                rectBalloon1 = imgBalloon1.get_rect()
                resetBalloon1()
                speed += 1

            if hands:
                hand = hands[0]
                x, y = hand['lmList'][8][0:2]
                if rectBalloon.collidepoint(x, y):
                    if num==pop_number: 
                        score += 10
                        t1= threading.Thread(target=correct)
                        t1.start()
                    num = random.randint(1,10)
                    imgBalloon = pygame.image.load('./Resources/randomballoon/'+str(num)+'.png').convert_alpha()
                    rectBalloon = imgBalloon.get_rect()
                    resetBalloon()
                    speed += 1
                if rectBalloon1.collidepoint(x, y):
                    if num1==pop_number:
                        score += 10
                        t1= threading.Thread(target=correct)
                        t1.start()
                    # resetBalloon1()
                    num1 = random.randint(1,10)
                    imgBalloon1 = pygame.image.load('./Resources/randomballoon/'+str(num1)+'.png').convert_alpha()
                    rectBalloon1 = imgBalloon1.get_rect()
                    resetBalloon1()
                    speed += 1

            # img[185:665,55:1225]=cv2.resize(bg,(1170,480))
            img[0:80,0:1280]=cv2.resize(bg,(1280,80))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)
            window.blit(imgBalloon1, rectBalloon1)

            font = pygame.font.Font('./Resources/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Score: {score}', True, (255, 255, 255))
            textTime = font.render(f'Time: {timeRemain}', True, (255, 255, 255))
            word_to_pop = font.render(f'Number: {word_number_list[pop_number-1]}', True, (255, 255, 255))
            window.blit(textScore, (35, 10))
            window.blit(textTime, (1000, 10))
            window.blit(word_to_pop,(500,10))
            # print(num)
        # Update Display
        try:
            pygame.display.update()
        except:
            break
        # Set FPS
        clock.tick(fps)

# def start():
#     for widget in window1.winfo_children():
#         widget.destroy()
    
#     bgimg = ImageTk.PhotoImage(Image.open("start.png").resize(screensize))
#     start_button_img = ImageTk.PhotoImage(Image.open("start_button.png").resize((330, 120)))
#     label1= Label(window1, image=bgimg)
    
#     Button(window1,image=start_button_img,borderwidth=0,command=gameplay).place(x=470,y=270)
#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()

# if __name__=="__main__":
#     start()
gameplay("try")
