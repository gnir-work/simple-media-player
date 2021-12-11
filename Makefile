GCC_FLAGS="-fcommon"

setup:
	python3 -m venv venv


install-apt-deps:
	sudo apt-get install ir-keytable -y

install-deps:
	export GCC_FLAGS=$(GCC_FLAGS)
	./venv/bin/pip install -e vlc_controller
	./venv/bin/pip install -e remote_controller

install-dev-deps:
	./venv/bin/pip install -r dev_requirments.txt

setup-ir-keys:
	sudo ir-keytable -p all
	sudo ir-keytable

install: install-dev-deps install-deps setup-ir-keys

test-ir-keys:
	ir-keytable -t -s rc0

vlc-controller-tests:
	./venv/bin/python -m pytest vlc_controller/tests

tests: vlc-controller-tests

run-controller:
	./venv/bin/python -m remote_controller
