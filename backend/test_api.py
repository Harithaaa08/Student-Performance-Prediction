import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "hours_studied": 7,
    "previous_scores": 85,
    "extracurricular": "Yes",
    "sleep_hours": 8,
    "question_papers": 3
}

response = requests.post(url, json=data)

print(response.json())
