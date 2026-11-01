run:
	uv run -- uvicorn --host=0.0.0.0 --port=8000 src.recognize_anything_api.server:app
