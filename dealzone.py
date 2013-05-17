from flask import Flask,render_template
import libdeals

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', deals=libdeals.getSteamDeals())

if __name__ == '__main__':
  app.config["DEBUG"] = True
  app.run(host='0.0.0.0', port=5001)
