##########################################################  LIBRARIES   ############################################################
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from functools import partial
import os
import sys
import subprocess
import vlc
import tkinter as tk
from tkinter import Frame
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Ellipse
from reportlab.graphics import renderPDF
import sqlite3
import os
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
os.add_dll_directory(os.getcwd())
current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from dashboard_analytics import user_dashboard
#####################################################################################################################################
name=""
age=0
contact = 0
city = ""
email = ""
password = ""

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/start/")


def relative_to_assets(ASSETS_PATH,path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1920x1080")
window.wm_attributes('-fullscreen', 'True')
window_height, window_width = window.winfo_screenheight(),window.winfo_screenwidth()
window.configure(bg = "#C4C4C4")
animated_selected =False
exercise_selected = False
main_module_selected=''
student_type = ""
########################################################################################################################################
def video_player(url):
    try:
        instance = vlc.Instance('--no-xlib')
        player = instance.media_player_new()
        media = instance.media_new(url)
        player.set_media(media)
    except Exception as e:
        print(f"Error initializing VLC player: {e}")
        return

    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Set the window to full screen

    # Create a frame for the video
    video_frame = Frame(root)
    video_frame.pack(fill="both", expand=True)

    # Set up the video window
    try:
        player.set_hwnd(video_frame.winfo_id())
    except Exception as e:
        print(f"Error setting up video window: {e}")
        root.destroy()
        return

    def play():
        player.play()

    def stop(event):
        player.stop()
        root.destroy()
        return

    # Bind the 'e' key to the stop function
    root.bind('e', stop)

    try:
        play()
        root.mainloop()
    except Exception as e:
        print(f"Error running the main loop: {e}")

###########################################################################################################################################3


def final_score_card(selected_module):
    global animated_selected, exercise_selected
    # balloon_game, object_detection, animated_stories, physical_fitness
    # alphabets_sign, digits_sign, emotions_understanding, emergency_sign
    # enhancing_communication, word_document_writing, keyboard_typing
    print(selected_module,main_module_selected)

    if selected_module == "balloon_game":
        command = "python BalloonPopGame/bolloonPop_1920.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return balloon game")

    elif selected_module == "calculation_reflex":
        command = "python GuessTheNumber/main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return calculation reflection")

    elif selected_module == "education_rights":
        command = "python education_rights/education_rights_cvm.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return education rights")

    elif selected_module == "ngo_information":
        command = "python ngo_information/ngo_info_cvm.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return ngo information")

    elif selected_module == "scholarship_information":
        command = "python scholarship_information/scholarship_awareness_cvm.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return scholarship information")
    elif selected_module == "employment_and_general_rights":
        command = "python employment_and_general_rights/employmentandgeneralrights.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return calculation reflection")
    
    elif selected_module == "cardreasoning":
        command = "python CardReasoning\shuffle_card.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return quiz")

    elif selected_module == "body_parts_detection":
        command = "python bodyparts/body_parts_main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from body parts detection")

    elif selected_module == "autism_legal_awareness":
        command = "python autism_legal_awareness/main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from body parts detection")

    elif selected_module in ["addition","subtraction","multiplication","division"]:
        command = "python arithmetic_module/main.py "+ selected_module
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from arithmetic module detection")
    
    elif selected_module == "autism_ngo":
        command = "python autistic_ngo/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic ngo module detection")

    elif selected_module == "resume_building":
        command = "python resume_module_final/resume_module_final/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic ngo module detection")

    elif selected_module == "deaf_legal":
        command = "python deaf_legal/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic deaf legal")

    elif selected_module == "dumb_legal":
        command = "python dumb_legal/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic deaf legal")
    

    elif selected_module == "deaf_ngo":
        command = "python deaf_ngo/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic ngo module detection")

    elif selected_module == "dumb_ngo":
        command = "python dumb_ngo/main.py"
        print(command)
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from autistic ngo module detection")

    elif selected_module == "digits_sign":
        command = "python digits_recognition/main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return digits_sign game")

    elif selected_module == "shape_matching":
        command = "python shape_matching/shape_identification_main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from shape matching")

    elif selected_module == "emotions_understanding":
        command = "python emotion_detection/EmotionDetection.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from emotion detection")
    
    elif selected_module == "general_rights":
        command = "python general_legal_awareness/legal.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from general rights")
    
    elif selected_module == "scholarships":
        command = "python scholarship_awareness/main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from scholarship_awareness")
        
    
    elif selected_module == "enhancing_communication":
        command = "python coummnication_module/main.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return from emotion detection")
        
    elif selected_module in ["education_rights.mp4","employment_video.mp4"]:
        video_url = os.getcwd()+"/assets/indusrial_skill_development_options/legal_knowledge_video_content/"+selected_module+".mp4"
        video_player(video_url)
        animated_selected = False

    
    elif selected_module == "keyboard_typing":
        command = "python keyboard_typing/keyboard_typing_updated.py"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return keyboard typing")
    
    elif selected_module in ['bad_touch', 'child_labour_education', 'crocodile_story', 'gender_equality', 'growing_up_healthy', 'gullak', 'healthy_lifestyle', 'internal_safety', 'mental_health', 'Module 5 Gender EqualityHindi_1080p', 'never_give_up', 'nutrition_sanitation', 'panchatantra', 'substance_misuse', 'true_friend', 'values_citizenship']:
        video_url = os.getcwd()+"/video_content/"+selected_module+".mp4"
        print(video_url)
        video_player(video_url)
        animated_selected = False

    elif selected_module in ["high_jump","squats"]:
        command = "python fitnessExercise/main_1920.py "+selected_module
        process = subprocess.Popen(command, shell=True)
        process.wait()
        print("successfully return physical fitness exercise")
        animated_selected = False

