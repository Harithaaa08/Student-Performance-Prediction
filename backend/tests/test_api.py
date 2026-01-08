from backend.app import app


def test_predict_api():
    client = app.test_client()
    payload = {
        "hours_studied": 6,
        "previous_scores": 80,
        "extracurricular": "No",
        "sleep_hours": 7,
        "question_papers": 3
    }

    resp = client.post('/predict', json=payload)
    assert resp.status_code == 200
    data = resp.get_json()
    assert 'prediction' in data
