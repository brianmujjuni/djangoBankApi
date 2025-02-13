
#!/bin/bash

set -o errexit
set -o nounset
set -o pipfail

python manage.py migrate django_celery_beat

rm -f './celerybeat.pid'

exec watchfiles --filter python celery.__main__.main --args '-A config.celery_app beat -l INFO'