#    elif selected_module == "quiz":
#        command="python quiz/main.py "
#        process=subprocess.Popen(command,shell=True)
#        process.wait()
#        print("succesfully return from quiz")
    # start()
#redirect to 
    main_module_selection(student_type)

############################################################        INDUSTRIAL MODULE   #########################################################################################
def rights_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/indusrial_skill_development_options/legal_knowledge_module_selection/employment_and_education_rights")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(industrial_module_selection),
        relief="flat"
    )
    button_1.place(
        x=25.0,
        y=4.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"education_rights"),
        relief="flat"
    )
    button_2.place(
        x=302.0,
        y=216.0,
        width=537.0,
        height=649.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png")),
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"employment_video"),
        relief="flat"
    )
    button_3.place(
        x=1081.0,
        y=216.0,
        width=537.0,
        height=649.0
    )
    window.resizable(False, False)
    window.mainloop()

def legal_module_selection() :
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/indusrial_skill_development_options/legal_knowledge_module_selection")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(industrial_module_selection),
        relief="flat"
    )
    button_1.place(
        x=25.0,
        y=4.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(rights_selection),
        relief="flat"
    )
    button_2.place(
        x=107.0,
        y=256.0,
        width=526.0,
        height=663.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"general_rights"),
        relief="flat"
    )
    button_3.place(
        x=684.0,
        y=255.0,
        width=526.0,
        height=663.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"scholarships"),
        relief="flat",
        
    )
    print("suceesfully return from scholarships")
    button_4.place(
        x=1261.0,
        y=254.0,
        width=526.0,
        height=663.0
    )
    window.resizable(False, False)
    window.mainloop()


def industrial_module_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/indusrial_skill_development_options")
    for widget in window.winfo_children():
            widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"education_rights"),
        relief="flat"
    )
    button_1.place(
        x=214.0,
        y=149.0,
        width=349.0,
        height=416.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= partial(final_score_card,"ngo_information"),
        relief="flat"
    )
    button_2.place(
        x=219.0,
        y=641.0,
        width=349.0,
        height=416.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"employment_and_general_rights"),
        relief="flat"
    )
    button_3.place(
        x=755.0,
        y=149.0,
        width=349.0,
        height=416.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"resume_building"),
        relief="flat"
    )
    button_4.place(
        x=760.0,
        y=641.0,
        width=349.0,
        height=416.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"keyboard_typing"),
        relief="flat"
    )
    button_5.place(
        x=1300.0,
        y=150.0,
        width=349.0,
        height=416.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"scholarship_information"),
        relief="flat"
    )
    button_6.place(
        x=1301.0,
        y=641.0,
        width=349.0,
        height=416.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command= partial(main_module_selection),
        relief="flat"
    )
    button_7.place(
        x=25.0,
        y=4.0,
        width=92.0,
        height=78.0
    )
    window.resizable(False, False)
    window.mainloop()


