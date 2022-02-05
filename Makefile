VENV_NAME=./venv
PIP_LOCATION=$(VENV_NAME)/bin/pip
PWD:=$(shell pwd)
SERIES_DIRECTORY:=$(PWD)/vlc_controller/tests/test_episodes
LOG_FILE:=


setup-venv:
	if [ ! -d $(VENV_NAME) ]; then python3 -m venv $(VENV_NAME); else echo "Skipping venv creation"; fi

setup-systemd-service:
	sudo cp ./remote_controller/remote_controller.service /etc/systemd/user
	systemctl daemon-reload --user
	systemctl enable remote_controller --user

install-apt-deps:
	sudo apt-get install vlc ir-keytable -y

install-deps: setup-venv
	$(PIP_LOCATION) install -e vlc_controller
	$(PIP_LOCATION) install -e remote_controller

install-dev-deps: setup-venv
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

run-controller: setup-ir-keys
	if [ ! -z $(LOG_FILE) ]; then\
		./venv/bin/python -m remote_controller -d $(SERIES_DIRECTORY)  -l $(LOG_FILE);\
	else\
	  	./venv/bin/python -m remote_controller -d $(SERIES_DIRECTORY);\
  	fi

lint:
	./venv/bin/python -m mypy vlc_controller
	./venv/bin/python -m mypy remote_controller

format:
	./venv/bin/python -m black .