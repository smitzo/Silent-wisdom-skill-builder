from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading
from faker import Faker
import os
import sys
from functools import partial
current_directory = os.getcwd()
current_path = os.path.abspath(os.path.join(current_directory))
sys.path.append(current_path)
from insert_into_database import insert_gameplay_data
from dashboard_analytics import user_dashboard
# Functionality Part
totaltime = 60
time = 0
wrongwords = 0
elapsedtimeinminutes = 0


def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        elapsed_timer_label.config(text=time)
        remainingtime = totaltime-time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)


def count():
    global wrongwords, accuracy
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

    totalwords_count_label.config(text=totalwords)

    para_word_list = label_paragraph['text'].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
            wrongwords += 1

    wrongwords_count_label.config(text=wrongwords)

    elapsedtimeinminutes = time/60
    wpm = (totalwords-wrongwords)/elapsedtimeinminutes
    wpm_count_label.config(text=wpm)
    gross_wpm = totalwords/elapsedtimeinminutes
    accuracy = wpm/gross_wpm*100
    accuracy = round(accuracy)
    accuracy_percent_label.config(text=str(accuracy)+'%')


def generate_random_paragraph(num_sentences):
    fake = Faker()
    sentences = [fake.sentence() for _ in range(num_sentences)]
    paragraph = " ".join(sentences)
    # paragraph = fake.paragraph(nb_sentences=min_sentences)
    return paragraph


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time, elapsedtimeinminutes
    time = 0
    elapsedtimeinminutes = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')


# GUI Part

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# root.geometry(f'{screen_width}x{screen_height}+0+0')
root.geometry('1920x1080+0+0')
root.resizable(0, 0)
root.overrideredirect(True)

mainframe = Frame(root, bd=4)
mainframe.grid()

titleframe = Frame(mainframe, bg='orange')
titleframe.grid()

titleLabel = Label(titleframe, text='Keyboard Typing', font=(
    'algerian', 30, 'bold'), bg='goldenrod3', fg='white', width=int(screen_width/24), bd=10)
titleLabel.grid(pady=10)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)

# Initialize the initial paragraph
initial_paragraph = generate_random_paragraph(7)

def terminating():
    insert_gameplay_data(int(accuracy),"keyboard typing speed")
    user_dashboard("keyboard typing speed")
    root.destroy()
    sys.exit()


label_paragraph = Label(
    paragraph_frame, text=initial_paragraph, wraplength=1400, justify=LEFT, font=('arial', 18, 'bold'),pady=30)
label_paragraph.grid(row=0, column=0)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2, column=0)