######################################################################  LEARNING MODULE ###################################################################################3

def arithmetic_module_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/arithmetic_module")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#088395",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(learning_module_selection),
        relief="flat"
        #print ("back to learning module selection")
    )
    button_1.place(
        x=25.0,
        y=4.0,
        width=110.98795318603516,
        height=94.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button (
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"addition"),
        relief="flat"
        #print ("addition selected")
    )
    button_2.place(
        x=89.0,
        y=292.0,
        width=411.0,
        height=474.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"subtraction"),
        relief="flat"
        #print("subtraction selected")
    )
    button_3.place(
        x=533.0,
        y=292.0,
        width=411.0,
        height=474.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"multiplication"),
        relief="flat"
        #print("multiplication selected")
    )
    button_4.place(
        x=977.0,
        y=292.0,
        width=411.0,
        height=474.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"division"),
        relief="flat"
        #print ("division selected")
    )
    button_5.place(
        x=1421.0,
        y=292.0,
        width=411.0,
        height=474.0
    )
    window.resizable(False, False)
    window.mainloop()

def deaf_dumb_module_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/deaf_dumb_module_options")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#088395",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(main_module_selection),
        relief="flat"
    )
    button_1.place(
        x=25.0,
        y=4.0,
        width=110.98795318603516,
        height=94.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= partial(arithmetic_module_selection),
        relief="flat"
    )
    button_2.place(
        x=182.0,
        y=289.0,
        width=422.0,
        height=490.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card, "digits_sign"),
        relief="flat"
        #print ("digits sign module selected")
    )
    button_3.place(
        x=751.0,
        y=289.0,
        width=422.0,
        height=490.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card, "emotions_understanding"),
        relief="flat"
        #print("emotions understanding module selected")
    )
    button_4.place(
        x=1320.0,
        y=289.0,
        width=422.0,
        height=490.0
    )
    window.resizable(False, False)
    window.mainloop()




##################################### animated stories content for dumb ##############################################################
def moral_stories():
    global animated_selected
    animated_selected=True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection/moral_stories")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection),
        relief="flat"
        #print("back to gamification module selection")
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"panchatantra"),
        relief="flat"
        #print ("panchtantra selected")
    )
    button_2.place(
        x=284.0,
        y=321.0,
        width=351.0,
        height=436.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"gullak"),
        relief="flat"
        #print ("gullak selected")
    )
    button_3.place(
        x=785.0,
        y=323.0,
        width=351.0,
        height=436.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"crocodile_story"),
        relief="flat"
        #print ("crocodile story selected")
    )
    button_4.place(
        x=1286.0,
        y=323.0,
        width=351.0,
        height=436.0
    )
    
    window.mainloop()

def health_stories():
    global animated_selected
    animated_selected=True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection/health_stories")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"healthy_lifestyle"),
        relief="flat"
    )
    button_2.place(
        x=109.0,
        y=317.0,
        width=354.0,
        height=454.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"nutrition_sanitation"),
        relief="flat"
    )
    button_3.place(
        x=558.0,
        y=313.0,
        width=354.0,
        height=454.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"growing_up_healthy"),
        relief="flat"
    )
    button_4.place(
        x=1007.0,
        y=309.0,
        width=354.0,
        height=454.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"mental_health"),
        relief="flat"
    )
    button_5.place(
        x=1456.0,
        y=305.0,
        width=354.0,
        height=454.0
    )
    window.resizable(False, False)
    window.mainloop()

