from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/camera")
def camera():
    return render_template("camerapage.html")
    
if __name__ == "__main__":
    app.run(debug=True)