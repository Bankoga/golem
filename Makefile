init:
	pip install -r requirements.txt

test:
	unittest discover . "*_tests.py"