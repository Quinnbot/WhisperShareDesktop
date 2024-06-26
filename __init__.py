from flask import Flask, request
from subprocess import Popen
import shlex

app = Flask(__name__)

playing = Popen

@app.route('/json', methods=['POST'])
def json():
    global playing
    # Get the JSON data from the request
    data = request.get_json()
    # Print the data to the console
    print(data['link'])

    try:
        if playing.poll() == None:
            print("killing last")
            playing.kill()
        playing = Popen(shlex.split('{0} {1} {2}'.format('mpv', '--fs', data['link'])))
        
    except:
        playing = Popen(shlex.split('{0} {1} {2}'.format('mpv', '--fs', data['link'])))
        
    return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
