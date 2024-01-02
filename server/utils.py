import json
import pickle
import numpy as np
__location= None
__data_columns= None
__model=None

def get_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1

    x=np.zeros(len(__data_columns))
    x[0]= sqft
    x[1]= bath
    x[2]= bhk
    if loc_index >=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)
def get_location_names():
    return __location

def load_articles():
    print("Loading")
    global __data_columns
    global __location

    with open("./artifacts/banglore_price.json","r") as f:
        __data_columns= json.load(f)['data_columns']
        __location=__data_columns[3:]
    global __model
    with open("./artifacts/banglore_home_price_prediction_model.pickle","rb") as f:
        __model=pickle.load(f)
    print("done")


if __name__=="__main__":
    load_articles()
    print(get_location_names())
    print(get_price('1st Phase JP Nagar',1000,2,2))
    print(get_price('1st Phase JP Nagar',1000,3,3))
    print(get_price('Kalhalli',1000,2,2))
    print(get_price('Ejipura',1000,2,2))