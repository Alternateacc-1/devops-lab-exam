# DevOps Lab Exam — GitHub Actions CI/CD

A small Flask app with a GitHub Actions pipeline (`.github/workflows/ci-cd.yml`).

On every push to `main`:

1. **build-and-test** — installs Python 3.12 and the requirements, runs `pytest`.
2. **docker-build** — runs only if the tests pass: builds the Docker image, starts the container and checks `/health`.

Run locally:

```bash
pip install -r requirements.txt
pytest -v
python app.py   # http://localhost:5000
```
