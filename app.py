from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    video_files = []
    
    for filename in os.listdir('static/videos'):
        if filename.endswith('.mp4'):
            video_files.append(filename)
    
    
    return render_template('index.html', video_files=video_files)

if __name__ == '__main__':
    app.run(debug=True)