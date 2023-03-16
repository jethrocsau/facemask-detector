# main.py
# import packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import numpy as np
import cv2
import webbrowser
import os
import time

#configure flask
app = Flask(__name__)

@app.route('/')
#rendering webpage
def index():
    # rendering webpage
    return render_template('index.html')

# define get camera function & format yield
def gen(camera):
    # init error counter 
    err_count = 0

    #try for 10 times max with 1 sec sleep timer
    while err_count <=10:
        try: 
            #get camera frame
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except Exception as e:
            print("Error getting frame: ", e)
            time.sleep(1)
            err_count += 1
    if err_count >10:
        print("Failed to generate camera image..please check the source of error")
        shutdown()

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def main():
    # open browser if reloader not yet run
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:3000/')

    # Otherwise, continue as normal
    app.run(host='0.0.0.0',port='3000', debug=True)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

# Run Flask
if __name__ == '__main__':
    # defining server ip address and port
    main()