
all: venv/.ok

venv:
	virtualenv venv -p python3

venv/.ok: venv Makefile requirements.txt
	./venv/bin/pip install -r requirements.txt
	touch venv/.ok

clean:
	rm -rf venv
