#!/bin/bash

set -0 errexit

set -o pipefail

set -o nounset

python << END
    import sys
    import time
    import psycopg2
    suggest_unrecoverable_after = 30
    start = time.time()
    while True:
    try:
        psycopg2.connect(
            dbname="${POSTGRES_DB}",
            user="${POSTGRES_USER}",
            password="${POSTGRES_PASSWORD}",
            host="${POSTGRES_HOST}",
            port="${POSTGRES_PORT}"
        )
        break
    except psycopg2.OperationalError as error:
        sys.stderr.write("Waiting for PostgresSql to become available...\n")
        if time.time() - start > suggest_unrecoverable_after:
            sys.stderr.write(
                "PostgresSql is taking an unusually long time to become available".
                "error: '{}'\n".format(error))
        time.sleep(3)
END

echo >&2 'PostgresSql is available'

exec "$@"