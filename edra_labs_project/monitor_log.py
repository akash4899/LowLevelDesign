from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Lock

app = Flask(__name__)
socketio = SocketIO(app)
thread = None
thread_lock = Lock()
LOG_FILE_PATH = "E:\LowLevelDesign\edra_labs_project\static\logfile.txt"
last_position = 0
position_lock = Lock()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            print("started execution in background!")
            thread = socketio.start_background_task(target=monitor_file)

def monitor_file():
    global last_position
    while True:
        try:
            with open(LOG_FILE_PATH, 'rb') as f:
                f.seek(0, 2)
                file_size = f.tell()
                if last_position != file_size:
                    buffer_size = 1024
                    if file_size < buffer_size:
                        buffer_size = file_size
                    f.seek(-buffer_size, 2)
                    lines = f.readlines()
                    last_lines = lines[-10:]
                    content = b'\n'.join(last_lines).decode('utf-8')
                    socketio.sleep(1)  # Add a small delay to prevent high CPU usage
                    socketio.emit('log_updates', {'content': content})
                    print("New lines broadcasted")
                    last_position = file_size
                else:
                    pass
        except FileNotFoundError:
            print(f"Error: {LOG_FILE_PATH} not found.")
        except Exception as e:
            print(f"Error while reading the file: {e}")

if __name__ == '__main__':
    socketio.run(app, debug=False, log_output=True, allow_unsafe_werkzeug=True)
