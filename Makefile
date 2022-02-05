VENV_NAME=./venv
PIP_LOCATION=$(VENV_NAME)/bin/pip
PWD:=$(shell pwd)

setup:
	if [ ! -d $(VENV_NAME) ]; then python3 -m venv $(VENV_NAME); else echo "Skipping venv creation"; fi

install-apt-deps:
	sudo apt-get install vlc ir-keytable -y

install-deps: setup
	$(PIP_LOCATION) install -e vlc_controller
	$(PIP_LOCATION) install -e remote_controller

install-dev-deps: setup
	$(PIP_LOCATION) install -r dev_requirments.txt

setup-ir-keys: install-apt-deps
	sudo ir-keytable -p all
	sudo ir-keytable

install: install-dev-deps install-deps

test-ir-keys:
	ir-keytable -t -s rc0

vlc-controller-tests:
	./venv/bin/python -m pytest vlc_controller/tests

tests: vlc-controller-tests

run-controller:
	./venv/bin/python -m remote_controller -d $(PWD)/vlc_controller/tests/test_episodes

lint:
	./venv/bin/python -m mypy vlc_controller
	./venv/bin/python -m mypy remote_controller

format:
	./venv/bin/python -m black .