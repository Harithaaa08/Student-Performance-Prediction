Student Performance Prediction App

This project is a Machine Learning web application that predicts the performance index of students based on features like hours studied, previous scores, sleep hours, extracurricular activities, and number of question papers practiced. It uses a Random Forest Regressor model trained with a sample dataset. The project includes a Flask backend API and a Streamlit frontend for user interaction.

Features

Predicts student performance index (numerical score) based on user input.

Handles categorical input like extracurricular activities (Yes/No) and converts it for model prediction.

Easy-to-use web interface using Streamlit.

API built with Flask for model inference.

Project Structure
Student-Performance-Prediction/
│
├── backend/
│ ├── app.py # Flask API for model predictions
│ ├── train_save.py # Script to train and save model
│ ├── student_performance_model.pkl # Trained ML model
│ ├── data/
│ │ ├── load_data.py # Load CSV dataset
│ │ ├── preprocess_data.py # Preprocess dataset for ML
│ └── model/
│ └── train_model.py # ML model training logic
│
├── frontend/
│ └── app.py # Streamlit app for user interface
│
├── dataset/
│ └── student_performance.csv # Sample student dataset
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

Installation

Clone the repository:

git clone <your-repo-url>
cd Student-Performance-Prediction

Create a virtual environment and activate it (optional but recommended):

python -m venv venv

# Windows

venv\Scripts\activate

# macOS/Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

How to Run

1. Train the Model (if not already trained)
   cd backend
   python train_save.py

This will create student_performance_model.pkl.

2. Run Flask API
   python app.py

The API will run at http://127.0.0.1:5000.

3. Run Streamlit Frontend
   cd frontend
   streamlit run app.py

Open the URL provided by Streamlit in your browser to use the app.

Sample Input
Hours Studied Previous Scores Extracurricular Sleep Hours Question Papers
7 82 Yes 8 3
Output

The app predicts a Performance Index, e.g., 78.5.

Technologies Used

Python 3

Flask (Backend API)

Streamlit (Frontend UI)

Pandas, NumPy (Data handling)

Scikit-learn (Machine Learning)

Joblib (Model persistence)

Notes

Ensure the backend is running before using the frontend.

The dataset used is a sample dataset. Accuracy may vary with real data.

You can modify the frontend design to improve the user experience.

---

## ✅ Testing & CI

- Run the project tests locally without pytest by executing:

```bash
python backend/run_tests.py
```

- A GitHub Actions workflow (`.github/workflows/ci.yml`) is included to run the test suite on push and pull requests (requires Python 3.10+).

**Tip:** If you prefer `pytest`, install it (`pip install pytest`) and run `pytest` in the project root.
