#dependencies to create flask app and machine learning model

From flask import flask, render_template, request
App = Flask(__name__)
Model_TSLA = pickle.load(open(‘model_tesla.pkl’,’rb’))

#create route for home route
@app.route("/")

def home():
    return render_template('index.html')
#create route for prediction to appear on Tesla.html
@app.route('/predict',methods=['POST'])

def predict():
    predicition = mdoel_TSLA.predict()
    output = round(prediciton[0],.2)
    return render_template('Tesla.html',predicition = Tesla Stock Price is: {}.format(output))

If __name__ == "__main__"
app.run(debug= True)