def social_issues():
    global animated_selected
    animated_selected=True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection/social_issues/")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"child_labour_education"),
        relief="flat"
    )
    button_2.place(
        x=106.0,
        y=306.0,
        width=345.0,
        height=468.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"values_citizenship"),
        relief="flat"
    )
    button_3.place(
        x=554.0,
        y=306.0,
        width=345.0,
        height=468.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"gender_equality"),
        relief="flat"
    )
    button_4.place(
        x=1002.0,
        y=306.0,
        width=345.0,
        height=468.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH ,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"substance_misuse"),
        relief="flat"
    )
    button_5.place(
        x=1450.0,
        y=306.0,
        width=345.0,
        height=468.0
    )
    window.resizable(False, False)
    window.mainloop()



def security_and_safety():
    global animated_selected
    animated_selected=True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection/security_and_safety")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= partial(animated_stories_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"bad_touch"),
        relief="flat"
    )
    button_2.place(
        x=453.0,
        y=275.0,
        width=429.0,
        height=524.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"internal_safety"),
        relief="flat"
    )
    button_3.place(
        x=1022.0,
        y=275.0,
        width=429.0,
        height=524.0
    )
    window.resizable(False, False)
    window.mainloop()



def motivation_stories():
    global animated_selected
    animated_selected=True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection/motivational_stories")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"never_give_up"),
        relief="flat"
    )
    button_2.place(
        x=453.0,
        y=275.0,
        width=429.0,
        height=524.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"true_friend"),
        relief="flat"
    )
    button_3.place(
        x=1022.0,
        y=275.0,
        width=429.0,
        height=524.0
    )
    window.resizable(False, False)
    window.mainloop()

def animated_stories_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/animated_stories_selection")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(learning_module_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(moral_stories),
        relief="flat"
    )
    button_2.place(
        x=246.0,
        y=149.0,
        width=362.0,
        height=427.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(health_stories),
        relief="flat"
    )
    button_3.place(
        x=512.0,
        y=623.0,
        width=362.0,
        height=427.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=partial(motivation_stories),
        relief="flat"
    )
    button_4.place(
        x=778.0,
        y=149.0,
        width=362.0,
        height=427.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=partial(social_issues),
        relief="flat"
    )
    button_5.place(
        x=1044.0,
        y=623.0,
        width=362.0,
        height=427.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command= partial(security_and_safety),
        relief="flat"
    )
    button_6.place(
        x=1310.0,
        y=149.0,
        width=362.0,
        height=427.0
    )

    window.mainloop()
    

########################################################################################################################################################
    
def exercise_selection():
    global exercise_selected
    exercise_selected = True
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options/exercise_selection")
    for widget in window.winfo_children():
        widget.destroy()

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"high_jump"),
        relief="flat"
    )
    button_1.place(
        x=337.0,
        y=253.0,
        width=470.0,
        height=542.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"squats"),
        relief="flat"
    )
    button_2.place(
        x=1023.0,
        y=244.0,
        width=470.0,
        height=542.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command= partial(animated_stories_selection),
        relief="flat"
    )
    button_3.place(
        x=21.0,
        y=16.0,
        width=92.0,
        height=78.0
    )
    window.mainloop()

###################################################################################################################################################
def quiz():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/quiz")
    #delete previous interface 
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    pass
   
def gamification_module_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/gamification_module_options")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#A0A0A0",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card, "balloon_game"),
        relief="flat"
    )
    button_1.place(
        x=39.0,
        y=281.0,
        width=422.0,
        height=517.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card, "body_parts_detection"),
        relief="flat"
    )
    button_2.place(
        x=489.0,
        y=281.0,
        width=422.0,
        height=517.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection, "animated_stories"),
        relief="flat"
    )
    button_3.place(
        x=939.0,
        y=281.0,
        width=422.0,
        height=517.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        # command=partial(final_score_card, "physical_fitness"),
        command=partial(exercise_selection),
        relief="flat"
    )
    button_4.place(
        x=1389.0,
        y=281.0,
        width=422.0,
        height=517.0
    )
    button_image_5 = PhotoImage(
    file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=learning_module_selection,
        relief="flat"
    )
    button_5.place(
        x=19.0,
        y=3.0,
        width=110.98797607421875,
        height=94.0
    )
    window.mainloop()


