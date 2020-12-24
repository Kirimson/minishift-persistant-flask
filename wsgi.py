from flask import Flask
application = Flask(__name__)

def read_file(path):
    text = ""
    try:
      with open(path, "r") as f:
          text = f.read()
    except:
        text = "nothing found"
    return text

@application.route('/')
def hello_world():
    text =  read_file('storage/hello.txt')
    return text

if __name__ == "__main__":
    application.run()
