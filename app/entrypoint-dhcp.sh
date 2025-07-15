#!/bin/bash

function database_ready() {
    python3 database_check.py
}

until database_ready; do
  echo "The database is not available - waiting..."
  sleep 10
done
echo "The database is ready!"

echo "Starting DHCP server..."
python3 manage.py rundhcp