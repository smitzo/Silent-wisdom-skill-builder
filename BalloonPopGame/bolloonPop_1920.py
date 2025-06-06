# Import
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import os
import sys
# SOUND
import threading
from playsound import playsound

current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from dashboard_analytics import user_dashboard
from insert_into_database import insert_gameplay_data

working_dir = '/BalloonPopGame/'
def wrong():
    playsound(os.getcwd() + working_dir + 'wrong.mp3')

def correct():
    playsound(os.getcwd() + working_dir + 'correct.mp3')


# SYSTEM SCREEN
user32 = ctypes.windll.user32
screensize = (1920, 1080)  # Change to the desired resolution (1920x1080 in this case)
geometry = str(screensize[0]) + "x" + str(screensize[1])

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # width
cap.set(4, 1080)  # height

# GUI window
# window1 = Tk()
# window1.geometry(geometry)
# window1.title("Balloon game")

def end_screen():
    cv2.namedWindow('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('DISPLAY SCREEN', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    score_img = cv2.imread(os.getcwd() + working_dir + "Resources/score.png")
    cv2.putText(score_img, "Score", (750, 500), cv2.FONT_HERSHEY_SIMPLEX, 5, (14, 53, 138), 10)
    cv2.putText(score_img, str(score), (900, 700), cv2.FONT_HERSHEY_SIMPLEX, 5, (14, 53, 138), 10)
    cv2.imshow("DISPLAY SCREEN", score_img)
    cv2.waitKey(5000)
    # Load an image from file
    # image = cv2.imread('Autistic.png')

    # # Check if the image was successfully loaded
    # if image is None:
    #     print("Error: Could not read the image.")
    #     exit()

    # # Define the rectangle parameters (top-left and bottom-right corners)
    # rect_start_point = (521, 343)
    # rect_end_point = (867, 420)

    # # Specify rectangle color
    # color = (0, 255, 0)  # Green color in BGR

    # # Fill the rectangle on the image
    # cv2.rectangle(image, rect_start_point, rect_end_point, color, thickness=-1)
    # cv2.rectangle(image, (521,507),(867,583) , color, thickness=-1)
    # cv2.rectangle(image, (521,670),(880,748), color, thickness=-1)
    # cv2.rectangle(image, (521,835),(835,912), color, thickness=-1)
    # cv2.rectangle(image, rect_start_point, rect_end_point, color, thickness=-1)

    # Display the image with the filled rectangle
    # cv2.imshow('Image with Filled Rectangle', image)
    # cv2.waitKey(5000)
    # cv2.destroyAllWindows()
    insert_gameplay_data(score,"balloon game")
    user_dashboard("balloon game")

def gameplay(flag):
    # Initialize
    global cap
    global score
    pygame.init()

    # Create Window/Display
    width, height = 1920, 1080
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop")

    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()
    num = random.randint(1, 10)
    num1 = random.randint(1, 10)
    pop_number = num
    imgBalloon = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num) + '.png').convert_alpha()
    rectBalloon = imgBalloon.get_rect()
    imgBalloon1 = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num1) + '.png').convert_alpha()
    rectBalloon1 = imgBalloon1.get_rect()
    rectBalloon1.x, rectBalloon1.y = 960, 540
    rectBalloon.x, rectBalloon.y = 480, 540

    # Variables
    speed = 10
    score = 0
    startTime = time.time()
    totalTime = 30

    # Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    word_number_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    def resetBalloon():
        rectBalloon.x = random.randint(100, 1820)
        rectBalloon.y = 1080 + 50

    def resetBalloon1():
        rectBalloon1.x = random.randint(100, 1820)
        rectBalloon1.y = 1080 + 50

    # Main loop
    start = True
    bg = cv2.imread(os.getcwd() + working_dir + "Resources/balloon_down.png")
    while start:
        # Get Events
        pop_number = num
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()

        # Apply Logic
        timeRemain = int(totalTime - (time.time() - startTime))
        if timeRemain < 0:
            pygame.quit()
            end_screen()

        else:
            # OpenCV
            bg = cv2.resize(bg, screensize)
            success, img = cap.read()
            img = cv2.resize(img, (1920, 1080))
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)
            rectBalloon.y -= speed  # Move the balloon up
            rectBalloon1.y -= speed

            # check if balloon has reached the top without pop
            if rectBalloon.y < 0:
                num = random.randint(1, 10)
                imgBalloon = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num) + '.png').convert_alpha()
                rectBalloon = imgBalloon.get_rect()
                resetBalloon()
                speed += 1

            if rectBalloon1.y < 0:
                num1 = random.randint(1, 10)
                imgBalloon1 = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num1) + '.png').convert_alpha()
                rectBalloon1 = imgBalloon1.get_rect()
                resetBalloon1()
                speed += 1

            if hands:
                hand = hands[0]
                x, y = hand['lmList'][8][0:2]
                if rectBalloon.collidepoint(x, y):
                    if num == pop_number:
                        score += 10
                        t1 = threading.Thread(target=correct)
                        t1.start()
                    num = random.randint(1, 10)
                    imgBalloon = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num) + '.png').convert_alpha()
                    rectBalloon = imgBalloon.get_rect()
                    resetBalloon()
                    speed += 1
                if rectBalloon1.collidepoint(x, y):
                    if num1 == pop_number:
                        score += 10
                        t1 = threading.Thread(target=correct)
                        t1.start()
                    num1 = random.randint(1, 10)
                    imgBalloon1 = pygame.image.load(os.getcwd() + working_dir + 'Resources/randomballoon/' + str(num1) + '.png').convert_alpha()
                    rectBalloon1 = imgBalloon1.get_rect()
                    resetBalloon1()
                    speed += 1

            img[0:80, 0:1920] = cv2.resize(bg, (1920, 80))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)

            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)
            window.blit(imgBalloon1, rectBalloon1)

            font = pygame.font.Font(os.getcwd() + working_dir + 'Resources/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Score: {score}', True, (255, 255, 255))
            textTime = font.render(f'Time: {timeRemain}', True, (255, 255, 255))
            word_to_pop = font.render(f'Number: {word_number_list[pop_number - 1]}', True, (255, 255, 255))
            window.blit(textScore, (35, 10))
            window.blit(textTime, (1500, 10))
            window.blit(word_to_pop, (750, 10))

        # Update Display
        try:
            pygame.display.update()
        except:
            break

        # Set FPS
        clock.tick(fps)
    return score
# def start():
#     for widget in window1.winfo_children():
#         widget.destroy()

#     bgimg = ImageTk.PhotoImage(Image.open("start.png").resize(screensize))
#     start_button_img = ImageTk.PhotoImage(Image.open("start_button.png").resize((330, 120)))
#     label1= Label(window1, image=bgimg)
#
#     Button(window1,image=start_button_img,borderwidth=0,command=gameplay).place(x=470,y=270)
#     label1.place(x=0,y=0)
#     window1.wm_attributes('-fullscreen', 'True')
#     window1.mainloop()

# if __name__=="__main__":
#     start()
gameplay("try")
