from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_manufacturer_names', methods=['GET'])
def get_manufacturer_names():
    response = jsonify({
        'manufacturers': util.get_manufacturer_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_used_car_price', methods=['GET', 'POST'])
def predict_used_car_price():

    m = request.form['Manufacturer']
    f = request.form['Fuel_Type']
    t = request.form['Transmission']
    o = request.form['Owner_Type']
    year = int(request.form['Year'])
    km_driven = float(request.form['KM_Driven'])
    mileage = float(request.form['Mileage'])
    engine = float(request.form['Engine'])
    power = float(request.form['Power'])
    seats = int(request.form['Seats'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(m,f,t,o,year,km_driven,mileage,engine,power,seats)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For used_car Price Prediction...")
    util.load_saved_artifacts()
    app.run()