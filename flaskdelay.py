from flask import Flask
from flask import request, jsonify, g
import time
import socket
app = Flask(__name__)


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route('/', methods=['GET'])
def delay():
    """ test for delayed response times """
    hostname = socket.gethostname()
    if 'delay' in request.args:
        delay = int(request.args['delay'])
    else:
        delay = 0
    time.sleep(delay)
    data = {'delay': delay, 'hostname': hostname, 'Render Time': g.request_time()}
    print("Rendered in", g.request_time(), "Seconds")
    return jsonify(data)

app.run()