#dependencies to create flask app and machine learning model

from flask import flask, render_template, request
app = Flask(__name__)

#if we create our own model can use pickle. 
filename = "prac_save.sav"
Model_TSLA = pickle.load(open(filename, "rb"))



#create route for home route
@app.route("/")

def home():
    return render_template('index.html')

#IF CREATING OWN MODEL.
#create route for prediction to appear on Tesla.html
@app.route('/predict',methods=['POST'])

def predict():
    predicition = mdoel_TSLA.predict()
    output = round(prediciton[0],.2)
    return render_template('Tesla.html',predicition = "Tesla Stock Price is: {}.format(output)")

if __name__ == "__main__"
    app.run(debug= True)
