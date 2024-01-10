PORT = 9001
check_and_kill:
	@if lsof -i :$(PORT); then \
		echo "Port $(PORT) is already in use. Killing the process..."; \
		lsof -ti :$(PORT) | xargs kill -9; \
	fi


run:
	npm start


all: check_and_kill run
