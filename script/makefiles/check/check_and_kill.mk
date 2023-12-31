# Check and kill the process on port 8000
check_and_kill:
	@if lsof -i :8000; then \
		echo "Port 8000 is already in use. Killing the process..."; \
		lsof -ti :8000 | xargs kill -9; \
	fi

check_and_kill_5555:
	@if lsof -i :5555; then \
		echo "Port 5555 is already in use. Killing the process..."; \
		lsof -ti :5555 | xargs kill -9; \
	fi
