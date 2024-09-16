from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import numpy as np 
from flask import Flask, request, jsonify

model_path = "../model/model_health_impact_88_0.3223.keras"
scaler = StandardScaler()
model=load_model(model_path)

app = Flask(__name__)

@app.route('/model_exec', method=["POST"])
def execute_model():
    if request.method == 'POST':
        try:
            body = request.get_json()
            np_data = np.array([[body['aqi'], body['pm10'], body['pm25'], body['no2'], body['so3']]])
            std_scaler = scaler.fit_transform(np_data)
            result = set_loading_model.predict(data_nor)
            max_idx = np.argmax(result)
            return max_idx, 200
        except:
            return "interal service error", 500

if __name__ == '__main__':
    # Listen on port 3333
    app.run(host='0.0.0.0', port=3456)