textarea = Text(textarea_frame, font=('arial', 18, 'bold'), width=120,
                height=8, bd=4, relief=GROOVE, wrap='word', state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

elapsed_time_label = Label(
    frame_output, text='Elapsed Time', font=('Tahoma', 14, 'bold'), fg='red')
elapsed_time_label.grid(row=0, column=0, padx=8, pady=11)

elapsed_timer_label = Label(frame_output, text='0',
                            font=('Tahoma', 14, 'bold'))
elapsed_timer_label.grid(row=0, column=1, padx=8, pady=11)

remaining_time_label = Label(
    frame_output, text='Remaining Time', font=('Tahoma', 14, 'bold'), fg='red')
remaining_time_label.grid(row=0, column=2, padx=8, pady=11)

remaining_timer_label = Label(
    frame_output, text='60', font=('Tahoma', 14, 'bold'))
remaining_timer_label.grid(row=0, column=3, padx=8, pady=11)

wpm_label = Label(frame_output, text='WPM',
                  font=('Tahoma', 14, 'bold'), fg='red')
wpm_label.grid(row=0, column=4, padx=8, pady=11)

wpm_count_label = Label(frame_output, text='0', font=('Tahoma', 14, 'bold'))
wpm_count_label.grid(row=0, column=5, padx=8, pady=11)

totalwords_label = Label(frame_output, text='Total Words',
                         font=('Tahoma', 14, 'bold'), fg='red')
totalwords_label.grid(row=0, column=6, padx=8, pady=11)

totalwords_count_label = Label(
    frame_output, text='0', font=('Tahoma', 14, 'bold'))
totalwords_count_label.grid(row=0, column=7, padx=8, pady=11)

wrongwords_label = Label(frame_output, text='Wrong Words',
                         font=('Tahoma', 14, 'bold'), fg='red')
wrongwords_label.grid(row=0, column=8, padx=8, pady=11)

wrongwords_count_label = Label(
    frame_output, text='0', font=('Tahoma', 14, 'bold'))
wrongwords_count_label.grid(row=0, column=9, padx=8, pady=11)

accuracy_label = Label(frame_output, text='Accuracy',
                       font=('Tahoma', 14, 'bold'), fg='red')
accuracy_label.grid(row=0, column=10, padx=8, pady=11)

accuracy_percent_label = Label(
    frame_output, text='0', font=('Tahoma', 14, 'bold'))
accuracy_percent_label.grid(row=0, column=11, padx=8, pady=11)

buttons_Frame = Frame(mainframe)
buttons_Frame.grid(row=4, column=0)

startButton = ttk.Button(buttons_Frame, text='Start', command=start)
startButton.grid(row=0, column=0, padx=10, pady=14)

resetButton = ttk.Button(buttons_Frame, text='Reset',
                         state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=10, pady=14)

exitButton = ttk.Button(buttons_Frame, text='Exit', command=partial(terminating))
exitButton.grid(row=0, column=2, padx=10, pady=14)

keyboard_frame = Frame(mainframe)
keyboard_frame.grid(row=5, column=0)

frame1to0 = Frame(keyboard_frame)
frame1to0.grid(row=0, column=0, pady=12)

label1 = Label(frame1to0, text='1', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label2 = Label(frame1to0, text='2', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label3 = Label(frame1to0, text='3', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label4 = Label(frame1to0, text='4', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label5 = Label(frame1to0, text='5', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label6 = Label(frame1to0, text='6', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label7 = Label(frame1to0, text='7', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label8 = Label(frame1to0, text='8', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label9 = Label(frame1to0, text='9', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
label0 = Label(frame1to0, text='0', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)

label1.grid(row=0, column=0, padx=7)
label2.grid(row=0, column=1, padx=7)
label3.grid(row=0, column=2, padx=7)
label4.grid(row=0, column=3, padx=7)
label5.grid(row=0, column=4, padx=7)
label6.grid(row=0, column=5, padx=7)
label7.grid(row=0, column=6, padx=7)
label8.grid(row=0, column=7, padx=7)
label9.grid(row=0, column=8, padx=7)
label0.grid(row=0, column=9, padx=7)

frameqtop = Frame(keyboard_frame)
frameqtop.grid(row=1, column=0, pady=7)
labelQ = Label(frameqtop, text='Q', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelW = Label(frameqtop, text='W', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelE = Label(frameqtop, text='E', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelR = Label(frameqtop, text='R', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelT = Label(frameqtop, text='T', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelY = Label(frameqtop, text='Y', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelU = Label(frameqtop, text='U', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelI = Label(frameqtop, text='I', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelO = Label(frameqtop, text='O', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelP = Label(frameqtop, text='P', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)

labelQ.grid(row=0, column=0, padx=7)
labelW.grid(row=0, column=1, padx=7)
labelE.grid(row=0, column=2, padx=7)
labelR.grid(row=0, column=3, padx=7)
labelT.grid(row=0, column=4, padx=7)
labelY.grid(row=0, column=5, padx=7)
labelU.grid(row=0, column=6, padx=7)
labelI.grid(row=0, column=7, padx=7)
labelO.grid(row=0, column=8, padx=7)
labelP.grid(row=0, column=9, padx=7)

frameatol = Frame(keyboard_frame)
frameatol.grid(row=2, column=0, pady=7)
labelA = Label(frameatol, text='A', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelS = Label(frameatol, text='S', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelD = Label(frameatol, text='D', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelF = Label(frameatol, text='F', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelG = Label(frameatol, text='G', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelH = Label(frameatol, text='H', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelJ = Label(frameatol, text='J', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelK = Label(frameatol, text='K', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelL = Label(frameatol, text='L', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)

labelA.grid(row=0, column=0, padx=7)
labelS.grid(row=0, column=1, padx=7)
labelD.grid(row=0, column=2, padx=7)
labelF.grid(row=0, column=3, padx=7)
labelG.grid(row=0, column=4, padx=7)
labelH.grid(row=0, column=5, padx=7)
labelJ.grid(row=0, column=6, padx=7)
labelK.grid(row=0, column=7, padx=7)
labelL.grid(row=0, column=8, padx=7)

frameztom = Frame(keyboard_frame)
frameztom.grid(row=3, column=0, pady=7)
labelZ = Label(frameztom, text='Z', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelX = Label(frameztom, text='X', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelC = Label(frameztom, text='C', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelV = Label(frameztom, text='V', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelB = Label(frameztom, text='B', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelN = Label(frameztom, text='N', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)
labelM = Label(frameztom, text='M', bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=5, height=3, bd=10, relief=GROOVE)

labelZ.grid(row=0, column=0, padx=7)
labelX.grid(row=0, column=1, padx=7)
labelC.grid(row=0, column=2, padx=7)
labelV.grid(row=0, column=3, padx=7)
labelB.grid(row=0, column=4, padx=7)
labelN.grid(row=0, column=5, padx=7)
labelM.grid(row=0, column=6, padx=7)

spaceFrame = Frame(keyboard_frame)
spaceFrame.grid(row=4, column=0, pady=7)

labelSpace = Label(spaceFrame, bg='black', fg='white', font=(
    'arial', 12, 'bold'), width=40, height=3, bd=10, relief=GROOVE)
labelSpace.grid(row=0, column=0)


def changeBG(widget):
    widget.config(bg='grey')
    widget.after(100, lambda: widget.config(bg='black'))


label_numbers = [label1, label2, label3, label4,
                 label5, label6, label7, label8, label9, label0]

label_alphabets = [labelA, labelB, labelC, labelD, labelE, labelF, labelG, labelH, labelI, labelJ, labelK, labelL, labelM, labelN,
                   labelO, labelP, labelQ, labelR, labelS, labelT, labelU, labelV, labelW, labelX, labelY, labelZ]

space_label = [labelSpace]

binding_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z']

binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x', 'y', 'z']

for numbers in range(len(binding_numbers)):
    root.bind(binding_numbers[numbers], lambda event,
              label=label_numbers[numbers]: changeBG(label))


for capital_alphabets in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[capital_alphabets], lambda event,
              label=label_alphabets[capital_alphabets]: changeBG(label))

for small_alphabets in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[small_alphabets], lambda event,
              label=label_alphabets[small_alphabets]: changeBG(label))

root.bind('<space>', lambda event: changeBG(space_label[0]))

root.mainloop()
