import cv2
import pickle


cap=cv2.VideoCapture(0)
try:
    with open("parklots",'rb')as f:
            points=pickle.load(f)
except:
    points=[]
def drawing(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        with open("parklots",'wb')as f:
            pickle.dump(points,f)
    if event==cv2.EVENT_RBUTTONDOWN:
       for i,pts in enumerate(points):
           x1,y1=pts
           if x1<x+w and y1<y+h:
               points.pop(i)
            
        

w,h=29,27
while True:
    success,frame=cap.read()
    if success==False:
        break

    frame=cv2.resize(frame,(640,480))
    for pts in points:
        cv2.rectangle(frame,pts,(pts[0]+w,pts[1]+h),(0,0,255),2)
    
    
  
    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame",drawing)
    if cv2.waitKey(32) & 0xFF == 27:
        break
cap.release()    
cv2.destroyAllWindows()
