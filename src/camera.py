'''
1. Provide a simple system for Web Based Video Live Streaming with AI Object Detection Function
2. Client will be any modern web browser like Chrome
3. Server connects to IP Cam or Web Cam, serve a simple webpage through HTTP to display the video frames on Client browser
4. Train a model using YOLO (any version) to perform object-detection over the video frames captures
5. Server utilizes the YOLO model onto video frames, allow frames to be annotated with the designated object detection.
6. You will propose the designated object to be detected, one object is sufficient. It can be things like common objects in daily life, company logos, trademarks, or signs, but not limited to these.
7. Do consider augmentation on the training subject, we will evaluate the model performance in real-world usage sense.
'''

# Import
from flask import Flask, Response
import cv2
import numpy as np 
import os
import torch
import time
import uuid

# Constants
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
YOLO_MED_PATH = os.path.join(DIR_PATH,'weights/yolov5m-100epoch-2.pt')
YOLO_PATH = os.path.join(DIR_PATH,'ultralytics/yolov5')
IMAGES_PATH = os.path.join(DIR_PATH, 'data/images') #/data/images
LABELS = ['mask','no_mask','background']
NUM_IMAGES = 10

# Load model
model = torch.hub.load(YOLO_PATH, 'custom', path=YOLO_MED_PATH, force_reload=True,trust_repo=True,source='local') 

# Set model parameters
model.conf = 0.5
model.iou = 0.5

# Define Camera object
class VideoCamera(object):
    def __init__(self):
       #capturing video
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        #releasing camera
        self.video.release()
    
    def get_frame(self):
        #extracting frames
        ret, image = self.video.read()
        results = model(image)
        data = np.squeeze(results.render())

        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


# Define Camera object for training preparation
class CamCapture(VideoCamera):
    
    def capture(self):  
        print("Starting cam capture...")

        #loop through labels
        for label in LABELS:
            print('Collecting images for {}'.format(label))
            time.sleep(5)
    
            # Loop through image range
            for img_num in range(NUM_IMAGES):
                print('Collecting images for {}, image number {}'.format(label, img_num))
                
                # Webcam feed
                ret, frame = self.video.read()
                
                # Naming out image path
                imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
                
                # Writes out image to file 
                cv2.imwrite(imgname, frame)
                
                # Render to the screen
                cv2.imshow('Image Collection', frame)
                
                # 2 second delay between captures
                time.sleep(2)
                
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                
        self.video.release()
        cv2.destroyAllWindows()
