from scipy.spatial import distance
from imutils import face_utils, resize
from dlib import get_frontal_face_detector, shape_predictor
import cv2
import numpy as np
import playsound
from threading import Thread
# alarm
def sound_alarm(soundfile):
    playsound.playsound(soundfile)
#detecing face
detect = get_frontal_face_detector()
predict = shape_predictor("shape_predictor_68_face_landmarks.dat")
#making facial landmarks(indexing)
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]


# calculating aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear
# setting limiting parameters
ear_limit=0.2
frame_limit=20
frame_counter=0
ALARM_ON=False

def drowsy(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    if (len(subjects) == 0):
        return 0
    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        lpts=np.array(leftEye)
        rpts=np.array(rightEye)
        cv2.polylines(img,[lpts],True,(255,255,0),2)
        cv2.polylines(img, [rpts], True, (255, 255, 0), 2)
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        return ear


#capturing video
print("Staring Video..")
vid= cv2.VideoCapture(0)

while (vid.isOpened()):
    # Read the frame
    _, img = vid.read()
    ear = drowsy(img)
    cv2.putText(img, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)


    if ear<ear_limit:
        frame_counter+=1
        if frame_counter>=frame_limit:
            cv2.putText(img, "WARNING!!!", (300, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if not ALARM_ON:
                ALARM_ON=True
                t=Thread(target=sound_alarm('alarm.mp3'))
                t.daemon=True
                t.start()
        cv2.putText(img,"BLINK:ARE YOU DROWSY?",(300,80),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    #print(ear)
    else:
        frame_counter=0
        ALARM_ON=False
    cv2.imshow('Detecting Drowsiness', img)
# Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
# Release the VideoCapture object
vid.release()
cv2.destroyAllWindows()