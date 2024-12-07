SHELL := /bin/bash

.PHONY: format

format:
	black *.py
