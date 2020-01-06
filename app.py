# load Flask 
import flask
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras import backend as back
import os
import numpy as np
from numpy import loadtxt

app = flask.Flask(__name__)
# define a predict function as an endpoint 
@app.route("/", methods=["GET","POST"])

def getPrediction():
    values = []
    keys = []
    model = 1
    # check for passed in parameters   
    params = flask.request.get_json()
    print(flask.request.get_json())
    if params is None:
        params = flask.request.args
    print(params)
    # if parameters are found, echo the msg parameter 
    if "model" in params.keys(): 
        model = int(params["model"])
        for key,value in params.items():
            if(key != "model"):
                print(type(value))
                print(value)
                values.append(value)
    
    print(model, values)
    back.clear_session()
    prediction, acc = predictClass(model, values)
    back.clear_session()

    result = {
        'prediction': prediction,
        'acc': acc
    }
    # return a response in json format 
    print("RETURNING ")
    print(result)
    return flask.jsonify(result)

def predictClass(inmodel, inputs):
    # load correct model
    model = load_model(inmodel)

    # add inputs to np array
    test = np.array([inputs])
    # test - numpy array with vars
    prediction = model.predict(test)

    if inmodel == 1:
        datasetPath = './datasets/pima_indians_diabetes.csv'
        dataset = loadtxt(datasetPath, delimiter=',')

        inputData = dataset[:,0:8]
        output = dataset[:,8]

        acc = model.evaluate(inputData, output)
    
    elif inmodel == 2:
        datasetPath = './datasets/breast_cancer.csv'
        dataset = loadtxt(datasetPath, delimiter=',')

        inputData = dataset[:,0:9]
        output = dataset[:,9]

        acc = model.evaluate(inputData, output)
    
    elif inmodel == 3:
        datasetPath = './datasets/heart_disease.csv'
        dataset = loadtxt(datasetPath, delimiter=',')

        inputData = dataset[:,0:13]
        output = dataset[:,13]

        acc = model.evaluate(inputData, output)

    # add this to json and return prediction[0]*100
    return int(prediction[0]*100), int(acc[1]*100)

    # add patient details to database

def load_model(model):
    loaded_model = None
    if(model == 1):
        json_file = open('models/diab_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("models/diab_model.h5")
        loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    elif(model == 2):
        json_file = open('models/cancer_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("models/cancer_model.h5")
        loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    elif(model == 3):
        json_file = open('models/heartd_model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("models/heartd_model.h5")
        loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    else:
        print("No model loaded")
    
    
    return loaded_model

# start the flask app, allow remote connections
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(debug=False, port=port, threaded=False)

