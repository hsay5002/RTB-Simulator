# RTB-Simulator

A lightweight simulation framework for **Real-Time Bidding (RTB)** in digital advertising. This version includes a basic **Flask API**, unit tests with **Pytest**, a **Dockerfile**, and a GitHub Actions-based **CI pipeline**.

---

## 🚀 Features

- Simulate bidding using advertisers and campaigns
- Run auctions based on keyword targeting
- RESTful Flask API to handle bid requests
- Unit testing with Pytest
- Docker support for containerized deployment
- GitHub Actions workflow for automated testing

---

## 🏗️ Project Structure

```
.
├── .github/workflows/python-ci.yml   # GitHub Actions CI workflow
├── .gitignore                        # Ignored files
├── Dockerfile                        # Container build
├── flask_api.py                      # Flask server with /bid endpoint
├── test_simulator.py                 # Unit tests
├── ad_exchange.py                    # AdExchange logic (pre-existing)
├── entities.py                       # Campaign and Advertiser classes (pre-existing)
```

---

## 🧪 Running Tests

Make sure you have `pytest` installed:

```bash
pip install pytest
pytest
```

---

## 🌐 Running the Flask API

Install dependencies and start the server:

```bash
pip install flask
python flask_api.py
```

Send a sample bid request (e.g., using Postman or curl):

```bash
curl -X POST http://127.0.0.1:5000/bid \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "keywords": ["sports", "shoes"]}'
```

---

## 🐳 Run with Docker

Build and run:

```bash
docker build -t rtb-simulator .
docker run -p 5000:5000 rtb-simulator
```

---

## ✅ CI Pipeline

This repository uses **GitHub Actions** to automatically run unit tests on every push or pull request to the `main` branch.

Workflow defined in: `.github/workflows/python-ci.yml`

---

## 📌 Example Bid Request

**POST** `/bid`

```json
{
  "id": 1,
  "keywords": ["sports", "shoes"]
}
```

**Response**

```json
{
  "winner": "Nike Inc.",
  "price": 0.01
}
```

---

## 🛠️ Requirements

- Python 3.10
- Flask
- Pytest

---

## 👨‍💻 Author

Yash Guleria ([@hsay5002](https://github.com/hsay5002))
