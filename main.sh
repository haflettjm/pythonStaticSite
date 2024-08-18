#! /bin/bash

python3 -m venv env
source env/bin/activate

pip install -r ./src/requirements.txt

python src/main.py
