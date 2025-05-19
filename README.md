# AI Journal MVP Backend

## Features
- FastAPI backend with Firestore storage
- Journal CRUD with per-user isolation (via `X-User-ID` header)
- Ready to deploy on Cloud Run

## Development
source $(poetry env info --path)/bin/activate

## Setup
```bash
cp .env.example .env
poetry install
poetry run uvicorn app.main:app --reload
```

## Docker Build
```bash
docker build -t journal-backend .
docker tag journal-backend gcr.io/lytic-brew-mira-development/journal-backend
```

## Cloud Run Deploy
```bash
gcloud run deploy journal-backend \
  --image=gcr.io/lytic-brew-mira-development/journal-backend \
  --platform=managed \
  --region=us-central1 \
  --concurrency=40 \
  --allow-unauthenticated