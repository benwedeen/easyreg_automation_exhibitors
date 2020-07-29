#!/bin/bash
##
pip3  install -r requirements.txt
<<<<<<< HEAD
python3 -m pytest  Tests\test_easy.py -v -s --alluredir=allure-results
=======
python3 -m pytest tests_easy.py -v -s --alluredir=allure-results
>>>>>>> origin/master
