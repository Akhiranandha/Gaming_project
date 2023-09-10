import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key , Controller

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
detector = HandDetector(detectionCon = 0.7 , maxHands = 1)

keyboard = Controller()
while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    hands , img = detector.findHands(img)

    if hands:
        fingers = detector.fingersUp(hands[0])
        if fingers == [0,0,0,0,0] :
            keyboard.press(Key.left)
            keyboard.release(Key.right)
        elif fingers == [1,1,1,1,1] :
            keyboard.press(Key.right)
            keyboard.release(Key.left)
    else :
        keyboard.release(Key.left)
        keyboard.release(Key.right)
    cv2.imshow("game", img)
    if cv2.waitKey(1) == ord("q"):
        cap.release()
        break