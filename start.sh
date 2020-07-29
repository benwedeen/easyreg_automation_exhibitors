#!/bin/bash
pip3  install -r requirements.txt
python3 -m pytest --alluredir=allure-results Tests\test_easy.py -v -s
