# facemask-detector
Author: Jethro Au

Date: 16 Mar, 2023

This is the repo for buildin a simple web-cam facemask detector using the YOLOv5m model.

Chosen detection object: **Mask**

# Specifications
- For demo purposes, this application will mount the device(0) webcam
- The src uses the YOLOv5M model trained on 100epochs. In the data folder, there are three other models that can be chosen. YOLOV5m was selected based on mAP0.5 performance metric
- Larger models were not used (such as the YOLOv5l) due to slow run time with streaming data
- it will connect to port:3000, please make sure there are no other applications using this port or else you will not be able to connect.

## Option 1 - Install and run source code via pip install requirements.txt
Clone repo and install requirements.txt in a Python>=3.8.0 environment, including PyTorch>=1.7. This code was developed in Python==3.9 environment.

```
git clone https://github.com/jethrocsau/facemask-detector # clone
pip install -r requirements.txt  # install
cd src
python main.py
```

## Option 2 - install the pyinstaller executable 

1. Install the executable this link here (https://drive.google.com/file/d/1JjTpa9CG9B9NCvZT_ha8fedTRvtit3xE/view?usp=sharing)
2. Open "main" folder
3. Run "main" file

# Reference Specifications
1. Provide a simple system for Web Based Video Live Streaming with AI Object Detection Function
2. Client will be any modern web browser like Chrome
3. Server connects to IP Cam or Web Cam, serve a simple webpage through HTTP to display the video frames on Client browser
4. Train a model using YOLO (any version) to perform object-detection over the video frames captures
5. Server utilizes the YOLO model onto video frames, allow frames to be annotated with the designated object detection.
6. You will propose the designated object to be detected, one object is sufficient. It can be things like common objects in daily life, company logos, trademarks, or signs, but not limited to these.
7. Do consider augmentation on the training subject, we will evaluate the model performance in real-world usage sense.
