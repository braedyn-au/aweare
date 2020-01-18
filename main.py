from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/camera")
def camera():
    return render_template("camerapage.html")
    
@app.route("/signup")
def signup():
    return render_template("sign-up.html")

@app.route("/signin")
def signin():
    return render_template("sign-in.html")

@app.route("/invite")
def invite():
    return render_template("invite.html")

@app.route("/problem")
def problem():
    return render_template("problem.html")

if __name__ == "__main__":
    app.run(debug=True)