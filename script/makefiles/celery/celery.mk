start-celery-worker:
	celery -A Backend worker -l info &

start-celery-beat:
	celery -A Backend beat -l info &