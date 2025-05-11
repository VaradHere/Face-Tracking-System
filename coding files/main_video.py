import cv2
from simple_facerec import SimpleFacerec
#import pyttsx3//
#import controller as cnt//

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
#t_s = pyttsx3.init()//

# Load Camera
cap = cv2.VideoCapture(0)

#boundry
left=50          # + to reduce
top=50           # + to reduce
right=600        # - to reduce
bottom=450       # - to reduce


while True:
    ret, frame = cap.read()


    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        print(face_loc)
        #    cv2.rectangle(frame, (600,50 ), (50, 450), (0, 0, 200), 4)
#        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        """face_loc[1]=right
           face_loc[2]=down
           face_loc[3]=top
           face_loc[0]=left
        """
#
        if (face_loc[0] < left) | (face_loc[3] < top)|(face_loc[1] > right) | (face_loc[2] > bottom):
            total = 1
            print("led 1 on\n other off")


        else:
            total = 0

        #cnt.abc(total)//
        cv2.putText(frame, name, (x1 - 50, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        #ans = "welcome",face_names//
        #t_s.say(ans)//
        #t_s.runAndWait()//
    cv2.rectangle(frame, (right,top), (left, bottom), (0, 0, 200), 4)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()