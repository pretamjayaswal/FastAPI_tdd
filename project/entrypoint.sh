#!/bin/sh

echo "Waiting for postgres...."

while ! nc -z web-db 5432; do
    sleep 0.1
done


echo "Postgres Started"
echo "$@"