#!/usr/bin/env bash

set -e

cmd="$@"

until  PGPASSWORD=$PG_PASSWORD psql -h $PG_HOST -U $PG_USER -d $PG_DB -c "\q" ; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd