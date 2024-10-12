#!/bin/bash

isort notify.py
black notify.py
flake8 notify.py
mypy notify.py
