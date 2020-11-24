import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands



### Functions
def recognizeHandGesture(landmarks):
  thumbState = 'UNKNOWN'
  indexFingerState = 'UNKNOWN'
  middleFingerState = 'UNKNOWN'
  ringFingerState = 'UNKNOWN'
  littleFingerState = 'UNKNOWN'
  recognizedHandGesture = None
  pseudoFixKeyPoint = landmarks.landmark[2].x
  if (landmarks.landmark[3].x < pseudoFixKeyPoint and landmarks.landmark[4].x  < landmarks.landmark[3].x ):
    thumbState = 'OPEN'    
  elif (pseudoFixKeyPoint < landmarks.landmark[3].x  and landmarks.landmark[3].x  < landmarks.landmark[4].x ):
    thumbState = 'CLOSE'    

  pseudoFixKeyPoint = landmarks.landmark[6].y
  if (landmarks.landmark[7].y < pseudoFixKeyPoint and landmarks.landmark[8].y < landmarks.landmark[7].y):
    indexFingerState = 'OPEN'    
  elif (pseudoFixKeyPoint < landmarks.landmark[7].y and landmarks.landmark[7].y < landmarks.landmark[8].y):
    indexFingerState = 'CLOSE'    

  pseudoFixKeyPoint = landmarks.landmark[10].y
  if (landmarks.landmark[11].y < pseudoFixKeyPoint and landmarks.landmark[12].y < landmarks.landmark[11].y):
    middleFingerState = 'OPEN'    
  elif (pseudoFixKeyPoint < landmarks.landmark[11].y and landmarks.landmark[11].y < landmarks.landmark[12].y):
    middleFingerState = 'CLOSE'

  pseudoFixKeyPoint = landmarks.landmark[14].y
  if (landmarks.landmark[15].y < pseudoFixKeyPoint and landmarks.landmark[16].y < landmarks.landmark[15].y):
    ringFingerState = 'OPEN'    
  elif (pseudoFixKeyPoint < landmarks.landmark[15].y and landmarks.landmark[15].y < landmarks.landmark[16].y):
    ringFingerState = 'CLOSE'
  
  pseudoFixKeyPoint = landmarks.landmark[18].y
  if (landmarks.landmark[19].y < pseudoFixKeyPoint and landmarks.landmark[20].y < landmarks.landmark[19].y):
    littleFingerState = 'OPEN'    
  elif (pseudoFixKeyPoint < landmarks.landmark[19].y and landmarks.landmark[19].y < landmarks.landmark[20].y):
    littleFingerState = 'CLOSE'
    
  if (thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN'):
    recognizedHandGesture = "FIVE"   
  elif (thumbState == 'CLOSE' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN'):
    recognizedHandGesture = "FOUR"  
  elif (thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
    recognizedHandGesture = "TREE"   
  elif (thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
    recognizedHandGesture = "TWO"   
  elif (thumbState == 'CLOSE' and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
    recognizedHandGesture = "FIST"
  elif (thumbState == 'CLOSE' and indexFingerState == 'CLOSE' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
    recognizedHandGesture = "FUCK DEVO"
  else:
    recognizedHandGesture = "UNKNOWN"

  print(recognizedHandGesture)  
  return recognizedHandGesture



def isSliding(landmarks,memo):

    actualPosition_x = landmarks.landmark[0].x
    actualPosition_y = landmarks.landmark[0].y

    if memo == None:
        memo=[landmarks.landmark[0].x,landmarks.landmark[0].y]

    lastPosition_x,lastPosition_y = memo[0],memo[1]

    slide = ""

    print(actualPosition_x - lastPosition_x )
    if actualPosition_x - lastPosition_x > 0.02:
        slide = "RIGHT SLIDE"
    elif actualPosition_x - lastPosition_x < -0.02:
        slide = "LEFT SLIDE"
    elif actualPosition_y - lastPosition_y > 0.02:
        slide = "DOWN SLIDE"
    elif actualPosition_y - lastPosition_y < -0.02:
        slide = "UP SLIDE"
    if slide == "":
        memory=[lastPosition_x,lastPosition_y]

    else :
        memory= [actualPosition_x, actualPosition_y]

    return [slide,memory] 

def getStructuredLandmarks(landmarks):
  structuredLandmarks = []
  for j in range(42):
    if( j %2 == 1):
      structuredLandmarks.append({ 'x': landmarks[j - 1], 'y': landmarks[j] })
  return structuredLandmarks

#recognizedHandGesture = recognizeHandGesture(getStructuredLandmarks(test_landmarks_data))
#print("recognized hand gesture: ", recognizedHandGesture) # print: "recognized hand gesture: 5"



hands = mp_hands.Hands(
    min_detection_confidence=0.7, min_tracking_confidence=0.5,max_num_hands=1)

cap = cv2.VideoCapture(0)

memo = None

while cap.isOpened():
  success, image = cap.read()
  if not success:
    break

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = False
  results = hands.process(image)


  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  font = cv2.FONT_HERSHEY_COMPLEX
  

  if results.multi_hand_landmarks:
    
    for hand_landmarks in results.multi_hand_landmarks: 
       
      mp_drawing.draw_landmarks(
          image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    text = recognizeHandGesture(results.multi_hand_landmarks[0])
    text2,memo = isSliding(results.multi_hand_landmarks[0],memo)[0],isSliding(results.multi_hand_landmarks[0],memo)[1]
    print("memo : "+str(memo[0])+" ,"+str(memo[1]))
    
    cv2.putText(image, text, (360,360), font, 1, (0, 0, 255), 2, cv2.LINE_4)

    cv2.putText(image, text2, (360,460), font, 1, (0, 0, 255), 2, cv2.LINE_4)    

  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break

hands.close()
cap.release()