from flask import Flask, request, render_template
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

#initiate flask
app = Flask('__name__')

app.static_folder = 'static'

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('clothmodel.h5')

# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        x=pd.DataFrame.from_dict(params, orient='index').transpose()
        with graph.as_default():
            data["prediction"] = str(model.predict(x)[0][0])
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data) 

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
    app.run(debug=True, host='0.0.0.0')