import math

import cv2
import mediapipe as mp
import pyautogui

# making failSafe False
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils
hand_detector = mp.solutions.hands.Hands()

screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    _, frame = cap.read()
    # flipping video to get accurate results
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # to Detect Hand
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)



                if id == 8:
                    # make circle on index finger
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                    # moving mouse cursor on finger movement
                    pyautogui.moveTo(index_x, index_y  )

                if id == 4:
                    # make circle on Thumb
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    # print(abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 35:
                        # pyautogui.click(clicks=2)
                        pyautogui.click()
                        pyautogui.sleep(1)

                if id == 12:
                    # make circle on Middle Finger
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y

                    diff_x = math.floor(index_x - middle_x)
                    diff_y = math.floor(index_y - middle_y)

                    # print(f"({index_x}, {index_y}),  ({middle_x}, {middle_y}), ({diff_x}, {diff_y})")

                    # Working properly
                    if (index_x < middle_x) and (index_y > middle_y) and ((diff_x <= -40) and (diff_x >= -90.00)) and ((diff_y >= 25) and (diff_y <= 45)):
                        pyautogui.scroll(-600)

                    elif (index_x > middle_x) and (index_y > middle_y) and ((diff_x >= 6) and (diff_x <= 60)) and ((diff_y >= 25) and (diff_y <= 70)):
                        pyautogui.scroll(600)



                    # if abs(index_y - middle_y) < 30:
                    #     # print("Dragging...")
                    #     # pyautogui.click()
                    #     # pyautogui.sleep(2)
                    #     # pyautogui.mouseDown()
                    #     print(f"Scroll Down: {abs(index_y - middle_y)}")
                    #     pyautogui.vscroll(-600)

                    # elif(index_y - middle_y) > 50:
                    #     print(f"Scroll UP: {abs(index_y - middle_y)}")
                    #     pyautogui.scroll(600)

                # if id == 16:
                #     # make circle on Ring Finger
                #     cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                #     ring_x = screen_width / frame_width * x
                #     ring_y = screen_height / frame_height * y
                #
                #     dif_x1 = math.floor(thumb_x - index_x)
                #     dif_x2 = math.floor(thumb_x - ring_x)
                #
                #     dif_y1 = math.floor(thumb_y - ring_y)
                #     dif_y2 = math.floor(thumb_y - ring_y)
                #
                #
                #
                #     print(f"({thumb_x}, {thumb_y}), ({index_x}, {index_y}),  ({ring_x}, {ring_y}), ({dif_x1}, {dif_x2}), ({dif_y1}, {dif_y2})")

                    # if (thumb_x > index_x) and (index_x > ring_x) and (thumb_y > ring_y) and (ring_y > index_y) and (dif_x1 <= -10) and (dif_x1 >= -60) and (dif_x2 <= -15) and (dif_x2 >= -60) and (dif_y1 >= 45) and (dif_y1 <= 150) and (dif_y2 >= 20) and (dif_y2 <= 100):
                    #     pyautogui.click()
                    #     pyautogui.click()
                    #     pyautogui.sleep(1)







    # use Double click
 # pyautogui.click(x=87, y=227, clicks=2)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)