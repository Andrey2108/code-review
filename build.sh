#!/bin/bash
docker-compose up -d --build
python app.py migrate
pip install -r requirements.txt
