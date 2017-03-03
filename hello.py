import os 
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def telytalk():
    return render_template("index.html")

@app.route("/sign_up")
def sign_up():
	 return render_template("sign_up.html")

@app.route("/profile")
def profile():
	 return render_template("profile.html")
	 


if __name__ == "__main__":
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    