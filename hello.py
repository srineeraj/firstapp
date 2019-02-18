from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "First Flask App.."

if __name__ == '__main__':
	app.run(port=5000, debug=True)


