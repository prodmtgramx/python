from flask import Flask
import json
import predykcja as pred
app = Flask(__name__)

@app.route("/predict")
def hello():
    return json.dumps(pred.predict(500))

if __name__ == "__main__":
    app.run(debug=True)