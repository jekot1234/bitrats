from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/js/<path:path>')
def script(path):
    return send_from_directory('js', path)

def main(*args, **kwargs):
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)

    

if __name__ == '__main__':
    main()
else:
    gmain = main()