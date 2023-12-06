import joblib
import numpy as np
import json
import pickle

with open('./data/columns.json', 'r') as f:
    data = json.load(f)['data_columns']
    location_names= data


with open('./data/lr_model.joblib', 'rb') as f:
    model1 = joblib.load(f)



def predict_price(location, sqft, bath, bedrooms):
    try:
        loc_index = location_names.index(location.lower())
    except:
        loc_index  = -1

    x = np.zeros(len(location_names))
    x[0] = sqft
    x[1] = bath
    x[2] = bedrooms

    if loc_index >= 0:
        x[loc_index] = 1

    return str(model1.predict([x])[0])


print(predict_price('2nd Stage Nagarbhavi', 1000, 5, 2))

