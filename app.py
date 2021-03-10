#dependencies to create flask app and machine learning model

# From flask import flask, render_template, request
# App = Flask(__name__)

# #if we create our own model can use pickle. 
# Model_TSLA = pickle.load(open(‘test_model.pkl’,’rb’))



# #create route for home route
# @app.route("/")

# def home():
#     return render_template('index.html')

# #IF CREATING OWN MODEL.
# #create route for prediction to appear on Tesla.html
# @app.route('/predict',methods=['POST'])

# def predict():
#     predicition = mdoel_TSLA.predict()
#     output = round(prediciton[0],.2)
#     return render_template('Tesla.html',predicition = Tesla Stock Price is: {}.format(output))

# If __name__ == "__main__"
# app.run(debug= True)

from keras.models import load_model 
from keras.backend import set_session
# from skimage.transform import resize
import matplotlib as plt
import tensorflow as tf 
import numpy as np 

print("Loading Model")

global sess 
sess = tf.Session()
set_session(sess)
global model
model = load_model('2021-03-08_TSLA-sh-1-sc-1-sbd-0-huber_loss-adam-LSTM-seq-50-step-4-layers-2-units-256.h5')
global graph 
graph = tf.get_default_graph()


#app route for home
@app.route("/")

def home():
    return render_template('index.html')

#app route for ML Tesla model 
@app.route('/', methods= ['GET','POST'])

def predict():

    predicition = mdoel_TSLA.predict()
    output = round(prediciton[0],.2)
    return render_template('Tesla.html',predicition = 'Tesla Stock Price is: {}.format(output)')

if __name__ == "__main__":
    app.run(debug=True)
