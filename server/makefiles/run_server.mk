# Run Django server
run_server: check_and_kill create_venv_activate
	python manage.py runserver 0.0.0.0:8000

# Check and kill the process on port 8000
check_and_kill:
	@if lsof -i :8000; then \
		echo "Port 8000 is already in use. Killing the process..."; \
		lsof -ti :8000 | xargs kill -9; \
	fi
