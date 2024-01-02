from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

utils.load_articles()


@app.route("/get_location_names")
def get_location_names():
    response = jsonify({'locations': utils.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    # print("mmmmm")
    return response


@app.route("/predict_price", methods=["POST"])
def predict_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": utils.get_price(location, total_sqft, bhk, bath)}
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Flask Server For Home Price Prediction")
    app.run()
