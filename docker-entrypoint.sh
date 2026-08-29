#!/bin/bash

echo "Intalling Dependencies"
pip install -r requirements.txt

exec "$@"
