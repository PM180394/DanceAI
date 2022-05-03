import cv2
import numpy as np
import mediapipe as mp
import math


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
landmarks= mp.solutions.pose.PoseLandmark


cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8, enable_segmentation=False) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("If reading input stream is unsucessful!!!")
      continue
      

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    nose= results.pose_landmarks.landmark[0]
    wrist= results.pose_landmarks.landmark[19]
    distance=math.dist([nose.x, nose.y],[wrist.x, wrist.y])
    print(distance)
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    if distance <0.44:
    	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    else:
    	image= cv2.cvtColor(image, cv2.COLOR_RGB2HSV)	
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),thickness=3, circle_radius=3),
        connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),thickness=3, circle_radius=3))
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
