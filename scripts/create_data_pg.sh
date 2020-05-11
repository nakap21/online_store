#!/usr/bin/env bash

set -e
set -u

echo "Start creating database '$POSTGRES_BASE'"
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	CREATE USER $POSTGRES_BASE;
	CREATE DATABASE $POSTGRES_BASE;
	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_BASE TO $POSTGRES_BASE;
EOSQL
echo "Finish creating database '$POSTGRES_BASE'"


