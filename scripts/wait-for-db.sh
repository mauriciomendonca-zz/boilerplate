#!/bin/sh
set -e
cd $(dirname $0)
pwd
echo Waiting for DB...
./wait-for ${POSTGRES_HOST}:5432
echo DB is up
