install:
	@poetry install

run:
	poetry run uvicorn run:app --reload

lint:
	poetry run flake8 .

migration:
	poetry run alembic revision --autogenerate