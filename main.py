import cv2
import os
import math
import numpy as np
import mediapipe as mp
import time
import random
import pygame

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

currentPath=os.path.dirname(__file__)
soundPath=os.path.join(currentPath,"sound")
imgPath=os.path.join(currentPath,"img")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

timer=0
stateResult=False
startGame=False
score=0

#-------------- 배경음악. 효과음 설정 --------------#
pygame.mixer.init()
bgmSound=pygame.mixer.Sound(os.path.join(soundPath,'bgm.wav'))
bgmSound.play(-1)
bgmSound.set_volume(0.5)
steteBgmSound=True
winSound=pygame.mixer.Sound(os.path.join(soundPath,'win.wav'))
loseSound=pygame.mixer.Sound(os.path.join(soundPath,'lose.wav'))
startSound=pygame.mixer.Sound(os.path.join(soundPath,'start.wav'))
gameSound=pygame.mixer.Sound(os.path.join(soundPath,'game.wav'))
#-------------------------------------------------#

while True:
    imgBG=cv2.imread(os.path.join(imgPath,"img.png"))
    ret, img = cap.read()
    imgFlipped=cv2.flip(img, 1)
    imgScaled=cv2.resize(imgFlipped,(0,0),None,1,1)

    start = time.time()
    img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
    img.flags.writeable = False
    results = face_mesh.process(img)
    img.flags.writeable = True
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_h, img_w, img_c = img.shape
    face_3d = []
    face_2d = []

    if startGame:
        if stateResult is False:         
            timer = 2-(time.time()-initialTime)    
            if timer<0:
                stateResult=True
                timer=2
                print(str(text))
                randomNumber=random.randrange(1,4) # 1:left / 2:right / 3:center
                print(int(randomNumber))

                if(randomNumber!=player):
                    winSound.play()
                    print('Player Win!')
                    score+=1
                elif(randomNumber==player):
                    loseSound.play()
                    print('Computer Win!')
                    score=0

    cv2.putText(imgBG,str(int(score)),(1070,640),cv2.FONT_HERSHEY_PLAIN,6,(255,255,255),5)          

#------------- 얼굴 좌우 확인 알고리즘 -------------#
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                    if idx == 1:
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                    
                    face_2d.append([x, y]) #2D좌표
                    face_3d.append([x, y, lm.z]) #3D좌표
            face_2d = np.array(face_2d, dtype=np.float64)
            face_3d = np.array(face_3d, dtype=np.float64)

            # The camera matrix
            focal_length = 1 * img_w

            cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                   [0, focal_length, img_w / 2],
                                   [0, 0, 1]])

            # The distortion parameters
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Solve PnP
            success, rot_vec, trans_vec = cv2.solvePnP(
                face_3d, face_2d, cam_matrix, dist_matrix)

            # Get rotational matrix
            rmat, jac = cv2.Rodrigues(rot_vec)

            # Get angles
            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            # Get the y rotation degree
            x = angles[0] * 360
            y = angles[1] * 360
            z = angles[2] * 360

            # See where the user's head tilting
            if y < -10:
                text = "Left"
                player=1
            elif y > 10:
                text = "Right"
                player=2
            else:
                text = "Center"
                player=3

            # Display the nose direction
            nose_3d_projection, jacobian = cv2.projectPoints(
                nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)

            p1 = (int(nose_2d[0]), int(nose_2d[1]))
            p2 = (int(nose_2d[0] + y * 10), int(nose_2d[1] - x * 10))

            cv2.line(img, p1, p2, (255, 0, 0), 3)

            # Add the text on the img
            cv2.putText(img, text, (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv2.putText(img, "x: " + str(np.round(x, 2)), (500, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, "y: " + str(np.round(y, 2)), (500, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, "z: " + str(np.round(z, 2)), (500, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        end = time.time()
        totalTime = end - start

        fps = 1 / totalTime
        #print("FPS: ", fps)

        cv2.putText(img, f'FPS: {int(fps)}', (20, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

        mp_drawing.draw_landmarks(image=img,
                                  landmark_list=face_landmarks,
                                  connections=mp_face_mesh.FACEMESH_CONTOURS,
                                  landmark_drawing_spec=drawing_spec,
                                  connection_drawing_spec=drawing_spec)                        
#------------- 얼굴 좌우 확인 알고리즘 -------------#
    cv2.imshow('Head Pose Estimation', img)
    imgBG[220:700,320:960]=imgScaled
    cv2.imshow('gameScreen', imgBG)

    key = cv2.waitKey(1)
    if key == ord('s'): #게임 시작
        startGame=True
        stateResult=False
        initialTime=time.time()
        if score==0:
            startSound.play()
            initialTime+=2
        else:
            gameSound.play()
    elif key == ord('m'): #Bgm 음소거 유무
        if steteBgmSound==True:
            bgmSound.stop()
            steteBgmSound=False
        else:
            bgmSound.play()
            steteBgmSound=True
    elif key == 27: #게임 종료
        break

cap.release()