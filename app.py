from flask import Flask,render_template,Response, request ,jsonify

import cv2
from main import callgem
from gemini import gemin

app=Flask(__name__)

# def generate_frames():
#     while True:
#         #read the camera frame
#         success,frame=camera.read()s
#         if not success :
#             break
#         else:
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame = buffer.tobytes()

#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/video')
# def video():
#     return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/call')
def call():
    return Response(callgem())

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message', '')
    # Call your Python function here
    response = codefunc(message)
    return jsonify({'response': response})

def codefunc(message):
    # Your backend function logic here
    print("code :  ")
    print(message)
    k=gemin(message)
    print(k)
    return k



if __name__=='__main__':
    app.run(debug=True)


