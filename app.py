from flask import Flask, g, jsonify

__all__ = ['app']
app = Flask(__name__)

@app.route('/')
def index():
  return '<h2>Welcome to MongoDB System</h2>'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)
