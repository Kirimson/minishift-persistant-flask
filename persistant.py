from flask import Flask
app = Flask(__name__)

def read_file(path):
    text = ""
    with open(path, "r") as f:
        text = f.read()
    return text

@app.route('/')
def hello_world():
    text =  read_file('storage/hello.txt')
    return text
