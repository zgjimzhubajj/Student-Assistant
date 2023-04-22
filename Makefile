#!/usr/bin/env make

# Change this to be your variant of the python command
# Set the env variable PYTHON to another value if needed
# PYTHON=python3 make version
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	-cd Program && $(PYTHON) -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black Program/ test_controller.py
	 $(PYTHON) -m black Program/ test_read_db.py
	 $(PYTHON) -m black Program/ test_write_db.py

codestyle: black


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m unittest discover Program

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover Program
	coverage report -m

test: lint coverage


# ---------------------------------------------------------


# ---------------------------------------------------------
# Calculate software metrics for your project.
#
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

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory Program

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive Program