#####################################################################################################################################
#redirect to main module selection
def learning_module_selection():
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/learning_module_options")
    for widget in window.winfo_children():
        widget.destroy()

    print(student_type)
    canvas = Canvas(
    window,
    bg = "#A0A0A0",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(main_module_selection),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=11.0,
        width=92.0,
        height=78.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(animated_stories_selection),
        relief="flat"
    )
    button_2.place(
        x=112.0,
        y=149.0,
        width=334.0,
        height=398.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(exercise_selection),
        relief="flat"
    )
    button_3.place(
        x=121.0,
        y=596.0,
        width=334.0,
        height=398.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command= partial(arithmetic_module_selection),
        relief="flat"
    )
    button_4.place(
        x=566.0,
        y=152.0,
        width=334.0,
        height=398.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command= partial(final_score_card,"calculation_reflex"),
        relief="flat"
    )
    button_5.place(
        x=575.0,
        y=599.0,
        width=334.0,
        height=398.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"balloon_game"),
        relief="flat"
    )
    button_6.place(
        x=1020.0,
        y=155.0,
        width=334.0,
        height=398.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"cardreasoning"),
        relief="flat"
    )
    button_7.place(
        x=1029.0,
        y=602.0,
        width=334.0,
        height=398.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"digits_sign"),
        relief="flat"
    )
    button_8.place(
        x=1474.0,
        y=158.0,
        width=334.0,
        height=398.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=partial(final_score_card,"emotions_understanding"),
        relief="flat"
    )
    button_9.place(
        x=1483.0,
        y=605.0,
        width=334.0,
        height=398.0
    )
    window.resizable(False, False)
    window.mainloop()



# def dashboard():
#     conn = sqlite3.connect('analytics.db')
#     cursor = conn.cursor()
#     with open('current.txt', 'r') as file:
#         email = file.read()
#     print(email)
#     # user_data = get_users_data(email)

#     # Query to fetch score and attempts for each category of the user
#     cursor.execute("""
#         SELECT * FROM gameplay
#         WHERE email = ?
#         GROUP BY category
#     """, (email,))

#     # Fetch all rows from the result set
#     rows = cursor.fetchall()

#     # Print the score and attempts for each category
#     print("Score and Attempts for User ID", email)
#     for row in rows:
#         print(row)

#     # Close the connection
#     conn.close()


def insert_signup_info(name, age, city ,contact, email, password,category):
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Execute the INSERT query to insert sign-up information into the users table
    cursor.execute("INSERT INTO users (name, age, contact, city, email, password,category) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (name, age, contact, city, email, password,category))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
################################################################################################################################################3
#redirects to learning_module_selection or industrial_module_selection
def main_module_selection(selected_student = None):
    global signin_name,signin_password
    # signin_name = ""
    # signin_password = ""
    try :
        signin_name = enter_name.get()
        signin_password = enter_password.get()
    except:
        print("Not updating values..")
    # print(enter_name.get())
    # establish connection with database
    # print(selected_student)
    file = open('current.txt', 'w')
    if selected_student:
        print(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),entry_6.get(),entry_7.get(),entry_8.get())
        insert_signup_info(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),entry_6.get(),entry_8.get())
        file.write(str(entry_5.get()))
    else:
        try:
            # file.write(enter_name.get())
            # print(enter_name.get(),enter_password.get())
            # if not check_credentials(enter_name.get(),enter_password.get()):
            #     signin()
            file.write(signin_name)
            print(signin_name,signin_password)
            if not check_credentials(signin_name,signin_password):
                signin()
        except:
            print("value not fetching..")       
        # pass
    file.close()
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/main_module_options")
    for widget in window.winfo_children():
        widget.destroy()
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(learning_module_selection),
        relief="flat"
    )
    button_1.place(
        x=381.0,
        y=241.0,
        width=510.0,
        height=594.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(industrial_module_selection),
        relief="flat"
    )
    button_2.place(
        x=1023.0,
        y=241.0,
        width=510.0,
        height=594.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(user_dashboard),
        relief="flat"
    )
    button_3.place(
        x=1657.0,
        y=22.0,
        width=236.0,
        height=82.0
    )
    window.resizable(False, False)
    window.mainloop()

