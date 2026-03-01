from flask import Flask, request, jsonify
from data import assessments
from recommend import recommend_assessments

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Working"

@app.route("/recommend", methods=["POST"])
def recommend():
    user_input = request.get_json()
    result = recommend_assessments(user_input, assessments)
    return jsonify({"recommended_assessments": result})

if __name__ == "__main__":
    app.run(debug=True)