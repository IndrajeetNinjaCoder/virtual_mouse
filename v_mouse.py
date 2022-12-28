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



                # if id == 4:
                #     # make circle on Thumb
                #     cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                #     thumb_x = screen_width/frame_width*x
                #     thumb_y = screen_height/frame_height*y
                #     pyautogui.moveTo(thumb_x, thumb_x)
                #     # print(abs(index_y - thumb_y))


                # if id == 8:
                #     # make circle on index finger
                #     cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                #     index_x = screen_width/frame_width*x
                #     index_y = screen_height/frame_height*y
                #
                #     # moving mouse cursor on finger movement
                #     if abs(index_y - thumb_y) < 35:
                #         pyautogui.click()
                #         pyautogui.sleep(1)




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
                        pyautogui.click()
                        pyautogui.sleep(1)

                if id == 12:
                    # make circle on Middle Finger
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y

                    if abs(index_y - middle_y) < 50:
                        # print("Dragging...")
                        # pyautogui.click()
                        # pyautogui.sleep(2)
                        # pyautogui.mouseDown()
                        print(f"Scroll Down: {abs(index_y - middle_y)}")
                        pyautogui.vscroll(-600)

                    elif(index_y - middle_y) > 50:
                        print(f"Scroll UP: {abs(index_y - middle_y)}")
                        pyautogui.scroll(600)

                # if id == 16:
                #     # make circle on Ring Finger
                #     cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                #     ring_x = screen_width / frame_width * x
                #     ring_y = screen_height / frame_height * y
                #     # print(abs(index_y - middle_y))
                #     print(f"Scroll UP {((index_y + middle_y + ring_y)/3) - ring_y}")
                #     cordinate_y = abs(((index_y + middle_y + ring_y)/3)- ring_y)
                #     if (cordinate_y > 40) and (cordinate_y < 100):
                #         pyautogui.vscroll(600)






    # use Double click
 # pyautogui.click(x=87, y=227, clicks=2)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)