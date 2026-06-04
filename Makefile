run:
	python -m nova.src.pipeline

try:
	python -m prep_code.python.day_1

test: 
	python -m pytest -v nova/tests/