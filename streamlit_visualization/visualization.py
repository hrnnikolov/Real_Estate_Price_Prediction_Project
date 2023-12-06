import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import pickle
import joblib
#import testingz
import os

path = os.path.dirname(__file__)
my_data = path+'/columns.json'
my_model = path+'/lr_model.joblib'

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Real_Estate_Price_Prediction_Project')

with open(my_data, 'r') as f:
    data = json.load(f)['data_columns']
    location_names= data

with open(my_model, 'rb') as f:
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

st.write(predict_price('2nd Stage Nagarbhavi', 1000, 5, 2))

if st.button('Goals Diagram'):
    # Data set
    height = list(df_onlyplayers['Gls'])
    bars = list(df_onlyplayers['Player'])
    y_pos = np.arange(len(bars))

    # Basic bar plot
    plt.bar(y_pos, height, color=(0.2, 0.4, 0.6, 0.6))
    plt.xticks(y_pos, bars, rotation=90)

    # Custom Axis title
    # plt.xlabel('Players', fontweight='bold', color = 'orange', fontsize='17', horizontalalignment='center')

    # Show the graph
    st.pyplot()

# In[ ]:




