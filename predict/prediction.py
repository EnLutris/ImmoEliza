import pickle
from sklearn import metrics
import pandas as pd

# load the model from disk
loaded_model = pickle.load(open('model/multiple_linear_reg.pkl', 'rb'))


def prediction(preproccesed_data):
   
    columns = ['post_code', 'garden', 'terrace', 'area', 'bedrooms', 'plot_surface', 'garden_area', 'swimming_pool', 'open_fire', 'terrace_area', 'facades', 'build_condition', 'kitchen']
    df = pd.DataFrame(preproccesed_data, index = columns).T


    prediction = loaded_model.predict(df)

    result = {'prediction': prediction[0][0], "status_code": 200}

    return result