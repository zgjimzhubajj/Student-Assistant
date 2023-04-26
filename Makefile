PYTHON :=
ifeq ($(OS),Windows_NT)
	PYTHON=.venv\Scripts\python
else
	PYTHON=.venv/bin/python
endif

venv:
	test -d .venv || python -m venv .venv/
	. .venv/Scripts/activate

install-requirements: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install -r requirements.txt

install-toml: check-venv
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m pip install .

## creates dist files and package release files based on pyproject.toml (depends on check-virtual-env)
build-toml: install-toml
	$(PYTHON) -m pip install --upgrade -q pip
	$(PYTHON) -m build

check-venv:
	@if [ -z "$$(which python | grep -o .venv)" ]; then \
		exit 1; \
	fi

pylint: check-venv
	@find Program/ -name '*.py' -print0 | xargs -0 pylint -d C0103 -rn

test: check-venv
	$(PYTHON) Program/test_read_db.py
	$(PYTHON) Program/test_write_db.py

flake8: check-venv
	@$(call MESSAGE,$@)
	@-flake8 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.nox,.eggs,*.egg,.venv,venv,*.pyc

clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

coverage-read:
	@$(call MESSAGE,$@)
	coverage run Program/test_read_db.py  
	coverage html
	coverage report -m
	
coverage-write:
	@$(call MESSAGE,$@) 
	coverage run Program/test_write_db.py
	coverage html
	coverage report -m

# Calculate software metrics for your project.

radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average Program

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show Program

radon-raw:
	@$(call MESSAGE,$@)
	radon raw Program

radon-hal:
	@$(call MESSAGE,$@)
	radon hal Program

metrics: radon-cc radon-mi radon-raw radon-hal cohesion

