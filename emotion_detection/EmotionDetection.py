from keras.models import load_model
import time
from keras.preprocessing.image import img_to_array
# from tensorflow.keras.utils import img_to_array
import cv2
import numpy as np
import os
import random
def main():
    working_dir = os.getcwd() + "/emotion_detection"
    # Load the face detection model and emotion classifier model
    face_classifier = cv2.CascadeClassifier(working_dir +'/haarcascade_frontalface_default.xml')
    classifier = load_model(working_dir + '/model.h5')

    emotion_labels = ['Angry', 'Fear', 'Disgust', 'Happy', 'Neutral', 'Sad', 'Surprise']
    # emotion_labels = [ 'Happy', 'Neutral', 'Surprise']

    cap = cv2.VideoCapture(0)

    cv2.namedWindow("BG", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("BG", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    task_img_start_time = time.time()
    start_time = time.time()
    time_duration = 30
    task_img_duration = 5

    # Initialize task_img outside the loop
    task_img = random.choice(emotion_labels)


    while time.time() - start_time < time_duration:
        label = ""
        if time.time() - task_img_start_time >= task_img_duration:
            task_img = random.choice(emotion_labels)
            task_img_start_time = time.time()

        imgBG = cv2.imread(working_dir + "/Assets/Bg.png")

        success, frame = cap.read()

        if not success:
            print("Frame isn't properly detected")
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        live_img_width = 740
        live_img_height = 710

        count_img_width = 740
        count_img_height = 680

        img_i = cv2.imread(working_dir + f"/assets/{task_img}.png")

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()-2]
                label_position = (x, y)
                cv2.putText(frame, label, label_position,
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'No Faces', (30, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if live_img_height is not None and live_img_width is not None:
            imgScaled = cv2.resize(frame, (live_img_width, live_img_height))
            print (imgScaled.shape)
        else:
            print("Live image error")

        if img_i is not None:
            print(img_i.shape)
            img_i = cv2.resize(img_i, (count_img_width, count_img_height))

        imgBG[290:290 + live_img_height, 80:80 + live_img_width] = imgScaled

        if count_img_height is not None and count_img_width is not None:
            imgBG[290:290 + count_img_height, 1103:1103 + count_img_width] = img_i
        else:
            print("Count image error")

        if task_img == label:
            cv2.putText(frame, 'you are correct', (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            task_img = random.choice(emotion_labels)

        cv2.imshow('BG', imgBG)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()