run:
	uv run --offline -- uvicorn --host=0.0.0.0 --port=8000 src.ram_api.server:app

run-docker:
	docker compose up --build
