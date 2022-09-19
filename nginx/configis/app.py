from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def print_hostname():
  return str(os.environ['CONFIG']) + '\n'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
