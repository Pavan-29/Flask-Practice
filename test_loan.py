import pytest
from loan import app

#Client -> acts as a client to send requests to the application without running the server
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.text == "<h1>Welcome to the loan Application Service</h1>"

def test_predict_get(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 200,
        "CreditHistory": 1
    }
    res = client.post("/predict", json=data)
    assert res.status_code == 200
    assert res.json == {"loan_approval_status": "Approved"}