.PHONY: api api-login webui

api:
	uv run uvicorn packages.api.src.api.main:app

api-login:
	uv run python -m packages.api.src.api.altmain

webui:
	uv run streamlit run packages/webui/src/webui/main.py
