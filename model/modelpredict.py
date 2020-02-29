# WorkLite Regression Prediction

import pickle
import numpy as np

def predict_claim(model, lst):
    
    client_data = np.array(lst)
    prediction = model.predict(client_data.reshape(1, -1))
    if prediction <= 0:
        return 0
    else:
        return prediction

def main():
    
    client_data = [0, 1, 1, .5, .2, 1, 0, 1, 1, 0, 0, 1, 0, 0]
    model = pickle.load(open('modelparams.sav', 'rb'))
    predicted_value = predict_claim(model, client_data)
    
    print(round(predicted_value[0], 2))
    
main()