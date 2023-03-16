# facemask-detector
Author: Jethro Au
Date: 16 Mar, 2023

This is the repo for buildin a simple web-cam facemask detector

Chosen detection object: Mask

## Function Specifications
1. Provide a simple system for Web Based Video Live Streaming with AI Object Detection Function
2. Client will be any modern web browser like Chrome
3. Server connects to IP Cam or Web Cam, serve a simple webpage through HTTP to display the video frames on Client browser
4. Train a model using YOLO (any version) to perform object-detection over the video frames captures
5. Server utilizes the YOLO model onto video frames, allow frames to be annotated with the designated object detection.
6. You will propose the designated object to be detected, one object is sufficient. It can be things like common objects in daily life, company logos, trademarks, or signs, but not limited to these.
7. Do consider augmentation on the training subject, we will evaluate the model performance in real-world usage sense.

# Run specifications
