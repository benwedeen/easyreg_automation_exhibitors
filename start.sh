#!/bin/bash
pip3  install -r requirements.txt
python3 -m pytest  Tests\test_easy.py -v -s --alluredir=allure-results
