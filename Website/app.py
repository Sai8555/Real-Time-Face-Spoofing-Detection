# # # from flask import Flask, render_template, request, jsonify
# # # import subprocess
# # # import threading

# # # app = Flask(__name__)

# # # # Global variable to store the process running the Python script
# # # process = None

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # @app.route('/detection')
# # # def detection():
# # #     # return render_template('index.html')
# # #     return render_template('detection page.html')

# # # @app.route('/start_liveness', methods=['POST'])
# # # def start_liveness():
# # #     global process
# # #     if process is None:
# # #         # Start the Python script in a separate thread
# # #         def run_script():
# # #             global process
# # #             process = subprocess.Popen(['python', 'Face_liveness/run.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # #             process.wait()
# # #             process = None  # Reset the process after it finishes

# # #         threading.Thread(target=run_script).start()
# # #         return jsonify({'status': 'success', 'message': 'Liveness testing started.'})
# # #     return jsonify({'status': 'error', 'message': 'Liveness testing is already running.'})

# # # @app.route('/stop_liveness', methods=['POST'])
# # # def stop_liveness():
# # #     global process
# # #     if process is not None:
# # #         process.terminate()  # Terminate the running process
# # #         process = None
# # #         return jsonify({'status': 'success', 'message': 'Liveness testing stopped.'})
# # #     return jsonify({'status': 'error', 'message': 'No liveness testing process is running.'})

# # # # # from Face_liveness.run import generate_frames  # Make sure Face_liveness has an __init__.py
# # # # import sys
# # # # sys.path.append('../')  # or the exact path where Face_liveness is
# # # # from Face_liveness.run import generate_frames

# # # # @app.route('/video_feed')
# # # # def video_feed():
# # # #     return Response(generate_frames(),
# # # #                     mimetype='multipart/x-mixed-replace; boundary=frame')

# # # if __name__ == '__main__':
# # #     app.run(debug=True)





# # from flask import Flask, render_template, Response, request, jsonify
# # import cv2
# # import threading
# # import time
# # import numpy as np
# # from tensorflow.keras.models import load_model
# # from tensorflow.keras.utils import img_to_array

# # app = Flask(__name__)
# # model = load_model("face_antispoofing_model.h5")
# # threshold = 0.8

# # # Global variables
# # camera = None
# # streaming = False
# # result_status = "Start"

# # def generate_frames():
# #     global camera, streaming, result_status
# #     live_start_time = None
# #     result_status = "Detecting..."  # Reset at the beginning of detection

# #     while streaming:
# #         success, frame = camera.read()
# #         if not success:
# #             break

# #         resized_frame = cv2.resize(frame, (224, 224))
# #         image_array = img_to_array(resized_frame) / 255.0
# #         prediction = model.predict(np.expand_dims(image_array, axis=0))[0][0]
# #         label = "Live Image" if prediction <= threshold else "Not Live Image - Spoofed"
# #         color = (0, 255, 0) if label == "Live Image" else (0, 0, 255)

# #         # Track liveness duration
# #         if label == "Live Image":
# #             if live_start_time is None:
# #                 live_start_time = time.time()
# #             elif time.time() - live_start_time >= 5:
# #                 result_status = "Live Face Confirmed"
# #                 streaming = False
# #                 if camera:
# #                     camera.release()
# #                 break
# #         else:
# #             live_start_time = None
# #             result_status = "Detecting..."

# #         # Overlay label
# #         cv2.putText(frame, f"{label} (Score: {prediction:.2f})", (10, 30),
# #                     cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

# #         ret, buffer = cv2.imencode('.jpg', frame)
# #         frame_bytes = buffer.tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/detection')
# # def detection():
# #     return render_template('detection page.html')

# # @app.route('/video_feed')
# # def video_feed():
# #     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # @app.route('/status')
# # def status():
# #     global result_status
# #     return jsonify({'status': result_status})

# # @app.route('/start_liveness', methods=['POST'])
# # def start_liveness():
# #     global camera, streaming, result_status
# #     if not streaming:
# #         result_status = "Detecting..."  # Reset here
# #         camera = cv2.VideoCapture(1)
# #         if not camera.isOpened():
# #             return jsonify({'status': 'error', 'message': 'Could not open webcam'})
# #         streaming = True
# #         return jsonify({'status': 'success'})
# #     return jsonify({'status': 'already_running'})

# # @app.route('/stop_liveness', methods=['POST'])
# # def stop_liveness():
# #     global camera, streaming, result_status
# #     if streaming:
# #         streaming = False
# #         result_status = "Live Face"  # Reset to default
# #         if camera:
# #             camera.release()
# #         return jsonify({'status': 'success'})
# #     return jsonify({'status': 'not_running'})

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, Response, request, jsonify
# import cv2
# import threading
# import time
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.utils import img_to_array

# app = Flask(__name__)
# model = load_model("face_antispoofing_model.h5")
# threshold = 0.8

# # Global variables
# camera = None
# streaming = False
# result_status = "Ready"  # Changed from "Start" to be more descriptive

# def generate_frames():
#     global camera, streaming, result_status
#     live_start_time = None
#     result_status = "Detecting..."  # Reset at the beginning of detection