############################################################################################################################
def student_type_selection(flag):
    global name
    global entry_1,entry_2,entry_3,entry_4,entry_5,entry_6
    if flag:
        enter_data(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),entry_6.get())
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/student_type")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(main_module_selection,"autistic"),
        relief="flat"
    )
    button_1.place(
        x=106.0,
        y=211.0,
        width=522.0,
        height=656.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=partial(main_module_selection,"deaf"),
        relief="flat"
    )
    button_2.place(
        x=699.0,
        y=212.0,
        width=522.0,
        height=656.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=partial(main_module_selection,"dumb"),
        relief="flat"
    )
    button_3.place(
        x=1292.0,
        y=213.0,
        width=522.0,
        height=656.0
    )
    window.resizable(False, False)
    window.mainloop()


####################################### Login and sign in   ############################################################33


# redirects to signup and signin
def start():
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#32807C",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: student_type_selection(),
        relief="flat"
    )
    button_1.place(
        x=666.0,
        y=406.0,
        width=589.0,
        height=267.0
    )
    window.resizable(False, False)
    window.mainloop()



# global variables
# Example usage
output_pdf_path = 'output.pdf'


def send_mail(sender,reciever,password,name,pdf_file_path):
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    FROM_EMAIL = sender
    TO_EMAIL = reciever
    PASSWORD = password
    # FROM_EMAIL = "joshismit2812@outlook.com"
    # TO_EMAIL = "ursindhuk@gmail.com"
    # PASSWORD = "Smit@2812"

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = FROM_EMAIL
    message["To"] = TO_EMAIL
    message["Subject"] = "Subject: hello "+ name

    # Add the body of the email
    body = " hello sir ,\n\nThis email is sent from our application .\n\nThanks, sincerely"
    message.attach(MIMEText(body, "plain"))

    # Attach the PDF file
    pdf_file_path = output_pdf_path
    with open(pdf_file_path, "rb") as attachment:
        pdf_part = MIMEBase("application", "octet-stream")
        pdf_part.set_payload(attachment.read())
        encoders.encode_base64(pdf_part)
        pdf_part.add_header("Content-Disposition", f"attachment; filename=your_file.pdf")
        message.attach(pdf_part)

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
    smtp.quit()

def create_pdf(data, filename='output.pdf'):
    # Create a PDF document
    pdf_canvas = canvas.Canvas(filename, pagesize=letter)

    # Set up the font and size
    pdf_canvas.setFont("Helvetica", 12)

    # Set up table headers
    headers = ["Name","Email", "Contact"]  # Replace with your actual column names
    col_widths = [pdf_canvas.stringWidth(header, "Helvetica", 12) + 6 for header in headers]
    row_height = 20

    # Draw headers
    x = 100
    y = 750
    for i, header in enumerate(headers):
        pdf_canvas.drawString(x, y, header)
        x += col_widths[i] + 10

    # Draw data
    y -= row_height
    for row in data:
        x = 100
        for i, cell in enumerate(row):
            pdf_canvas.drawString(x, y, str(cell))
            x += col_widths[i] + 100
        y -= row_height

    # Save the PDF
    pdf_canvas.save()


def filter_data() :
    data = entry_1.get()
    # Output PDF filename
    output_filename = 'output.pdf'
    database = "./database/login.sqlite3"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    sql="select name, email, contact from user_data where type=?"

    cursor.execute(sql,(data,))
    result = cursor.fetchall()
    print(result)
    conn.commit()
    cursor.close()
    conn.close()
    create_pdf(result, output_filename)
    send_mail("joshismit2812@outlook.com","srp2092002@gmail.com","Smit@2812",name,output_filename)

