import cv2 
import socket
import zmq

import time 
from client import Client
  
vid = cv2.VideoCapture('rtsp://hoopad:admin123@192.168.10.56:554/cam/realmonitor?channel=1&subtype=0') 

# context = zmq.Context()
# socket = context.socket(zmq.PAIR)
# socket.bind("tcp://*:5555")


client = Client("localhost:50051")
c=0
while(True): 

    ret, frame = vid.read() 
    c+=1
    print('send frame: ',c)
    if ret:

        tim=time.time()
        # socket.send_pyobj(frame)
        # frame=cv2.resize(frame,(800,600))
        response = client.request_start(frame.tobytes())

        # s=socket.recv_string()
        s=response
        # print(s)
        tim2=time.time()
        print((tim2-tim))
        # print(s)
        # cv2.imshow('frame', frame) 

        # if cv2.waitKey(1) & 0xFF == ord('q'): 
        #     break