#     while streaming:
#         success, frame = camera.read()
#         if not success:
#             result_status = "Camera Error"
#             streaming = False
#             break

#         resized_frame = cv2.resize(frame, (224, 224))
#         image_array = img_to_array(resized_frame) / 255.0
#         prediction = model.predict(np.expand_dims(image_array, axis=0))[0][0]
#         label = "Live Image" if prediction <= threshold else "Not Live Image - Spoofed"
#         color = (0, 255, 0) if label == "Live Image" else (0, 0, 255)

#         # Track liveness duration
#         if label == "Live Image":
#             if live_start_time is None:
#                 live_start_time = time.time()
#                 result_status = "Live Face Detected"
#             elif time.time() - live_start_time >= 5:
#                 result_status = "Live Face Confirmed"
#                 streaming = False
#                 if camera:
#                     camera.release()
#                 break
#         else:
#             live_start_time = None
#             result_status = "Spoof Detected"

#         # Overlay label
#         cv2.putText(frame, f"{label} (Score: {prediction:.2f})", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame_bytes = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/detection')
# def detection():
#     return render_template('detection page.html')

# @app.route('/video_feed')
# def video_feed():
#     global streaming, camera
#     if not streaming or camera is None:
#         # Return a blank frame if not streaming
#         blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
#         ret, buffer = cv2.imencode('.jpg', blank_frame)
#         frame_bytes = buffer.tobytes()
#         return Response(b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n',
#                mimetype='multipart/x-mixed-replace; boundary=frame')
    
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/status')
# def status():
#     global result_status
#     return jsonify({'status': result_status})

# @app.route('/start_liveness', methods=['POST'])
# def start_liveness():
#     global camera, streaming, result_status
    
#     # Make sure to close any existing camera
#     if camera is not None:
#         camera.release()
#         camera = None
    
#     # Try camera index 0 first (default webcam)
#     camera = cv2.VideoCapture(1)
#     if not camera.isOpened():
#         # Try camera index 1 as fallback
#         camera = cv2.VideoCapture(0)
#         if not camera.isOpened():
#             return jsonify({'status': 'error', 'message': 'Could not open webcam'})
    
#     streaming = True
#     result_status = "Detecting..."
#     return jsonify({'status': 'success'})

# @app.route('/stop_liveness', methods=['POST'])
# def stop_liveness():
#     global camera, streaming, result_status
#     streaming = False
#     result_status = "Ready"  # Reset to default
#     if camera:
#         camera.release()
#         camera = None
#     return jsonify({'status': 'success'})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, Response, request, jsonify
import cv2
import threading
import time
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array

app = Flask(__name__)
model = load_model("face_antispoofing_model.h5")
threshold = 0.8

# Global variables
camera = None
streaming = False
result_status = "Start"

def generate_frames():
    global camera, streaming, result_status
    live_start_time = None
    result_status = "Detecting..."  # Reset at the beginning of detection

    while streaming:
        success, frame = camera.read()
        if not success:
            break

        resized_frame = cv2.resize(frame, (224, 224))
        image_array = img_to_array(resized_frame) / 255.0
        prediction = model.predict(np.expand_dims(image_array, axis=0))[0][0]
        label = "Live Image" if prediction <= threshold else "Not Live Image - Spoofed"
        color = (0, 255, 0) if label == "Live Image" else (0, 0, 255)

        # Track liveness duration
        if label == "Live Image":
            if live_start_time is None:
                live_start_time = time.time()
            elif time.time() - live_start_time >= 5:
                result_status = "Live Face Confirmed"
                streaming = False
                if camera:
                    camera.release()
                break
        else:
            live_start_time = None
            result_status = "Detecting..."

        # Overlay label
        cv2.putText(frame, f"{label} (Score: {prediction:.2f})", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detection')
def detection():
    return render_template('detection page.html')

@app.route('/video_feed')
def video_feed():
    global streaming, camera
    if not streaming or camera is None:
        # Return a blank frame if not streaming
        blank_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        ret, buffer = cv2.imencode('.jpg', blank_frame)
        frame_bytes = buffer.tobytes()
        return Response(b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n',
                       mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    global result_status
    return jsonify({'status': result_status})

@app.route('/start_liveness', methods=['POST'])
def start_liveness():
    global camera, streaming, result_status
    
    # Make sure any existing camera is released
    if camera is not None:
        camera.release()
        camera = None
    
    # Start with a fresh camera
    camera = cv2.VideoCapture(1)  # Try camera index 0 first
    
    if not camera.isOpened():
        camera = cv2.VideoCapture(1)  # If 0 doesn't work, try index 1
        
    if not camera.isOpened():
        return jsonify({'status': 'error', 'message': 'Could not open webcam'})
    
    streaming = True
    result_status = "Detecting..."
    return jsonify({'status': 'success'})

@app.route('/stop_liveness', methods=['POST'])
def stop_liveness():
    global camera, streaming, result_status
    streaming = False
    result_status = "Ready"
    if camera:
        camera.release()
        camera = None
    return jsonify({'status': 'success', 'message': result_status})

if __name__ == '__main__':
    app.run(debug=True, port=5001)