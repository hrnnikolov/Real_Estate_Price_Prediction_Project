import streamlit as st
import numpy as np
import json
import joblib
import os
import base64


def predict_price(location, sqft, bath, bedrooms):
    try:
        loc_index = location_names.index(location)
    except:
        loc_index  = -1

    x = np.zeros(len(location_names))
    x[0] = sqft
    x[1] = bath
    x[2] = bedrooms

    if loc_index >= 0:
        x[loc_index] = 1

    return str(model1.predict([x])[0])


def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


path = os.path.dirname(__file__)
my_data = path+'/columns_upper.json'
my_model = path+'/lr_model.joblib'
background_png = path+'/background.png'

#set_bg_hack(background_png)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Real Estate Price Prediction')

with open(my_data, 'r') as f:
    location_names = json.load(f)['data_columns']
    #location_names= data

with open(my_model, 'rb') as f:
    model1 = joblib.load(f)

# st.markdown("<span style='color:red'>Location</span>",
#              unsafe_allow_html=True)

location = st.selectbox('Location', location_names[3:])
area = st.text_input('Area in square feet')
baths = st.text_input('How many baths')
bedrooms = st.text_input('How many rooms')

if st.button('Calculate price'):
    #st.write(predict_price(location_names, area, baths, bedrooms))
    st.markdown(f'The ***price*** for a ***{area}*** sqft apartment in ***{location}*** with ***{bedrooms}*** bedrooms and ***{baths}***'
                f' bathrooms will be ***{float(predict_price(location, area, baths, bedrooms))*1200:.2f}$***')




