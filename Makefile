install:
	@poetry install

run:
	poetry run uvicorn run:app --reload

lint:
	poetry run flake8 .