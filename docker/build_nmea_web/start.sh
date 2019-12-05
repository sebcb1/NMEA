#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib
cd /app/NMEA-master/web
python3 manage.py runserver 0:8000 



