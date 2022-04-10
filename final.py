import cv2
import array as ars
import numpy as np

from simple_facerec import SimpleFacerec

stf=SimpleFacerec()
stf.load_encoding_images("images")

array=[]

def search(list,n):
  
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False
  

#load camera 

cap = cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()


    face_locations, face_names=stf.detect_known_faces(frame)

    for face_loc, name in zip(face_locations,face_names):
        y1,x1,y2,x2= face_loc[0],face_loc[1],face_loc[2],face_loc[3]

        cv2.putText(frame,name,(x1,y1 -10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),4)
        x=search(array,face_names)
        if  not x: 
            array.append(face_names)



    cv2.imshow("Frame", frame)
    
    key=cv2.waitKey(30) & 0xff
    if key==27:
        break


print(array)

with open("attendance.txt","w") as filehandle:
    for listitem in array:
        filehandle.write('%s\n' % listitem)


cap.release()
cv2.destroyAllWindows()