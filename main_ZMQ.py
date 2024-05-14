import cv2 
import socket
import zmq

import time 

  
vid = cv2.VideoCapture('rtsp://hoopad:admin123@192.168.10.56:554/cam/realmonitor?channel=1&subtype=0') 

context = zmq.Context()
socket = context.socket(zmq.PAIR)

socket.bind("tcp://*:5555")

c=0
while(True): 

    ret, frame = vid.read() 
    c+=1
    print('send frame: ',c)
    if ret:

        tim=time.time()
        socket.send_pyobj(frame)

        s=socket.recv_string()
        tim2=time.time()
        print((tim2-tim))
        # print(s)
        cv2.imshow('frame', frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
