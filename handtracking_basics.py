import cv2 
import mediapipe as mp
import time
# imported the libaraires
cap = cv2.VideoCapture(0)
# access the webcam
mpimport = mp.solutions.mediapipe.python.solutions
# imported main files link hand, drawingutil, etc
mp_drawing_style = mpimport.drawing_styles
mp_hands = mpimport.hands.Hands()
# imported hand class in hand module
cTime = 0
pTime = 0
while True:
    frame, img = cap.read()
    # read the webcam data
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # covert BGR to RGB
    results = mp_hands.process(imgRGB)
    # process the results
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            # Drawing the landmark
            for id, lms in enumerate(handlms.landmark):
                # giving accurate x and y coordinates for detection
                H, W, C = img.shape
                Cx, Cy = int(lms.x*H), int(lms.y*W)
                print(id, Cx, Cy)
            mpimport.drawing_utils.draw_landmarks(img, handlms, mpimport.hands.HAND_CONNECTIONS,mp_drawing_style.get_default_hand_landmarks_style(),
            mp_drawing_style.get_default_hand_connections_style())
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # Geting fps
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)
    # priting fps on the webcam
    cv2.imshow("camera",img)
    # shown the webcam data
    if cv2.waitKey(1) == ord('q'):
        break
    # update the camera data every 1 milisecond