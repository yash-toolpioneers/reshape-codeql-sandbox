import os
import sys
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run_command():
    user_input = request.args.get('cmd')
    os.system(user_input)
    return "done"

@app.route('/file')
def read_file():
    filename = request.args.get('name')
    with open(filename, 'r') as f:
        return f.read()
