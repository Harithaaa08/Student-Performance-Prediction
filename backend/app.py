from flask import Flask, request, jsonify
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)

model_path = Path(__file__).resolve().parent / "student_performance_model.pkl"
model = joblib.load(model_path)
print(f"✅ Model loaded from {model_path}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        val = data.get('extracurricular')
        if isinstance(val, str):
            extracurricular = 1 if val == 'Yes' else 0
        else:
            try:
                extracurricular = 1 if int(val) == 1 else 0
            except Exception:
                extracurricular = 0

        input_df = pd.DataFrame([{
            'Hours Studied': data['hours_studied'],
            'Previous Scores': data['previous_scores'],
            'Extracurricular Activities': extracurricular,
            'Sleep Hours': data['sleep_hours'],
            'Sample Question Papers Practiced': data['question_papers']
        }])

        prediction = model.predict(input_df)

        return jsonify({'prediction': float(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
