import pickle
import json
import numpy as np

__manufacturer = None
__data_columns = None
__model = None


def get_estimated_price(m,f,t,o,year,km_driven,mileage,engine,power,seats): 
    try:
        loc_index1 = __data_columns.index("Manufacturer_"+m)
    except:
        loc_index1 = -1   
    try:
        loc_index2 = __data_columns.index("Fuel_Type_"+f)
    except:
        loc_index2 = -1   
    try:
        loc_index3 = __data_columns.index("Transmission_"+t)
    except:
        loc_index3 = -1   
    try:
        loc_index4 = __data_columns.index("Owner_Type_"+o)
    except:
        loc_index4 = -1   
    x = np.zeros(len(__data_columns))
    x[0] = year
    x[1] = km_driven
    x[2] = mileage
    x[3] = engine
    x[4] = power
    x[5] = seats
    if loc_index1 >= 0:
        x[loc_index1] = 1
    if loc_index2 >= 0:
        x[loc_index2] = 1
    if loc_index3 >= 0:
        x[loc_index3] = 1
    if loc_index4 >= 0:
        x[loc_index4] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __manufacturer

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __manufacturer = __data_columns[6:30] 

    global __model
    if __model is None:
        with open('./artifacts/used_car_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_manufacturer_names():
    return __manufacturer

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_manufacturer_names())
    print(get_estimated_price("Tata","Petrol","Auto","First",5,18350,22,625,37.5,4))