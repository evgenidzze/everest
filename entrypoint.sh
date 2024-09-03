#!/bin/bash

flask db migrate
flask db upgrade

# Запускаємо додаток Flask
flask run --host=0.0.0.0
