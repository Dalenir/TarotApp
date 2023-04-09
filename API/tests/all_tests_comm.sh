#!/bin/sh

mkdir -p "reports/flake8_report"
flake8 --config tests/.flake8
pytest
allure generate reports/allure -o reports/generated
allure-combine reports/generated
