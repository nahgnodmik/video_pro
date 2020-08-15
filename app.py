from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/write', methods=['POST'])

@app.route('/list', methods=['GET'])

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)