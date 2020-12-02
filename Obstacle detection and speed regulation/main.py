import cv2
import numpy as np

cap = cv2.VideoCapture('video.avi')  # to take input if want to take through webcam replace value with 0

car_cascade = cv2.CascadeClassifier('cars.xml')  # for car
bus_cascade = cv2.CascadeClassifier('Bus_front.xml')  # for bus
bike_cascade = cv2.CascadeClassifier('two_wheeler.xml')  # for two wheeler
human_cascade = cv2.CascadeClassifier('pedestrian.xml')  # for humans

delay = 0

while True:
    ret, frame = cap.read()  # to read frames

    if ret:
        delay += 1
    else:
        break  # to go out of loop when input gets over

    height = frame.shape[0]  # to get the height of frame
    width = frame.shape[1]  # to get the width of frame

    count = 0  # to get number of obstacles in a frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # to obtain gray layer frame from original frame

    car = car_cascade.detectMultiScale(gray, 1.1, 2)  # to detect cars in the frame
    bus = bus_cascade.detectMultiScale(gray, 1.16, 1)  # to detect bus in the frame
    bike = bike_cascade.detectMultiScale(gray, 1.05, 3)  # to detect two wheeler in the frame
    human = human_cascade.detectMultiScale(gray,1.1,5)  # to detect humans in the frame

    for (x, y, w, h) in car:
        if x >= (int(width / 2)) and w <= width and y >= 50 and h <= height - 80:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # making rectangle over cars in required lane
            #roi_gray = gray[y:y + h, x:x + w]
            #roi_color = frame[y:y + h, x:x + w]
            count += 1  # counting number of cars

    for (x, y, w, h) in bus:
        if x >= (int(width / 2)) and w <= width and y >= 50 and h <= height - 80:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # making rectangle over bus in required lane
            #roi_grayb = gray[y:y + h, x:x + w]
            #roi_colorb = frame[y:y + h, x:x + w]
            count += 1  # counting number of bus

    for (x, y, w, h) in bike:
        if x >= (int(width / 2)) and w <= width and y >= 50 and h <= height - 80:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # making reactangle over two wheeler in required lane
            #roi_graytw = gray[y:y + h, x:x + w]
            #roi_colortw = frame[y:y + h, x:x + w]
            count += 1  # counting number of two wheelers

    for (x, y, w, h) in human:
        if x >= (int(width / 2)) and w <= width and y >= 50 and h <= height - 80:
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # making reactangle over humans in required lane
            #roi_grayh = gray[y:y + h, x:x + w]
            #roi_colorh = frame[y:y + h, x:x + w]
            count += 1  # counting number of humans

    cv2.putText(frame, str(count), (10, 400), cv2.FONT_ITALIC, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if(delay==5):
        delay = 0
        print('Number of obstacles : ', count)

        if count >= 0 and count <= 1:
            print('Maintain a speed between 70 kmph to 80 kmph')

        if count >= 2 and count < 4:
            print('Maintain a speed between 50 kmph to 60 kmph')

        if count >= 4 and count < 7:
            print('Maintain a speed between 40 kmph to 50 kmph')

        if count >= 7 and count < 9:
            print('Maintain a speed between 30 kmph to 40 kmph')

        if count >=9 and count < 11:
            print('Maintain a speed between 20 kmph to 30 kmph')

        if count >= 11:
            print('Maintain a speed under 20 kmph')

    if cv2.waitKey(2) & 0xFF == ord('q'):  # if wait key is not declared the frame is opened but not seen.
        break

cap.release()
cv2.destroyAllWindows()
print('Number of obstacles : ', count)


