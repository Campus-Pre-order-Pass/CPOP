#!/bin/bash

source .venv/bin/activate

cd Server
python  manage.py runserver  0.0.0.0:8000