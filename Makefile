GCC_FLAGS="-fcommon"

setup:
	python3 -m venv venv

install-deps:
	export GCC_FLAGS=$(GCC_FLAGS)
	./venv/bin/pip install -r requirments.txt

install-dev-deps:
	./venv/bin/pip install -r dev_requirments.txt

install: install-dev-deps install-deps


vlc-controller-tests:
	./venv/bin/python -m pytest vlc_controller/tests

tests: vlc-controller-tests