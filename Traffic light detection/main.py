import cv2
import numpy as np

cap = cv2.VideoCapture('videoplayback.mp4')    # to read input
dummy = 0
while True:
    ret, frame1 = cap.read()    # to read the frames
    if ret:
        dummy += 1
    else:
        break

    height = frame1.shape[0]     # to get height of frame
    width = frame1.shape[1]      # to get width of frame

    frame = frame1[0:int(height / 2), int(width / 3):int(width) - 20]  # to limit the field of view

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         # converting frame in hsv format
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)     # only seeing red colours in the specified range
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)     # only seeing red colours in the specified range

    lower_green = np.array([40, 50, 50])
    upper_green = np.array([90, 255, 255])

    lower_yellow = np.array([15, 150, 150])
    upper_yellow = np.array([35, 255, 255])

    if(dummy == 50):
        dummy = 0
        here = 0
        #r_circles = None
        #g_circles = None
        #y_circles = None
        maskg = cv2.inRange(hsv, lower_green, upper_green)   # only detecting green colour in the specified range
        masky = cv2.inRange(hsv, lower_yellow, upper_yellow)   # only detecting yellow colour in the specified range
        maskr = cv2.add(mask1, mask2)                           # only detecting red colour in the specified range

        r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, 180,
                                 param1=50, param2=10, minRadius=0, maxRadius=30)     # detecting red signals
        y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 180,
                                     param1=50, param2=10, minRadius=0, maxRadius=30)   # detecting yellow signals
        g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 180,
                                     param1=50, param2=10, minRadius=0, maxRadius=30)    # detecting green signals

        #if r_circles is not None:
            #here = 1
        #if here != 1:

            #y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 180,
                                 #param1=50, param2=10, minRadius=0, maxRadius=30)     # detecting yellow signals
            #here = 1

        #if here != 1:
            #g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, 180,
                                 #param1=50, param2=10, minRadius=0, maxRadius=30)     # detecting green signals
            #here = 1

        #size = frame.shape
        #cimg = frame

        #r = 5
        #bound = 4.0 / 10


        if r_circles is not None:
            here = 1

            r_circles = np.uint16(np.around(r_circles))
            print('STOP')

            """for i in r_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0] or i[1] > size[0] * bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):
                        if (i[1] + m) >= size[0] or (i[0] + n) >= size[1]:
                            continue
                        h += maskr[i[1] + m, i[0] + n]
                        s += 1
                if h / s > 50:
                    cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                    cv2.circle(maskr, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                    cv2.putText(cimg, 'RED', (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA)"""
        if g_circles is not None:

            if here == 1:
                continue
            g_circles = np.uint16(np.around(g_circles))
            print('GO')
            here = 1

            """for i in g_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0] or i[1] > size[0] * bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):

                        if (i[1] + m) >= size[0] or (i[0] + n) >= size[1]:
                            continue
                        h += maskg[i[1] + m, i[0] + n]
                        s += 1
                if h / s >100:
                    cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                    cv2.circle(maskg, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                    cv2.putText(cimg, 'GREEN', (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA)"""

        if y_circles is not None:

            if here == 1:
                continue
            y_circles = np.uint16(np.around(y_circles))
            print('BE READY')
            here = 1

            """for i in y_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0] or i[1] > size[0] * bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):

                        if (i[1] + m) >= size[0] or (i[0] + n) >= size[1]:
                            continue
                        h += masky[i[1] + m, i[0] + n]
                        s += 1
                if h / s > 50:
                    cv2.circle(cimg, (i[0], i[1]), i[2] + 10, (0, 255, 0), 2)
                    cv2.circle(masky, (i[0], i[1]), i[2] + 30, (255, 255, 255), 2)
                    cv2.putText(cimg, 'YELLOW', (i[0], i[1]), font, 1, (255, 0, 0), 2, cv2.LINE_AA)"""

    cv2.imshow('frame',frame1)

    if cv2.waitKey(2) & 0xFF == ord('q'):   # if wait key is not declared the frame is opened but not seen.
        break

cv2.imshow('frame',frame1)
cv2.waitKey(0)