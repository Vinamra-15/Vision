# WEBCAM REALTIME READ
import cv2
import numpy as np

cap = cv2.VideoCapture('human.mp4')

car_cascade = cv2.CascadeClassifier('cars.xml')
bus_cascade = cv2.CascadeClassifier('Bus_front.xml')
bike_cascade = cv2.CascadeClassifier('two_wheeler.xml')


# 0=webcam1
# 1=webcam2

while True:

    ret, frame = cap.read()

    if ret:
        dummy = 0
    else:
        break

    height = frame.shape[0]
    width = frame.shape[1]

    count = 0

    #frame = frame[50:height-50, (int(width/2))+50:width]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # creates a frame with gray layer)

    car = car_cascade.detectMultiScale(gray, 1.1, 2)
    bus = bus_cascade.detectMultiScale(gray, 1.16, 1)
    bike = bike_cascade.detectMultiScale(gray, 1.05, 3)

    #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)


    for (x, y, w, h) in car:
        if x>=(int(width/2))+250 & w<=width & y>=50 & h<=height-80 :
         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
         roi_gray = gray[y:y + h, x:x + w]
         roi_color = frame[y:y + h, x:x + w]
         count += 1

    for (x, y, w, h) in bus:
        if x >= (int(width / 2)) + 250 & w <= width & y >= 50 & h <= height - 80:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
         roi_gray = gray[y:y + h, x:x + w]
         roi_color = frame[y:y + h, x:x + w]
         count += 1

    for (x, y, w, h) in bike:
        if x >= (int(width / 2)) + 250 & w <= width & y >= 50 & h <= height - 80:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
         roi_grayb = gray[y:y + h, x:x + w]
         roi_colorb = frame[y:y + h, x:x + w]
         count += 1

    print(count)
    cv2.putText(frame, str(count), (10, 400), cv2.FONT_ITALIC, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if count <= 2:
        print('Maintain a speed between 50 kmph to 70 kmph')

    if count >= 3 and count < 5:
        print('Maintain a speed between 20 kmph to 40 kmph')

    if count >= 5:
        print('Maintain a speed under 20 kmph')

    if cv2.waitKey(2) & 0xFF == ord('q'):  # if wait key is not declared the frame is opened but not seen.
        break

cap.release()
cv2.destroyAllWindows()
print("no of hurdles")
print(count)