def report_generation():
    global entry_1

    # Create PDF with the given data
    
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/report")
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(signup),
        relief="flat"
    )
    button_1.place(
        x=596.0,
        y=660.0,
        width=369.0,
        height=113.0
    )
    
    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=filter_data,
        relief="flat"
    )
    button_2.place(
        x=990.0,
        y=660.0,
        width=369.0,
        height=113.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(ASSETS_PATH,"button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=21.0,
        y=6.0,
        width=92.0,
        height=78.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_1.png"))
    entry_bg_1 = canvas.create_image(
        965.0,
        546.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#F8F8F8",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=729.0,
        y=508.0,
        width=472.0,
        height=74.0
    )

    window.resizable(False, False)
    window.mainloop()


def validate(email,password):
    database = "./login.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    sql="select password from student_data where email = ?"
    cursor.execute(sql, (email,))
    result = cursor.fetchone()
    print(result)
    if result:
        print(result)
    

def check_credentials(email, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Execute the SELECT query to check if email and password match
    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?", (email, password))

    # Fetch the result
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    # If result is not None, credentials match
    if result is not None and email!= "":
        print("Credentials match!")
        return True
    else:
        print("Credentials do not match.")
        return False


#redirects to student_type_selection 
def signin():
    global enter_name, enter_password
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/signin")
    for widget in window.winfo_children():
      widget.destroy()
    
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_1.png"))
    entry_bg_1 = canvas.create_image(
        456.0,
        449.0,
        image=entry_image_1
    )
    enter_name = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    enter_name.place(
        x=180.0,
        y=419.0,
        width=552.0,
        height=58.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_2.png"))
    entry_bg_2 = canvas.create_image(
        462.0,
        577.0,
        image=entry_image_2
    )
    enter_password = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    enter_password.place(
        x=186.0,
        y=547.0,
        width=552.0,
        height=58.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= partial(signup),
        relief="flat"
    )
    button_1.place(
        x=239.0,
        y=684.0,
        width=199.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= partial(main_module_selection,False),
        relief="flat"
    )
    button_2.place(
        x=480.0,
        y=689.0,
        width=190.0,
        height=71.0
    )
    window.resizable(False, False)
    window.mainloop()


def enter_data(name,contact, age, email, city, password):
    database = "./login.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    # data_to_insert = [i for i in global_list]
    sql = '''
        INSERT INTO student_data (name,contact, age, email, city, password) VALUES (?,?,?,?,?,?);
    '''
    cursor.execute(sql,[name,contact, age, email, city, password])
    conn.commit()

def signup():
    global entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8
    ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd()+"/assets/signup")

    #delete previous interface 
    for widget in window.winfo_children():
        widget.destroy()
    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"image_1.png"))
    image_1 = canvas.create_image(
        960.0,
        540.0,
        image=image_image_1
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_1.png"))
    entry_bg_1 = canvas.create_image(
        450.0,
        187.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_1.place(
        x=83.0,
        y=160.0,
        width=734.0,
        height=53.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_2.png"))
    entry_bg_2 = canvas.create_image(
        250.0,
        304.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_2.place(
        x=83.0,
        y=277.0,
        width=334.0,
        height=53.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_3.png"))
    entry_bg_3 = canvas.create_image(
        650.0,
        304.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_3.place(
        x=483.0,
        y=277.0,
        width=334.0,
        height=53.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_4.png"))
    entry_bg_4 = canvas.create_image(
        450.0,
        421.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_4.place(
        x=83.0,
        y=394.0,
        width=734.0,
        height=53.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_5.png"))
    entry_bg_5 = canvas.create_image(
        450.0,
        538.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_5.place(
        x=83.0,
        y=511.0,
        width=734.0,
        height=53.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_6.png"))
    entry_bg_6 = canvas.create_image(
        450.0,
        655.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_6.place(
        x=83.0,
        y=628.0,
        width=734.0,
        height=53.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_7.png"))
    entry_bg_7 = canvas.create_image(
        450.0,
        772.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_7.place(
        x=83.0,
        y=745.0,
        width=734.0,
        height=53.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"entry_8.png"))
    entry_bg_8 = canvas.create_image(
        450.0,
        892.5,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        font = ("Helvetica",20)
    )
    entry_8.place(
        x=83.0,
        y=865.0,
        width=734.0,
        height=53.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=partial(signin),
        relief="flat"
    )
    button_1.place(
        x=197.0,
        y=945.0,
        width=257.0,
        height=79.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets(ASSETS_PATH,"button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= partial(main_module_selection,True),
        relief="flat"
    )
    button_2.place(
        x=464.0,
        y=953.0,
        width=261.0,
        height=76.0
    )
    window.resizable(False, False)
    window.mainloop()



#starting point
signup()