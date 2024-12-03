from flask import Flask, render_template, Response
from log_file_monitor import Monitor
import time



app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/log_updates')
def log_updates():
    def generate_updates():
        while True:
            yield f"data: {','.join(log_monitor.monitor_log())}\n\n"
            time.sleep(1)
    return Response(generate_updates())

if __name__ == '__main__':
    log_monitor = Monitor('E:\LowLevelDesign\edra_labs\log.txt')
    log_monitor.start()
    app.run(debug=True)