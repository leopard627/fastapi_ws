export DATABASE_CONFIG=""
export REDIS_URL="redis://localhost:6379/1"

uvicorn fastapi_ws.main:app --port 8000 --ws-ping-interval 300 --timeout-keep-alive 300 --ws-ping-timeout 300
