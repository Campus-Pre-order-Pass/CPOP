# Run Django server
run_server_wsgi:
	gunicorn Backend.wsgi:application